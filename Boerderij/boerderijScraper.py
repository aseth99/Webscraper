from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

import ssl

import csv
from datetime import datetime

#SSL: CERTIFICATE_VERIFY_FAILED
#to bypass verification....:
#https://access.redhat.com/articles/2039753 explains certificate verification in python
#i bypassed verification, not sure if that is correct way of doing it, or if i should try and get url verified

# This restores the same behavior as before.
context = ssl._create_unverified_context()
#urllib.urlopen("https://no-valid-cert", context=context )
#https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error where i got bypassing verification code


try:
	html = urlopen("https://www.boerderij.nl/", context=context)
except HTTPError as e:
	print(e) #website exists, file doesnt?
	#return null, break or other...
except URLError as e:
	print("server couldnt be found") #url is wrong
else:
	print("no HTTPError or URLError")
	#continues...


html = urlopen("https://www.boerderij.nl/", context=context)
bsObj = BeautifulSoup(html, "lxml")


titleList = bsObj.findAll("article", {"class":"media-ankeiler"})
with open("boerderij.csv", "a") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(["TITLE OF ARTICLE", "URL OF ARTICLE", "SUMMARY", "DATE/TIME INFO WAS EXTRACTED"])

for childlist in titleList:
# 	# print("title of article: ", name.get_text())
# 	#for child in childlist.children:

#i think this kinda works, gets all the articles, but there are some articles at the bottom which may be irrevelant
	print("article title: ")
	print(childlist.findNext("a")["title"])
	print("\n")

	print("article url: ")
	print(childlist.findNext("a")["href"])
	print("\n")

	print("article summary: ")
	print(childlist.findNext("p").get_text())
	print("\n")
	with open("boerderij.csv", "a") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([childlist.findNext("a")["title"], childlist.findNext("a")["href"], childlist.findNext("p").get_text(), datetime.now()])

#name.findNext("p").get_text()

	#print(childlist)

# titleList = bsObj.findAll("a", {"id": "title"})
# #linkList = bsObj.findAll("a", href=True)
# summaryList = bsObj.findAll("p", {"id": "summary"})


# #loop prints out each article, url and paragraph
# #each loop also writes a new row with that info into the csv file
# for name in titleList:
# 	print("title of article: \n", name.get_text())
# 	print("url: \n", name["href"])
# 	print("\nfirst paragraph of article: \n", name.findNext("p").get_text())
# 	with open("foodingredientsfirst.csv", "a") as csv_file:
# 		writer = csv.writer(csv_file)
# 		writer.writerow([name.get_text(), name.findNext("p").get_text(), name["href"], datetime.now()])

# 	#ayeee it works
	
# # for summ in summaryList:
# # 	print(summ.get_text())

# # for a in soup.findAll('a', href=True):
# #     print "Found the URL:", a['href']

# #now that we have info, lets store in csv

# # open a csv file with append, so old data will not be erased

	
