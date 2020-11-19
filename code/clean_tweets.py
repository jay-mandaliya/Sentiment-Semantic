import json

print("Opening file tweets.json")

#importing file with uncleaned tweets
with open('../data/tweets.json') as f:
	info = json.load(f)

print("Cleaning data in progress...")

data = {}
data['tweets'] = []

for tweet in info['tweets']:
	#removing RT from every tweet. Everything else is clean
	str = tweet['tweet'].replace('RT', '')
	
	data['tweets'].append({'tweet': str})

#writing data to new json file
with open('../data/clean_data.json','w') as f:
	json.dump(data,f)

print("Cleaning completed.")
