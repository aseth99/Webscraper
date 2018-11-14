from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
#could have page is not found or server is not found...
bsObj = BeautifulSoup(html.read(), 'lxml')

print(bsObj.h1)
#print(bsObj.nonExtinetTAg.sometag) --> attribute error, object doesnt have attribute sometag


