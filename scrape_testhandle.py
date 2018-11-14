from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html = urlopen("http://www.pythonscraping.com/pages/pfd1.html")
except HTTPError as e:
	print(e) #website exists, file doesnt?
	#return null, break or other...
except URLError as e:
	print("server couldnt be found") #url is wrong
else:
	print("it works")
	#continues...
