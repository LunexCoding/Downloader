import requests
from requests import ConnectionError
from debug import LOG_WARNING
from const import protocols, codeStatusOK


class Downloader:
    def __init__(self, url=None, filename=None):
        self._url = url
        self._filename = filename
        self._request = None


    def downloadFile(self):
        try:
            if self._url.split('://')[0] not in protocols:
                if self._url == '':
                    invalidURL = "''"
                    LOG_WARNING(f'Invalid URL {invalidURL} . Perhaps you meant http://{self._url}?')
                invalidURL = self._url.split('://')[1]
                LOG_WARNING(f'Invalid URL {self._url}. \nPerhaps you meant http://{invalidURL}?')
            else:
                try:
                    self._request = requests.get(self._url)
                    if self._request.status_code == codeStatusOK:
                        with open(self._filename, 'wb') as f:
                            f.write(self._request.content)
                    else:
                      LOG_WARNING(f'{self._filename}: Unknown error {self._request.status_code}')
                except ConnectionError:
                    LOG_WARNING(f"Internet connection not detected.")
        except IndexError:
            LOG_WARNING('Invalid URL.')
        except:
            LOG_WARNING('An unexpected error has occurred')

def downloadFile(url, filename):
    downloader = Downloader(url, filename)
    downloader.downloadFile()