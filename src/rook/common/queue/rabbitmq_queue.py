"""
Implementations of queues using RabbitMQ.
"""
import json
import pika

from .queue import QueueReceiver, QueueSender

class RabbitMQQueueReceiver(QueueReceiver):
    
    def __init__(self, conn_factory):
        self.conn_factory = conn_factory

    def receive(self, queue_name, handler):
        with self.conn_factory() as q_conn:
            q_channel = q_conn.channel()
            q_channel.queue_declare(queue=queue_name)
            self._register_consumer(q_channel, queue_name, handler)
            q_channel.start_consuming()

    def _register_consumer(self, q_channel, queue_name, handler):
        q_channel.basic_consume(
            queue=queue_name,
            on_message_callback=self._create_handler_callback(handler),
            auto_ack=True
        )
                
    def _create_handler_callback(self, handler):
        def callback(q_channel, method, properties, body):
            handler(json.loads(body))
        return callback

class RabbitMQQueueSender(QueueSender):
    def __init__(self, conn_factory):
        self.conn_factory = conn_factory
        self._declared_queues = set()
        
    def _declare_queue(self, queue_name, q_channel):
        if not queue_name in self._declared_queues:
            q_channel.queue_declare(queue=queue_name)
            self._declared_queues.add(queue_name)

    def send_session(self, callback):
        with self.conn_factory() as q_conn:
            q_channel = q_conn.channel()
            def sender(queue_name, obj):
                self._declare_queue(queue_name, q_channel)
                q_channel.basic_publish(
                    exchange='',
                    routing_key=queue_name,
                    body=json.dumps(obj))
            callback(sender)