from urllib.request import urlopen
from bs4 import BeautifulSoup

#SSL: CERTIFICATE_VERIFY_FAILED
#to bypass verification....:
#https://access.redhat.com/articles/2039753 explains certificate verification in python
#i bypassed verification, not sure if that is correct way of doing it, or if i should try and get url verified
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()
#urllib.urlopen("https://no-valid-cert", context=context )
#https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error where i got bypassing verification code

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html = urlopen("https://www.foodingredientsfirst.com/news/category/dairy.html", context=context)
except HTTPError as e:
	print(e) #website exists, file doesnt?
	#return null, break or other...
except URLError as e:
	print("server couldnt be found") #url is wrong
else:
	print("no HTTPError or URLError")
	#continues...



html = urlopen("https://www.foodingredientsfirst.com/news/category/dairy.html", context=context)
bsObj = BeautifulSoup(html, "lxml")

titleList = bsObj.findAll("a", {"id": "title"})
#linkList = bsObj.findAll("a", href=True)
summaryList = bsObj.findAll("p", {"id": "summary"})


for name in titleList:
	print("title of article: \n", name.get_text())
	print("url: \n", name["href"])
	print("\nfirst paragraph of article: \n", name.findNext("p").get_text())
	
# for summ in summaryList:
# 	print(summ.get_text())

# for a in soup.findAll('a', href=True):
#     print "Found the URL:", a['href']
	
