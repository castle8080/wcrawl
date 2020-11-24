"""
Adds support for URL info using MongoDB.
"""
from rook.common.container import singleton, Provider
from pymongo import MongoClient
from rook.wcrawl.url.mongodb_url_download_info import MongoDBURLDownloadInfo

class MongoDBProvider(Provider):

    @singleton
    def mongodb_client(self):
        return MongoClient(**self.mongodb_credentials())

    @singleton
    def url_download_info(self):
        return MongoDBURLDownloadInfo(self.mongodb_client())