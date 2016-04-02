import urllib
from bs4 import *

url = raw_input('Enter - ')
count = int(raw_input('Enter count: ')) + 1
pos = int(raw_input('Enter position: ')) - 1

for i in range(count):
    html = urllib.urlopen(url).read()
    print 'Retrieving: ', url
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[pos].get('href', None)
