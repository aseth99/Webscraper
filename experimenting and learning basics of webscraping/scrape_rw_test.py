from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	#tests for bad html
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), 'lxml')
		title = bsObj.body.h1
	#tests for bad attributes
	except AttributeError as e:
		return None
	return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
	print("Title couldnt be found...")
else:
	print(title)