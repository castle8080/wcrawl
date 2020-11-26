import cgi
import urllib
from urllib.robotparser import RobotFileParser

class RobotStore:
    def __init__(self, url_store):
        self.url_store = url_store
        
    def get_robots(self, url, download_handler):
        robots_url = self._get_robots_url(url)
        (robots_url_info, robots_url_content) = self._get_robots_content(robots_url, download_handler)

        if robots_url_content is None:
            return None
        
        content_type, ct_attrs = cgi.parse_header(robots_url_info['content_type'])
        charset = ct_attrs.get('charset', None)
        if charset is None or charset == '':
            charset = 'utf-8'
        
        rf_parser = RobotFileParser()
        rf_parser.parse(robots_url_content.decode(charset).splitlines())
        return rf_parser
            
    def _get_robots_content(self, robots_url, download_hanlder):
        robots_url_info, robots_url_content = self._get_robots_content_from_cache(robots_url)
        print(robots_url_info)
        if robots_url_content is None and robots_url_info is None:
            download_handler({
                'url': robots_url,
                'fire_downloaded': False,
                'check_robots': False,
                'record_not_found': True
            })
            robots_url_info, robots_url_content = self._get_robots_content_from_cache(robots_url)
            print(robots_url_info)
        return (robots_url_info, robots_url_content)
        
    def _get_robots_content_from_cache(self, robots_url):
        robots_result = self.url_store.get(robots_url, lambda url_info, fh: (url_info, fh.read() if fh else None))
        if robots_result is None:
            return (None, None)
        else:
            return robots_result        

    def _get_robots_url(self, url):
        url_p = urllib.parse.urlparse(url)
        url_robots = url_p.scheme + "://" + url_p.netloc + "/robots.txt"
        return url_robots
