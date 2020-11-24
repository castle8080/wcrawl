from abc import ABC, abstractmethod

class URLDownloadInfo(ABC):
        
    @abstractmethod
    def add_info(self, url, content_type, retrieved, blob_id):
        pass
    
    @abstractmethod
    def get_info(self, url):
        pass