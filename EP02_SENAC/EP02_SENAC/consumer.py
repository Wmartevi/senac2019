import pika
import time
from pymongo import MongoClient 

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client.ep02_database

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='fila'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    db.ep02_collection.insert_one(body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()