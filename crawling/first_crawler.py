from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

context = ssl._create_unverified_context()


html = urlopen("https://en.wikipedia.org/wiki/Lucas_%26_Steve", context=context)
bsObj = BeautifulSoup(html, "lxml")


# for link in bsObj.findAll("a"):
#changed for loop and added regex to get rid of unneccesary links
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
	if "href" in link.attrs:
		#gives all links...

		print(link.attrs["href"])
