"""
A handler which responds to a URL download request.
"""
import requests
import urllib
import datetime as dt
import re
import logging

logger = logging.getLogger(__name__)

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
        logger.debug(f"Request to download: {request}")
        # TODO: check robots.txt
        # TODO: Consider adding if-modified since header?
        
        with requests.get(request['url'], stream=True) as resp:
            content_type = resp.headers['content-type']
            if (resp.status_code == 404) and request.get('record_not_found', False):
                self._process_not_found(request, resp)
            elif resp.status_code >= 400:
                raise Exception(f"Could not retrieve {request['url']} - {resp.status_code}")
            elif resp.status_code == 200 and self._is_supported_content_type(content_type):
                self._process_download(request, resp)
            else:
                logger.info(f"Unprocessed url: status={resp.status_code}, url={request['url']}")

    def _process_not_found(self, request, resp):
        retrieval_time = self.time_provider()
        self.url_store.save(request['url'], '', retrieval_time, write_resp)
        
    def _process_download(self, request, resp):
        url = request['url']
        content_type = resp.headers['content-type']
        retrieval_time = self.time_provider()

        def write_resp(blob_stream):
            for chunk in resp.iter_content(chunk_size=URLDownloadHandler.CHUNK_SIZE):
                blob_stream.write(chunk)

        self.url_store.save(url, content_type, retrieval_time, write_resp)
        if self._should_fire_downloaded_event(request):
            self.event_publisher.send_url_downloaded(url)

    def _should_fire_downloaded_event(self, request):
        return request.get('fire_downloaded', True)

    def _is_supported_content_type(self, content_type):
        return URLDownloadHandler.SUPPORTED_CONTENT_TYPES.search(content_type) is not None
