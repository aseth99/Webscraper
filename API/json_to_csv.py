import json
import csv

#this only works if JSON file is already scraped & saved as user_timeline_[twitterhandle] 

# import re
# import pandas as pd

#code from https://stats.seandolinar.com/collecting-twitter-data-converting-twitter-json-to-csv-ascii/
#and used https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data
 
# data_json = open('user_timeline_WeedFeed.json', mode='r').read() #reads in the JSON file into Python as a string
# data_python = json.loads(data_json) #turns the string into a json Python object

# user = sys.argv[1] #uses first arguement that we enter in command
# client = get_twitter_client()
# fname = "user_timeline_{}.json".format(user)

# with open(fname, 'w') as f:
# for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
# for status in page:
# f.write(json.dumps(status._json)+"\n")

chooseName = input("\nWhat should we name the csv file?\n\n\n")
csvFileName = "{}.csv".format(chooseName)
csv_out = open(csvFileName, mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['Twitter Handle & User Name', 'Tweet', ' external URL', 'Hashtags', 'Date of Tweet', 'Followers', 'Following', 'RT', 'FAV'] #field names
writer.writerow(fields) #writes field

tweets = []
filterArray = ["resilien","adversity","disaster","terrorist"]

exitClause = "notdone"
print("what words do we want to filter by? (already filtering by resilien,adversity,disaster or terrorist)\n\n\n")

while exitClause != "done":
    exitClause = input("(type done if finished)\n\n")
    if exitClause == "done":
    	break
    filterWord = "{}".format(exitClause)
    filterArray.append(filterWord)

if exitClause == "done":
    print("okay... now...")



exitClause = "notdone"
print("(this only works if JSON file is already scraped & saved as user_timeline_[twitterhandle])\n So whose tweets are we outputting to csv?\n\n\n")

while exitClause != "done":
    exitClause = input("(type done if finished)\n\n@")
    if exitClause == "done":
    	break
    jsonFileToBeOpened = "user_timeline_{}.json".format(exitClause)
    for line in open(jsonFileToBeOpened, 'r'):
        tweets.append(json.loads(line))

if exitClause == "done":
    print("converting...")


# for line in open('user_timeline_dutchdailynews.json', 'r'):
#     tweets.append(json.loads(line))

# for line in open('user_timeline_DutchNewsNL.json', 'r'):
#     tweets.append(json.loads(line))

for line in tweets:
 	
    urlvar = line.get('entities').get('urls')
    if(urlvar):
    	urlvar = urlvar[0].get('expanded_url')
    else:
    	urlvar = "no external urls in this tweet"

    hashtagsVar = line.get('entities').get('hashtags')
    tempHashList = []
    if not hashtagsVar:
    	hashtagsVar = "no hashtags in this tweet"
    else:
    	for i in hashtagsVar:
    		tempHashList.append(i['text'])
    	hashtagsVar = tempHashList



    #writes a row and gets the fields from the (now pyton) dict
    #screen_name and followers/friends are found on the second level hence two get methods
    #filters and only puts tweets in csv that have the word "win" in tweets
    
    if any(x in line.get('text') for x in filterArray):

	    writer.writerow([line.get('user').get('screen_name')+" , "+line.get('user').get('name'),
	                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
	                     urlvar,
	                     hashtagsVar,
	                     line.get('created_at'),
	                     line.get('user').get('followers_count'),
	                     line.get('user').get('friends_count'),
	                     line.get('retweet_count'),
	                     line.get('favorite_count')])
	 
csv_out.close()


#line.get('entities').get('urls').get("expanded_url"),
# "entities": 
# {
# 	"hashtags": [], 
# 	"symbols": [], 
# 	"user_mentions": [], 
# 	"urls": 
# 		[{
# 		"url": "https://t.co/v4eTGXIChd", 
# 		"expanded_url": "https://goo.gl/6YkRg2", 
# 		"display_url": "goo.gl/6YkRg2", 
# 		"indices": [46, 69]
# 		}]
# }, 
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