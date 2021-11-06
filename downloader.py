import requests
from debug import LOG_WARNING
from const import protocols


class Downloader:
    def __init__(self, url=None, filename=None):
        self._url = url
        self._filename = filename
        self._request = None
        self.downloadFile()

    def downloadFile(self):
        if self._url.split('://')[0] not in protocols:
            if self._url == '':
                invalidURL = "''"
                return LOG_WARNING(f'Invalid URL {invalidURL} . Perhaps you meant http://{self._url}?')
            invalidURL = self._url.split('://')[1]
            return LOG_WARNING(f'Invalid URL {self._url}. \nPerhaps you meant http://{invalidURL}?')

        else:
            self._request = requests.get(self._url)
            if self._request.status_code == 200:
                with open(self._filename, 'wb') as f:
                    f.write(self._request.content)
            else:
              LOG_WARNING('Unknown error {} '.format(self._request.status_code))