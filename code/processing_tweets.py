import json

print('importing required data files.')

# importing the clean data obtained by running the script clean_tweets.py
with open('../data/clean_data.json') as f:
	info = json.load(f)


#importing positive words from positive-words.txt
with open('../data/positive-words.txt','r') as f:
	positiveWords = f.readlines()
#removing the \n character from every word
positiveWords = [temp.strip() for temp in positiveWords]


#importing negative words from negative-words.txt
with open('../data/negative-words.txt','r') as f:
	negativeWords = f.readlines()
#removing the \n character from every word
negativeWords = [temp.strip() for temp in negativeWords]


print('performing analysis on tweets, please wait...')

counter = 0
rows = []

for tweet in info['tweets']:
	uniqueWords = []
	bow = {}
	
	#spliting whole sentence to list of words
	listOfWords = tweet['tweet'].encode('utf-8').strip().split()

	#generating bag of words
	for word in listOfWords:
		if word not in uniqueWords:
			bow[word] = 1
			uniqueWords.append(word)
		else:
			bow[word] += 1
	

	row = {}

	counter += 1
	row['tweet'] = counter
	
	row['message'] = tweet['tweet']

	positiveCount = 0
	negativeCount = 0

	matchWords = []

	#comparing every word with available positive and negative words
	for key in bow:
		if str(key) in positiveWords:
			positiveCount += bow[key]
			matchWords.append(str(key))

		if str(key) in negativeWords:
			negativeCount += bow[key]
			matchWords.append(str(key))

	row['match'] = ','.join(matchWords)

	#calculating polarity on basis of positive and negative counts
	if positiveCount > negativeCount:
		row['polarity'] = 'positive'
	elif negativeCount > positiveCount:
		row['polarity'] = 'negative'
	else:
		row['polarity'] = 'neutral'

	rows.append(row)

print('writing data to file.')

#writing data to new json file
with open('../data/sentiment_data.json','w') as f:
  json.dump(rows,f)

print('process completed.')

# ref for positive and negative words
# https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html