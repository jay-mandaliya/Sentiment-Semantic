# Sentiment-Semantic

### Project Definition
-----
This	project	covers concepts	related	to	data	analysis.	The	primary objective	of	this project is to	use	concepts	and	tools	related	to	Semantic	Analysis and Sentiment	Analysis.

### Sentiment Analysis
-----
* I have used the json file from the assignment 3 as the data source. The file name is tweets.json.

* The tweets.json file already has the cleaned data but it is required for this project to remove the “RT” from beginning of the tweet. Hence I have developed the script clean_tweets.py which removes extra RT from the previous data and the new data is stored under clean_data.json.

* From the clean tweets, I have developed script processing_tweets.py which creates bag-ofwords for every tweet. Every bag-of-words has their unique words with their counts of appearance in the whole text.

* After researching about the positive and negative words, I found a website https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html which has the list of positive and negative words in the text file. This would be our source of words which should be compared to the text in the tweets.

* I have created the logic for comparing the words and deciding it if it is a positive word or a negative word. After counting total positive and negative words we can decide the polarity of the tweet, that rather it is a positive mood tweet or a negative mood tweet. I have created the json file sentiment_data.json which has the information related to tweet number, tweet text, tweet word match for a positive or negative word and the polarity of the tweet.

* Fir this step I have installed tableau from the official website. After that I have imported the file sentiment_data.json into tableau worksheet and analysed the positive and negative tweets. I have provided the matched words as input for the analysis. After that I have created the word cloud which has polarity positive. Hence, we would get words with maximum frequency among positive tweets.

* Below is the snapshot of most appearing words in positive tweets
![alt text](/images/positive.png)

* Below is the snapshot of the most appearing words in the negative tweets
![alt text](/images/negative.png)

* The most appearing negative words here is right and fault. Other most frequent words are sad, poor, slower, infection and the virus.

### Semantic Analysis
-----
* I have recollected the news articles using the News API using script news_cleaning,py. The data was than cleaned by removing special characters, URL’s, and the next line characters. The cleaned data is stored inside file news_data.json.

* Rather than crating separate documents for every news article, I have created the array of news articles and stored inside the json file news_data.json.

* I have removed the meta-data from the news articles and had only stored the columns “title”, “description” and “content”

* For the term frequency-inverse document frequency, I have searched for words “Canada”, “University”, “Dalhousie University”, “Halifax” and “Business”. I have created the script news_processing.py which searches for the above-mentioned words among all the articles and had created the report table as mentioned below:
![alt text](/images/numbers.png)

* The next task was to search for the word “Canada” among all the news documents and find the frequency of word “Canada” in each article. Also, it was required to find the total number of words in the article with the word frequency. I have developed the logic for the above problem in news_processing.py and had created the file table2.csv. Below is the snapshot of the table:
![alt text](/images/frequency.png)

* At last it was required to display the article with the highest relative frequency with the help of formula f/m. The logic for this problem is also derived in news_processing.py and the snapshot of the output is as below:
![alt text](/images/final.png)

### References
-----
 “Tableau Public: Free Data Visualization Software”. Available: https://public.tableau.com/en-us/s/.
