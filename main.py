from downloader import downloadFile
from log import initializeLogger

def download():
    downloadFile('', 'git.txt')
    downloadFile('https://raw.githubusercontent.com/LunexCoding/EasyGeometry/main/version.txt', 'git1.txt')
    downloadFile('gfgfg', 'git2.txt')
    downloadFile('hhtp://fgjfn', 'git3.txt')
    downloadFile('http://', 'git4.txt')
    downloadFile('raw.githubusercontent.com/LunexCoding/EasyGeometry/main/version.txt', 'git.txt5')
    downloadFile('htt://raw.githubusercontent.com/LunexCoding/EasyGeometry/main/version.txt', 'git.txt7')
    downloadFile('-', 'git.txt8')
    downloadFile('   ', 'git.txt9')

if __name__ == "__main__":
    LOGGER = initializeLogger('main')
    LOGGER.info('Start app.')
    download()
    LOGGER.info('Completion of work.')