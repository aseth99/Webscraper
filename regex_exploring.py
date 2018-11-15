#EMAIL IDENTIFYING - REGEX EXAMPLE

#regex orgin from perl, this is pythons interpretation
#regex differ slightly with language

# uppercase, lowercase, numbers 0-9, periods, + sign, _ underscore:
# [A-Za-z0-9\._+]+
# @:
# # @
# at least one uppercase or lowercase letter:
# [A-Za-z]+
# (.):
# # \.
# ends with com, org, edu or net:
# (com|org|edu|net)

#[] means anything inside bracket is recognized
#[]+ means anything inside can be repeated any number of times
#if just one thing like : @ : occurs exactly once

#concatenating all the rules we arrive at:
#[A-za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)
#^regex for email address ending in com or org or edu or net

# symbol: example   explanation
# * :  a*b*   preceding chars to * can occur 0 or more times
# + :  a+b+   preceding chars to + can occur 1 or more times
# [] : [A-Z]*  matches any char in the brackets 
# () : (a*b)*  matches exact phrase i think... (capture)
# {m, n} : a{2,3}b{2,3}  matches preceding thing between m&n times, matches a or b between 2-3 times
# [^]  :  [^A-Z]*  matches anything not in the bracket
# |  :  b(a|i|e)d  'pipe' means matches any char separated (or)
# .  :  b.d    means match any single character including space/symbols
# ^  :  ^a  means char or subexpression occurs at beginning of string
# \  : \.\|\\. escape char --> allows u to use special chars
# $  :  [A-Z]*[a-z]*$  used at end of regex, match this to end of string
# ?!  :  ^((?![A-Z]).)*$  means does not contain, preceding chars shouldnt be found, tricky to use, use in conjunction with ^ & $

#most expressions that take in string argument in find(id..) will take regex
#cant do .findAll("img") as layout might change, sites use blank images, etc
#useful to use regex 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
	print(image["src"])


#prints out all ../img/gifts/img[#].jpg files
#regex can be inserted as any arg in BS expression
#allows flexibility in finding target elements





































