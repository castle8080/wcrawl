"""
Adds support for URL info using MongoDB.
"""
from rook.common.container import singleton, Provider
from pymongo import MongoClient
from rook.wcrawl.store.mongodb_url_info_store import MongoDBURLInfoStore

class MongoDBProvider(Provider):

    @singleton
    def mongodb_client(self):
        return MongoClient(**self.mongodb_credentials())

    @singleton
    def url_info_store(self):
        return MongoDBURLInfoStore(self.mongodb_client())