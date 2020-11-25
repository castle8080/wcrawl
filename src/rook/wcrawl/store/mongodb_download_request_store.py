import datetime as dt

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from .download_request_store import DownloadRequestStore

class MongoDBDownloadRequestStore(DownloadRequestStore):
        
    def __init__(self, mongodb_client: MongoClient, db_name: str):
        self.mongodb_client = mongodb_client
        self.db_name = db_name
        self.db = self.mongodb_client[self.db_name]
        self.download_requests = self.db['download_requests']

    def add(self, url: str) -> bool:
        try:
            self.download_requests.insert_one({ '_id': url, 'request_datetime': dt.datetime.utcnow()})
            return True
        except DuplicateKeyError as e:
            return False

    def size(self) -> int:
        return self.download_requests.count_documents({})

    def list(self, limit: int = -1):
        cur = self.download_requests.find({})
        if limit >= 0:
            cur = cur.limit(limit)
        return list(map(self._fix_id, cur))

    def remove(self, url: str) -> bool:
        result = self.download_requests.delete_one({'_id': url})
        return result.deleted_count == 1
    
    def clear(self) -> None:
        result = self.download_requests.delete_many({})

    def pop_random(self):
        results = list(self.download_requests.aggregate([{ '$sample': { 'size': 1 } }]))
        if len(results) > 0:
            result = results[0]
            self.download_requests.delete_one({ '_id': result['_id'] })
            return self._fix_id(result)
        else:
            return None

    def _fix_id(self, url_obj):
        if url_obj is not None:
            url_obj = url_obj.copy()
            url_obj['url'] = url_obj['_id']
            del(url_obj['_id'])
            return url_obj