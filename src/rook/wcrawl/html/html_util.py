import urllib
from bs4 import BeautifulSoup

def is_valid_href(href):
    if href is None or href == '':
        return False
    
    # Fragment
    if href.startswith("#"):
        return False
    
    # Only http/https schemes are supported
    href_p = urllib.parse.urlparse(href)
    if href_p.scheme not in { '', 'http', 'https' }:
        print(href_p.scheme)
        return False
    
    return True

def get_hrefs_from_doc(url, doc):
    links = set()
    for a_tag in doc.findAll('a'):
        href = a_tag.attrs['href']
        if is_valid_href(href):
            href = urllib.parse.urljoin(url, href)
            links.add(href)
            
    links = list(links)
    links.sort()
    return links

def extract_links(url, url_content_fh):
    doc = BeautifulSoup(url_content_fh, features="html.parser")
    links = get_hrefs_from_doc(url, doc)
    return links