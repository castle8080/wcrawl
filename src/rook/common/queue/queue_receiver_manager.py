from threading import Thread

class QueueReceiverThread(Thread):
    def __init__(self, receiver, queue_name, handler):
        super().__init__()
        self.receiver = receiver
        self.queue_name = queue_name
        self.handler = handler

    def run(self):
        print(f"Start receiving from {self.queue_name}")
        self.receiver.receive(self.queue_name, self.handle)

    def handle(self, msg):
        try:
            self.handler(msg)
        except Exception as e:
            print(f"[ERROR] handling message: {msg} - {e}")

class QueueReceiverManager:

    def __init__(self, receiver):
        self.receiver = receiver
        self.receiver_threads = {}

    def subscribe(self, queue_name, handler):
        rt = QueueReceiverThread(self.receiver, queue_name, handler)
        rt.start()
        if queue_name not in self.receiver_threads:
            self.receiver_threads[queue_name] = []
        self.receiver_threads[queue_name].append(rt)

