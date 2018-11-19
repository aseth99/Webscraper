from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
import random
import datetime
import time

context = ssl._create_unverified_context()

random.seed(datetime.datetime.now())


pages = set()
#only prints unique pages, no repetitions
def getLink(articleUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+articleUrl, context=context)
	bsObj = BeautifulSoup(html, "lxml")

	#data printing
	try: 
		print("H1: ", bsObj.h1.get_text())
		print("First Paragraph: \n", bsObj.find(id = "mw-content-text").findAll("p")[0])
		print("Edit Link: ", bsObj.find(id = "ca-edit").find("span").find("a").attrs['href'])
	except AttributeError:
		print("This page is missing somethin")

	#looks through all tags and prints the links
	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']

				print('-----------------------\n', newPage)

				#print(newPage)
				pages.add(newPage)
				getLink(newPage)
getLink("/wiki/Lucas_%26_Steve")

	#return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#links = getLink("/wiki/Lucas_%26_Steve")

# while len(links) > 0:
# 	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
# 	print(newArticle)
# 	time.sleep(3)
# 	links = getLink(newArticle)