import ssl
import urllib.request
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Calypso.html'
count = 7
position = 18

print('Retrieving:', url)
for i in range(count):
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  tags = soup('a')
  url = tags[position - 1].get('href', None)
  print('Retrieving:', url)

print('Last name found:', tags[position - 1].contents[0])
