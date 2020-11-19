import requests
import json
import re

#following words will be searched in news articles
keywords = ["canada", "university", "dalhousie university", "halifax", "business"]

info = {}
info['news'] = []

print("Fetching news, please wait...")
for keyword in keywords:
	url = ('http://newsapi.org/v2/everything?'
		'q=%s&'
		'apiKey=42ec0d029ebf4ffd8282ff481d8215da&'
		'pageSize=50' % keyword)

	response = requests.get(url)
	response = response.json()

	for article in response['articles']:
		
		#check if description is null or not
		if article['description'] is None:
			str = ""
		else:
			#clean data by removing special chars, urls, and next line character
			str = re.sub(r"http\S+", " ", article['description'])
			str = "".join([char for char in str if (char.isalnum() or char.isspace())])
			str = str.replace('\n', ' ')

		info['news'].append({'title': article['title'], 'description': str, 'content': article['content']})


print('writing data to file')

#writing data to new json file
with open('../data/news_data.json', 'w') as f:
	json.dump(info,f)

print("Done")
