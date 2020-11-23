"""
The base common providers for wcrawl.
"""
from rook.common.container import singleton, Provider
from rook.wcrawl.event.event_publisher import EventPublisher
from rook.wcrawl.handlers.url_downloader import URLDownloader

class BaseProvider(Provider):

    @singleton
    def event_publisher(self):
        return EventPublisher(self.queue_sender())

    def url_download_handler(self):
        return URLDownloader()