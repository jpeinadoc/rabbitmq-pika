import pika

# Conexión
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
channel = connection.channel()
channel.queue_declare(queue='TestQueue', durable=True)

# Enviar
channel.basic_publish(exchange='TestExchange', routing_key='mi-route', body='Hola soy jorge feliz navidad!')
print("[x] Mensaje enviado")

connection.close()