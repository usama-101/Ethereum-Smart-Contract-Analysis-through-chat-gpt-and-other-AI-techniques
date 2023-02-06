import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.sentiment import SentimentIntensityAnalyzer
import csv

# Load the data from the CSV file
data = pd.read_csv('C:/Users/39349/Desktop/combined.csv',encoding='latin-1', on_bad_lines='skip', engine='python')
data = data.dropna()
text = data['Responses']


# Replace 'text' with the correct column name
text = data.iloc[:,1].values.tolist()
ref = data.iloc[:,0].values.tolist()



# Perform topic modeling using Latent Dirichlet Allocation
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
doc_term_matrix = vectorizer.fit_transform(text)
lda = LatentDirichletAllocation(n_components=10, random_state=42)
lda.fit(doc_term_matrix)

# Extract the topics and their corresponding weights
topics = lda.components_
topic_weights = lda.transform(doc_term_matrix)

# Perform sentiment analysis using the NLTK library
sia = SentimentIntensityAnalyzer()
sentiments = []
for doc in text:
    sentiments.append(sia.polarity_scores(doc))

# Write the topics and sentiments to a CSV file
with open('topics_sentiments4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Reference", "Topic", "Words", "Sentiments"])
    for i, topic in enumerate(topics):
        for index, weight in enumerate(topic):
            writer.writerow([ref[i], i, vectorizer.get_feature_names_out()[index], weight])
    for i, sentiment in enumerate(sentiments):
        writer.writerow([ref[i], "Sentiment", sentiment])