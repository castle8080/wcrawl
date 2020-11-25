from pymongo import MongoClient
from .url_info_store import URLInfoStore

class MongoDBURLInfoStore(URLInfoStore):
    
    def __init__(self, mongodb_client: MongoClient, db_name: str):
        self.mongodb_client = mongodb_client
        self.db_name = db_name
        self.db = self.mongodb_client[self.db_name]
        self.urls = self.db.urls
        
    def save(self, url, content_type, retrieved, exists=True):
        payload = {
            '_id': url,
            'content_type': content_type,
            'retrieved': retrieved
        }
        if not exists:
            payload['exists'] = False

        self.urls.update({ '_id': url }, payload, upsert=True)

    def get(self, url):
        with self.urls.find({ '_id': url }) as cur:
            urls = list(cur)
            if len(urls) == 0:
                return None
            else:
                url = urls[0].copy()
                url['url'] = url['_id']
                del(url['_id'])
                return url