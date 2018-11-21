from tweepy import Cursor
from twitter_scraper_client import get_twitter_client


if __name__ == '__main__':
	client = get_twitter_client()

	for status in Cursor(client.home_timeline).items(100):
		#process single status
		print(status.text)