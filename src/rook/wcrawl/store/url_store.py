import datetime as dt
import hashlib

from abc import ABC, abstractmethod

class URLStore(ABC):
    
    @abstractmethod
    def save(self, url, content_type, retrieval_time, writer):
        pass

    @abstractmethod
    def get(self, url, reader):
        pass
    
class BlobInfoURLStore(URLStore):
    
    def __init__(self, blob_store, url_info_store):
        self.blob_store = blob_store
        self.url_info_store = url_info_store
    
    def get(self, url, reader):
        url_info = self.url_info_store.get(url)
        if url_info is None:
            return None
        blob_id = self._get_id(url_info['url'])
        return self.blob_store.read(blob_id, lambda fh: reader(url_info, fh))
        
    def save(self, url, content_type, retrieval_time, writer):
        blob_id = self._get_id(url)
        self.blob_store.write(blob_id, writer)
        self.url_info_store.save(url, content_type, retrieval_time)
        
    def _get_id(self, url):
        h = hashlib.sha256()
        h.update(url.encode('utf-8'))
        return h.hexdigest()
