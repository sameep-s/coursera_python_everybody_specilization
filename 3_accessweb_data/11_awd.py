#Assignment 1
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl 

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all anchor tags
tags = soup('span')
sum = 0
for tag in tags:
#	print(tag.get('class', None))
#	print(tag.attrs)
	intTag= int(tag.contents[0])
	sum = sum + intTag
print(sum)
