import time

class URLDownloadedHandler:

    def __call__(self, request):
        print(f"URLDownloadedHandler: {request}")
        time.sleep(1)
        print("after sleep")
