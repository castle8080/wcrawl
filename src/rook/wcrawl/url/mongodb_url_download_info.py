
from .url_download_info import URLDownloadInfo

class MongoDBURLDownloadInfo(URLDownloadInfo):
    
    def __init__(self, mongodb_client):
        self.mongodb_client = mongodb_client
        self.db = self.mongodb_client.wcrawl
        self.urls = self.db.urls
        
    def add_info(self, url, content_type, retrieved, blob_id):
        self.urls.insert_one({
            'url': url,
            'content_type': content_type,
            'retrieved': retrieved,
            'blob_id': blob_id
        })
    
    def get_info(self, url):
        with self.urls.find({ 'url': url }) as cur:
            return list(cur)