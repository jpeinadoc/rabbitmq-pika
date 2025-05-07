import pika

# Conexión
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

# Declara (crea si no existe) un exchange llamado 'TestExchange' de tipo 'direct'.
# Los exchanges 'direct' enrutan los mensajes a las colas cuya routing_key coincida exactamente con la del mensaje.
# 'durable=True' asegura que el exchange sobreviva a reinicios del servidor RabbitMQ.
channel.exchange_declare(exchange='TestExchange', exchange_type='direct', durable=True)

# Declara (crea si no existe) una cola llamada 'TestQueue'.
# También es durable para que persista tras reinicios del broker.
channel.queue_declare(queue='TestQueue', durable=True)

# Enlaza la cola 'TestQueue' con el exchange 'TestExchange' usando la routing_key 'mi-route'.
# Esto significa que los mensajes enviados al exchange con routing_key='mi-route' se enviarán a 'TestQueue'.
channel.queue_bind(exchange='TestExchange', queue='TestQueue', routing_key='mi-route')



def callback(ch, method, properties, body):
    print(f"[x] Recibido: {body.decode()}")

channel.basic_consume(queue='TestQueue', on_message_callback=callback, auto_ack=True)
print("[x] Esperando mensajes. Presiona CTRL+C para salir.")
channel.start_consuming()