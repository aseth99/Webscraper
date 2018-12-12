import os, datetime, re, hashlib
import requests

import csv
from datetime import datetime
from bs4 import BeautifulSoup

#Function to extract all URLs of complete articles from news page
def LinkExtractor(content):
        links = []
        newssoup = BeautifulSoup(content, 'lxml')
        newslink = newssoup.find_all('a', id = 'title')
        for link in newslink:
            links.append(link.get('href'))
        return(links)

#Scrape contents of newspage and extract all URLs of complete articles
r = requests.get('http://www.foodingredientsfirst.com/news/category/news.html')
allLinks = LinkExtractor(r.content)

#Remove URLs that are in the list previousUrls (whch have been scraped before)
# allLinks = [link for link in allLinks if link not in previousUrls]
# print("2nd")
# print(allLinks)

#For each URL, scrape the full artcle, store in dict and append to list of dicts


with open("foodingredientsfirst2.csv", "a") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(["TITLE OF ARTICLE", "TEXT", "URL OF ARTICLE", "publication DATE", "DATE/TIME  INFO WAS EXTRACTED", "SOURCE", "ARTICLE ID"])

documents = []
if len(allLinks) != 0:
    for link in allLinks:
        try:
            r = requests.get(link)
            articlesoup = BeautifulSoup(r.content, 'lxml')
            title = articlesoup.title.get_text()
            bodyText = ''
            for string in articlesoup.find(class_ ='article_text' ).stripped_strings:
                bodyText += string

            dict = {}
            dict['url'] = link
            dict['title'] = title
            dict['publication date'] = bodyText[0:11]
            dict['text'] = bodyText[16:]
            dict['source'] = 'FoodIngredientsFirst'
            dict['articleID'] = hashlib.sha1(dict['title'].encode()).hexdigest()
            print(dict)
            print("\n")
            # documents.append(dict)

            print("got to here..")
            with open("foodingredientsfirst2.csv", "a") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([dict['title'], dict['text'], dict['url'], dict['publication date'], datetime.now(), dict['source'], dict['articleID']])

            
        except:
            print('This link was not scraped:\n', link)

