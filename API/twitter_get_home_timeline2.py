
from tweepy import Cursor
from twitter_scraper_client import get_twitter_client


if __name__ == '__main__':
	client = get_twitter_client()

	#prints out the x number of tweets at top of timeline
	for status in Cursor(client.home_timeline).items(100):

		#process single status
		print(status.text)