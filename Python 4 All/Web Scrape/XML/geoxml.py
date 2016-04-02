import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
xml = urllib.urlopen(url)
print 'Retrieving', url
data = xml.read()
tree = ET.fromstring(data)

count = 0
counts = tree.findall('.//count')

for x in counts:
    count += int(x.text)
print count
