from downloader import Downloader
from view import g_view

files = {}
numbers = ['first', 'second', 'three']

numberFiles = int(input('Number of files -> '))
for file in range(numberFiles):
    g_view.showMessage(f'\n{numbers[file]} file:')
    files[input('filename - > ')] = input('link -> ')

for filename, link in files.items():
   Downloader(link, filename)