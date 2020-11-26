"""
The base common providers for wcrawl.
"""
from rook.common.container import singleton, Provider
from rook.wcrawl.event.event_publisher import EventPublisher
from rook.wcrawl.handlers.url_download_handler import URLDownloadHandler
from rook.wcrawl.handlers.url_downloaded_handler import URLDownloadedHandler
from rook.wcrawl.store.url_store import BlobInfoURLStore
from rook.wcrawl.store.robot_store import RobotStore
from rook.common.queue.queue_receiver_manager import QueueReceiverManager

class BaseProvider(Provider):

    @singleton
    def event_publisher(self):
        return EventPublisher(self.queue_sender())

    @singleton
    def robot_store(self):
        return RobotStore(self.url_store())

    @singleton
    def url_download_handler(self):
        return URLDownloadHandler(self.url_store(), self.event_publisher())

    @singleton
    def url_downloaded_handler(self):
        return URLDownloadedHandler()

    @singleton
    def url_store(self):
        return BlobInfoURLStore(self.blob_store(), self.url_info_store())

    @singleton
    def queue_receiver_manager(self):
        return QueueReceiverManager(self.queue_receiver())