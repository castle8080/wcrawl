"""
Adds support for Blob using a file system.
"""
import os

from rook.common.container import singleton, Provider
from rook.common.blob.filesystem_blobstore import FileSystemBlobStore

class FileSystemProvider(Provider):

    def blob_root_directory(self):
        return os.path.join(self.app_root(), "var/blob")

    @singleton
    def blob_store(self):
        return FileSystemBlobStore(self.blob_root_directory())
