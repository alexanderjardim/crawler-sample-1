import requests
from lxml import html
from os.path import sep, abspath, join
from pathlib import Path
from furl import furl
from requests.exceptions import InvalidSchema, MissingSchema

class Downloader:
    """
    This class implements the implements the file download logic.
    """

    def __init__(self, output=None, login=None, password=None):
       self.login = login
       self.password = password
       self.output = output
       self.auth_active = self.must_authenticate()
    
    def must_authenticate(self):
        if self.login and self.password:
            return True
        return False
    
    def execute_request(self, url):
        try:
            response = None
            if self.auth_active:
                print(url)
                response = requests.get(url, auth=(self.login, self.password))
            else:
                response = requests.get(url)
            if response is not None:
                if response.status_code != 200:
                    print(f"{url} {response.status_code}: {response.reason}")
            return response
        except InvalidSchema as err:
            print(f"URL {url} is invalid. Should contain HTTP or HTTPS scheme")
        except Exception as err:
            print(err)

    def get(self, url):
        page_string = None
        purl = furl(url)
        print(purl)
        self.scheme = purl.scheme
        self.host = purl.host
        self.port = purl.port
        response = self.execute_request(purl)
        if response is not None:
            if response.status_code == 200 and response.content:
                page_string = str(response.content)
            response.close()
        return page_string
    
    def create_path(self, domain_dir, original_path):
        path_dir = "/".join(original_path.segments[:-1])
        path = Path(self.output+sep+domain_dir+sep+path_dir).resolve()
        path.mkdir(parents=True, exist_ok=True)

    def save(self, url):
        try: 
            purl = furl(url)
            purl.host = self.host  if not bool(purl.host) else purl.host
            purl.scheme = self.scheme if not bool(purl.scheme) else purl.scheme
            purl.port = self.port
            response = self.execute_request(purl)
            if response.status_code == 200:
                self.create_path(self.host, purl.path)
                self.save_file(self.host, purl.path, response.content)
            response.close()
        except Exception as err:
            print(err)

    def save_file(self, domain_dir, file_path, file_content):
        filepath = Path(f"{self.output}{sep}{domain_dir}{sep}{file_path}").resolve()
        file = open(filepath, "wb+")
        file.write(file_content)
        print(f"Saved file {filepath}")
        file.close()

        
