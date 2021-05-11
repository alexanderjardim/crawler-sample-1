from lxml import html
from urllib.parse import urlparse

def extract(page_string):
    document = html.fromstring(page_string)
    items = document.xpath('//img[re:test(@src, "\\.png($|\\?)", "i")]/@src', namespaces={'re': 'http://exslt.org/regular-expressions'})
    return items