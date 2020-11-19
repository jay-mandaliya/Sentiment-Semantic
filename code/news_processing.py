import json
import csv
import math

print("importing required file for importing data")
# importing the clean data obtained by running the script news_cleaning.py
with open('../data/news_data.json') as f:
	info = json.load(f)

# n is the total number of articles
n = len(info['news'])

# following are the keywords which are needed to be search among all articles
search = {}
search['canada'] = 0
search['university'] = 0
search['dalhousie university'] = 0
search['halifax'] = 0
search['business'] = 0

print('searching news articles for specific words...')
for word in search:
	for news in info['news']:
		#check if word is present in the news article
		if word in news['description'].lower():
			search[word] += 1

print('writing data to file table1.csv')
# print the output in the form of table in file table1.csv
with open("../data/table1.csv", "w", newline='', encoding='utf-8') as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(["Total Documents", n])
	csvWriter.writerow(["Search Query", "Document containing term (df)", "Total Documents (N) / number of documents term appeared (df)", "Log (N/df)"])

	csvWriter.writerow(["Canada", search['canada'], float(n) / search['canada'], math.log(float(n) / search['canada'], 10)])
	csvWriter.writerow(["University", search['university'], float(n) / search['university'], math.log(float(n) / search['university'], 10)])
	csvWriter.writerow(["Dalhousie University", search['dalhousie university'], float(n) / search['dalhousie university'], math.log(float(n) / search['dalhousie university'], 10)])
	csvWriter.writerow(["Halifax", search['halifax'], float(n) / search['halifax'], math.log(float(n) / search['halifax'], 10)])
	csvWriter.writerow(["Business", search['business'], float(n) / search['business'], math.log(float(n) / search['business'], 10)])


print('calculating frequency for word canada among all articles')
count = 0
rows = []

max_frequency = 0
freq_index = 0

index = -1

for news in info['news']:
	index += 1

	#check if canada is present in the news article
	if 'canada' in news['description'].lower():

		#calculating total words in article
		total_words = len(news['description'].split())
		#calculating frequency of word canada in article
		freq = news['description'].lower().count('canada')

		count += 1
		rows.append(["Article #" + str(count), total_words, freq])

		rel_freq = float(freq) / total_words
		
		#check if relative frequency is greater than maximum frequency
		if rel_freq > max_frequency:
			max_frequency = rel_freq
			freq_index = index
	

print("\nBelow printed is news article with maximum word frequency:")
print(info['news'][freq_index]['description'])

#writing data to file in form of table
with open("../data/table2.csv", "w", newline='', encoding='utf-8') as dataFile:
	csvWriter = csv.writer(dataFile)

	csvWriter.writerow(["Term", "Canada"])
	csvWriter.writerow(["Canada appeared in " + str(count) + " documents", "Total Words (m)", "Frequency (f)"])
	csvWriter.writerows(rows)
 