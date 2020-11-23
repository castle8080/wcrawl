"""
A class which can be used to fire events in the wcrawl system.
"""
from . import events

class EventPublisher:

    def __init__(self, queue_sender):
        self.queue_sender = queue_sender

    def send_url_download(self, url):
        self.queue_sender.send(events.URL_DOWNLOAD, { 'url': url })