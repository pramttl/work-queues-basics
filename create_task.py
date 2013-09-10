#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

input_data = ' '.join(sys.argv[1:]) or "2"

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=input_data,
    properties=pika.BasicProperties(delivery_mode = 2,) 
    # delivery_mode 2 makes message persistent
)

print " [x] Sent Input - %r - to the queue. " % (input_data,)
connection.close()
