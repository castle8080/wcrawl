"""
A handler which responds to a URL download request.
"""
import requests
import urllib
import datetime as dt
import re

class URLDownloadHandler:

    SUPPORTED_CONTENT_TYPES = re.compile(r"^(text/html|text/plain)", re.I)
    CHUNK_SIZE = 1024 * 1024
    
    def __init__(self, url_store, event_publisher, time_provider=None):
        self.url_store = url_store
        self.event_publisher = event_publisher
        self.time_provider = time_provider
        if self.time_provider is None:
            self.time_provider = dt.datetime.utcnow
    
    def __call__(self, request):
        print(f"Request to download: {request['url']}")
        # TODO: check robots.txt
        # TODO: Consider adding if-modified since header?
        
        with requests.get(request['url'], stream=True) as resp:
            content_type = resp.headers['content-type']
            if resp.status_code >= 400:
                raise Exception(f"Could not retrieve {request['url']}")
            elif resp.status_code == 200 and self._is_supported_content_type(content_type):
                self._process_download(request['url'], resp)
        
    def _process_download(self, url, resp):
        content_type = resp.headers['content-type']
        retrieval_time = self.time_provider()

        def write_resp(blob_stream):
            for chunk in resp.iter_content(chunk_size=URLDownloadHandler.CHUNK_SIZE):
                blob_stream.write(chunk)

        self.url_store.save(url, content_type, retrieval_time, write_resp)
        self.event_publisher.send_url_downloaded(url)

    def _is_supported_content_type(self, content_type):
        return URLDownloadHandler.SUPPORTED_CONTENT_TYPES.search(content_type) is not None
