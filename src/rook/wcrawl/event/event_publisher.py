"""
A class which can be used to fire events in the wcrawl system.
"""
import logging
from . import events

logger = logging.getLogger(__name__)

class EventPublisher:

    def __init__(self, queue_sender):
        self.queue_sender = queue_sender

    def send_url_download(self, url):
        logger.debug(f"URL download request: {url}")
        self.queue_sender.send(events.URL_DOWNLOAD, { 'url': url })

    def send_url_downloaded(self, url):
        logger.debug(f"URL downloaded event: {url}")
        self.queue_sender.send(events.URL_DOWNLOADED, { 'url': url })