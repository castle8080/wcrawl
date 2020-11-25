"""
Adds support for URL info using MongoDB.
"""
from rook.common.container import singleton, Provider
from pymongo import MongoClient
from rook.wcrawl.store.mongodb_url_info_store import MongoDBURLInfoStore
from rook.wcrawl.store.mongodb_download_request_store import MongoDBDownloadRequestStore

class MongoDBProvider(Provider):

    @singleton
    def mongodb_client(self):
        return MongoClient(**self.mongodb_credentials())

    @singleton
    def mongodb_db_name(self):
        return "wcrawl"

    @singleton
    def url_info_store(self):
        return MongoDBURLInfoStore(self.mongodb_client(), self.mongodb_db_name())

    @singleton
    def download_request_store(self):
        return MongoDBDownloadRequestStore(self.mongodb_client(), self.mongodb_db_name())