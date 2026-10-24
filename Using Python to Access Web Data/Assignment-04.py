import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors (useful across different OS environments)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print(f'Retrieving {url}')

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print(f'Retrieved {len(data)} characters')

# Parse the XML data from string
tree = ET.fromstring(data)

# Find all 'count' tags anywhere in the XML tree
counts = tree.findall('.//count')

total_sum = 0
total_count = len(counts)

for item in counts:
    total_sum += int(item.text)

print(f'Count: {total_count}')
print(f'Sum: {total_sum}')
