"""
Adds support for URL info using MongoDB.
"""
from rook.common.container import singleton, Provider
from pymongo import MongoClient

class MongoDBProvider(Provider):

    @singleton
    def mongodb_client(self):
        return MongoClient(**self.mongodb_credentials())