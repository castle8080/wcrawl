import pymongo
from .url_info_store import URLInfoStore

class MongoDBURLInfoStore(URLInfoStore):
    
    def __init__(self, mongodb_client):
        self.mongodb_client = mongodb_client
        self.db = self.mongodb_client.wcrawl
        self.urls = self.db.urls
        
    def save(self, url, content_type, retrieved):
        self.urls.update(
            { '_id': url },    
            {
                '_id': url,
                'content_type': content_type,
                'retrieved': retrieved
            }, upsert=True)

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