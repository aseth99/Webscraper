from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
import random
import datetime
import time

context = ssl._create_unverified_context()

random.seed(datetime.datetime.now())
def getLink(articleUrl):
	html = urlopen("http://en.wikipedia.org"+articleUrl, context=context)
	bsObj = BeautifulSoup(html, "lxml")
	return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLink("/wiki/Lucas_%26_Steve")

while len(links) > 0:
	newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	time.sleep(1)
	links = getLink(newArticle)
# html = urlopen("https://en.wikipedia.org/wiki/Lucas_%26_Steve", context=context)
# bsObj = BeautifulSoup(html, "lxml")

# # for link in bsObj.findAll("a"):
# #changed for loop and added regex to get rid of unneccesary links
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
# 	if "href" in link.attrs:
# 		#gives all links...

# 		print(link.attrs["href"])

# #now that we can get the links... 
# #function to return list of linked article urls...
# #main function to call the above function to get list of links 

