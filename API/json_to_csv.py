import json
import csv
import re
import pandas as pd

#code from https://stats.seandolinar.com/collecting-twitter-data-converting-twitter-json-to-csv-ascii/
#and used https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data
 
# data_json = open('user_timeline_WeedFeed.json', mode='r').read() #reads in the JSON file into Python as a string
# data_python = json.loads(data_json) #turns the string into a json Python object

csv_out = open('tweets_out_ASCII.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['created_at', 'text', 'screen_name', 'followers', 'friends', 'rt', 'fav'] #field names
writer.writerow(fields) #writes field

tweets = []
for line in open('user_timeline_WeedFeed.json', 'r'):
    tweets.append(json.loads(line))

for line in tweets:
 
    #writes a row and gets the fields from the json object
    #screen_name and followers/friends are found on the second level hence two get methods
    writer.writerow([line.get('created_at'),
                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                     line.get('user').get('screen_name'),
                     line.get('user').get('followers_count'),
                     line.get('user').get('friends_count'),
                     line.get('retweet_count'),
                     line.get('favorite_count')])
 
csv_out.close()



# f = open('home_timeline.json')
# data = json.load(f)
# f.close()

# f = csv.writer(open('userTimelineCSV.csv', 'wb+'))
# # use encode to convert non-ASCII characters
# for item in data:
#     values = [ x.encode('utf8') for x in item['fields'].values() ]
#     f.writerow([item['pk'], item['model']] + values)

# import pandas as pd

# with open('home_timeline.json', 'r') as f:
# 	data = f.readlines()

# data = map(lambda x: x.rstrip(), data)

# data_json_str = "[" + ','.join(data) + "]"

# data_df = pd.read_json(data_json_str)

# data.to_csv('test.csv', encoding='utf-8', index=False)

# # data = pd.read_json('../Desktop/Hammer/Webscraper/API/home_timeline.json', lines=True)
# #  # as f_input:
# #  #    df = pd.read_json(f_input)

# # data.to_csv('weedfeed_timeline.csv', encoding='utf-8', index=False)