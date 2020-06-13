#Assignment 2
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#To verify Security certificates.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter Url :')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

pos= int(input('Enter Position :'))-1
count=int(input('Enter Count : '))
sequence = []

i = 1
tags = soup('a')
while i <= count:
	link = tags[pos].get('href', None)
	print('Retrieving:', link)
	sequence.append(tags[pos].contents[0])
	html = urllib.request.urlopen(link, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	link = tags[pos].get('href', None)
	i = i + 1
print(sequence[-1])