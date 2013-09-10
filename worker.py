#!/usr/bin/env python
import pika
import time

## Define your computationally intensive task as a function here.
def intensive_task(n):
    # For now I add a dummy task that takes n seconds to complete.
    time.sleep(n)


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print ' [*] Worker ready waiting for input. To exit press CTRL+C'
print

def callback(ch, method, properties, body):
    print " [x] Received an input: %r" % (body,)
    intensive_task(int(body))
    print " [x] Work has been completed, waiting for next task"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')
channel.start_consuming()
