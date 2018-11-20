from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

import re
import ssl
import random
import datetime
import time

context = ssl._create_unverified_context()
random.seed(datetime.datetime.now())

pages = set()


#get internal links
def getInternalLinks(bsObj, includeUrl):
	includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
	internalLinks = []

	#find all links that begin with "/"
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				if(link.attrs['href'].startswith("/")):
					internalLinks.append(includeUrl+link.attrs['href'])
				else:
					internalLinks.append(link.attrs['href'])
	return internalLinks

#get external links
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []

	#find all links that begin with http, doesnt begin with same url
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks


def getRandomExternalLink(startingPage):
	#html = urlopen(startingPage, context=context)
	

	
	print("opening... "+ startingPage)
	html = urlopen(startingPage, context=context)


	bsObj = BeautifulSoup(html, "lxml")
	externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
	if len(externalLinks) == 0:
		print("no external links, looking around for one...\n")
		domain = urlparse(startingPage).scheme + "://" +urlparse(startingPage).netloc
		internalLinks = getInternalLinks(bsObj, domain)

		print("len internal links: ", len(internalLinks))
		if len(internalLinks) == 0:
			print("no internal or external links...starting over...")
			return followExternalOnly("https://www.foodingredientsfirst.com/news/category/dairy.html")
		else:
			return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	print("starting site is: "+ startingSite)
	print("random external link is: "+externalLink)
	
	try:
		html = urlopen(externalLink, context=context)
	except HTTPError as e:
		print("http error.. program about to break... so repeating prev link") #website exists, file doesnt?
		#return null, break or other...
		followExternalOnly(startingSite)

	except URLError as e:
		print("server couldnt be found, program about to break... so repeating prev link") #url is wrong
		followExternalOnly(startingSite)

	else:
		print("it works")
		followExternalOnly(externalLink)

		#continues...


#
#collect list of urls

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
	html = urlopen(siteUrl, context=context)
	domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
	bsObj = BeautifulSoup(html, "lxml")
	internalLinks = getInternalLinks(bsObj, domain)
	externalLinks = getExternalLinks(bsObj, domain)

	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print(link)
	for link in internalLinks:
		if link not in allIntLinks:
			allIntLinks.add(link)
			print(link)

allIntLinks.add("https://www.foodingredientsfirst.com/news/category/dairy.html")
getAllExternalLinks("https://www.foodingredientsfirst.com/news/category/dairy.html")

followExternalOnly("https://www.foodingredientsfirst.com/news/category/dairy.html")





















