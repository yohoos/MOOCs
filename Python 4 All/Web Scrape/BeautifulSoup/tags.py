import requests
from bs4 import *

url = raw_input('Enter - ')
html = requests.get(url).text

soup = BeautifulSoup(html)

tags = soup('span', 'comments')
total = 0
count = 0
for tag in tags:
    count += 1
    total += int(tag.text)
print 'Count', count
print 'Sum', total
