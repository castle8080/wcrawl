import logging
import time

logger = logging.getLogger(__name__)

# Note: I might to have the handlers named based on task
#       such as link extraction and text analysis instead.
#       Then I need to decide if I want to still use queues.
#       or using multiple subscribers.

class URLDownloadedHandler:

    def __call__(self, request):
        # TODO Implement this.
        logger.debug(f"URLDownloadedHandler: {request}")
        time.sleep(1)
        logger.debug("after sleep")
