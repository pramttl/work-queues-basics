## Basic work queues model demonstration using RabbitMQ
A very basic project on Work Queues serving as a demo for my presentation at IIT (BHU), Varanasi.

## Slide Deck

I have added a presentation on **Basics of distributed task processing with work queues** on speakerdeck -
[here](https://speakerdeck.com/pramttl/basics-of-distributed-task-processing-with-work-queues-amqp)

I prepared this for a seminar at my Institute for the Department of Electronics Engineering.
This idea will help professors at our Institute tap the potential of the available hardware to carry out faster computations for their research.
AMQP & Celery are already common in web applications where it may not be possible to process a request as soon as it is received.
There are many patterns or models in the AMQP protocol of which Work Queues is one simple yet very useful model.

## Code

* RabbitMQ is used as the AMQP server in this repository.
* pika is used as a Python networking client
