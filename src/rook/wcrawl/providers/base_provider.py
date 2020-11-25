"""
The base common providers for wcrawl.
"""
from rook.common.container import singleton, Provider
from rook.wcrawl.event.event_publisher import EventPublisher
from rook.wcrawl.handlers.url_download_handler import URLDownloadHandler
from rook.wcrawl.store.url_store import BlobInfoURLStore

class BaseProvider(Provider):

    @singleton
    def event_publisher(self):
        return EventPublisher(self.queue_sender())

    @singleton
    def url_download_handler(self):
        return URLDownloadHandler(self.url_store(), self.event_publisher())

    @singleton
    def url_store(self):
        return BlobInfoURLStore(self.blob_store(), self.url_info_store())

    