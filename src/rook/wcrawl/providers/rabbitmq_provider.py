"""
Adds support for queueing using RabbitMQ.
"""
from ro
from rook.common.container import singleton, Provider
from rook.common.queue.rabbitmq_queue import RabbitMQQueueReceiver, RabbitMQQueueSender

import pika

class RabbitMQProvider(Provider):

    def rabbitmq_connection(self):
        return pika.BlockingConnection(pika.URLParameters(self.rabbitmq_url()))

    @singleton
    def queue_receiver(self):
        return RabbitMQQueueReceiver(self.rabbitmq_connection)

    @singleton
    def queue_sender(self):
        return RabbitMQQueueSender(self.rabbitmq_connection)
