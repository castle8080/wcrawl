"""
Abstraction for storing and accessing binary objects.
"""
from abc import ABC, abstractmethod

class BlobStore(ABC):

    @abstractmethod
    def write(self, file_id, stream_callback):
        pass
    
    @abstractmethod
    def read(self, file_id, stream_callback):
        pass
