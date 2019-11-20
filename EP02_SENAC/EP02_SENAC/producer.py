import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fila'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = {
    "nome":"Usuario 123",
    "email":"usuario@empresa.com.br",
    "data_nascimento":"1980-01-01"
}

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()