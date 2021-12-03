import requests
from requests import ConnectionError
from .const import *
import os


try:
    os.mkdir('./downloads')
    os.chdir('./downloads')
except OSError:
    os.chdir('./downloads')


class Downloader:
    def __init__(self, url=None, filename=None):
        self._url = url
        self._filename = filename
        self._request = None

    def downloadFile(self):
        try:
            if self._url.split('://')[0] not in protocols:
               print(f'Invalid URL {self._url}')
            else:
                try:
                    self._request = requests.get(self._url)
                    if self._request.status_code == codeStatusOK:
                        with open(self._filename, 'wb') as f:
                            f.write(self._request.content)
                    else:
                      print(f'Unknown error {self._request.status_code}')
                except ConnectionError:
                    print(f"Internet connection not detected.")
        except IndexError:
            print(f'Invalid URL.')
        except:
            print(f'An unexpected error has occurred.')

def downloadFile(url, filename):
    downloader = Downloader(url, filename)
    downloader.downloadFile()
