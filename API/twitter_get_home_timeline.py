import json
from tweepy import Cursor
from twitter_scraper_client import get_twitter_client


if __name__ == '__main__':
	client = get_twitter_client()

	# #prints out the x number of tweets at top of timeline
	# for status in Cursor(client.home_timeline).items(100):

	# 	#process single status
	# 	print(status.text)

	#with open('home_timeline.json', 'w') as f: saves a json file, the jsonl files puts each status on one line
	#jsonl file allows file to be split, easier to process one line at a time

	#limits to 800 from our own timeline, 3200 from a specific user timeline
	with open('home_timeline.jsonl', 'w') as f:
		for page in Cursor(client.home_timeline, count=200).pages(4):
			for status in page:
				f.write(json.dumps(status._json)+"\n")