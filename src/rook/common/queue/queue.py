"""
Abstractions for working with queues.
"""
from abc import ABC, abstractmethod

class QueueSender(ABC):

    def send(self, queue_name, obj):
        self.send_session(lambda sender: sender(queue_name, obj))

    @abstractmethod
    def send_session(self, callback):
        pass

class QueueReceiver(ABC):

    @abstractmethod
    def receive(self, queue_name, handler):
        pass

class MultiThreadedQueueReceiver:

    def __init__(self, receiver, handler_specs):
        self.receiver = receiver
        self.handler_specs = handler_specs

    def start(self):
        pass