import requests
from requests import ConnectionError
from const import protocols, codeStatusOK
from log import initializeLogger
import os

LOGGER = initializeLogger(__name__)

if not os.path.isdir("downloads"):
    os.mkdir("downloads")
os.chdir("downloads")

class Downloader:
    def __init__(self, url=None, filename=None):
        self._url = url
        self._filename = filename
        self._request = None


    def downloadFile(self):
        try:
            if self._url.split('://')[0] not in protocols:
                LOGGER.warning(f'{self._filename}: Invalid URL {self._url}')
            else:
                try:
                    self._request = requests.get(self._url)
                    if self._request.status_code == codeStatusOK:
                        with open(self._filename, 'wb') as f:
                            f.write(self._request.content)
                        LOGGER.info(f'{self._filename}: Successfully loaded.')
                    else:
                      LOGGER.error(f'{self._filename}: Unknown error {self._request.status_code}')
                except ConnectionError:
                    LOGGER.error(f"{self._filename}: Internet connection not detected.")
        except IndexError:
            LOGGER.error(f'{self._filename}: Invalid URL.')
        except:
            LOGGER.error(f'{self._filename}: An unexpected error has occurred.')

def downloadFile(url, filename):
    downloader = Downloader(url, filename)
    downloader.downloadFile()