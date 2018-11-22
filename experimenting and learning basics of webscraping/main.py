import requests
from bs4 import BeautifulSoup

url = 'https://api.coinbase.com/v2/prices/USD/spot?'
response = requests.get(url).json()

print(response)

for x in range(11):
	print((response['data'][x]['currency'])+" "+(response['data'][x]['base'])+" "+(response['data'][x]['amount']))


#response: {'data': [{'currency': 'USD', 'base': 'BTC', 'amount': '7590.01'}, {'currency':'USD', 'base': 'ETH', 'amount': '296.86'}, {'currency': 'USD', 'base': 'LTC', 'amount': '54.59'}]}

# print(response)
# soup = BeautifulSoup(response.content, 'html.parser')
# seven_day = soup.find(id="seven-day-forecast")
# bitcoin = soup.find('pre',{'style':'word-wrap: break-word; white-space: pre-wrap;'})

# print(bitcoin)