from abc import ABC, abstractmethod

class DownloadRequestStore(ABC):
        
    @abstractmethod
    def add(self, url: str) -> bool:
        pass

    @abstractmethod
    def remove(self, url: str) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def list(self, limit: int = -1):
        pass

    @abstractmethod
    def clear(self) -> None:
        pass