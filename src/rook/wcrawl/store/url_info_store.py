from abc import ABC, abstractmethod

class URLInfoStore(ABC):
        
    @abstractmethod
    def save(self, id, url, content_type, retrieved, exists=True):
        pass
    
    @abstractmethod
    def get(self, url):
        pass