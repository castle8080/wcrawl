
"""
A handler which responds to a URL download request.
"""
class URLDownloader:

    def __call__(self, request):
        print(f"Request to download: {request}")

