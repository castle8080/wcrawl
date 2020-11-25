"""
Implementation of BlobStore using a single directory.
"""
import os
from .blobstore import BlobStore

class FileSystemBlobStore(BlobStore):
    def __init__(self, directory):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)
        
    def write(self, file_id, stream_callback):
        filename = self._get_filename(file_id)
        with open(filename, 'wb') as fh:
            return stream_callback(fh)
    
    def read(self, file_id, stream_callback):
        filename = self._get_filename(file_id)
        with open(filename, 'rb') as fh:
            return stream_callback(fh)

    def delete(self, file_id):
        filename = self._get_filename(file_id)
        os.remove(filename)

    def _get_filename(self, file_id):
        return os.path.join(self.directory, file_id)