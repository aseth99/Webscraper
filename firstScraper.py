from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
#could have page is not found or server is not found...
bsObj = BeautifulSoup(html.read(), 'lxml')

print(bsObj.h1)
#print(bsObj.nonExistentTag.sometag) --> attribute error, object doesnt have attribute sometag




#psuedocode
try:
	badContent = bsObj.nonExistentTag.anotherTag
except AttributeError as e:
	print("Tag not found...")
else: 
	if badContent == None:
		print("Tag not found...")
	else:
		print(badContent)