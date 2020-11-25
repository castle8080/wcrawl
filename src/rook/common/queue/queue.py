"""
Abstractions for working with queues.
"""
from abc import ABC, abstractmethod
import json

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

class ListQueueSender(QueueSender):
    """
    A QueueSender which saves messages into lists.
    """

    def __init__(self):
        self.queues = {}
    
    def clear(self):
        self.queues = {}

    def next_message(self, queue_name):
        if not queue_name in self.queues:
            return None
        if len(self.queues[queue_name]) == 0:
            return None
        msg = self.queues[queue_name].pop()
        return json.loads(msg)

    def send(self, queue_name, obj):
        self.send_session(lambda sender: sender(queue_name, obj))

    def send_session(self, callback):
        def on_send(queue_name, obj):
            if queue_name not in self.queues:
                self.queues[queue_name] = []
            self.queues[queue_name].append(json.dumps(obj))
        callback(on_send)

class MultiThreadedQueueReceiver:

    def __init__(self, receiver, handler_specs):
        self.receiver = receiver
        self.handler_specs = handler_specs

    def start(self):
        pass