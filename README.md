## Social Media Sentiment Analysis Pipeline

### Overview
This project collects Twitter data using Twitter API v2 and performs sentiment analysis
using NLP techniques and a Naive Bayes classifier.

### Technologies
Python, Tweepy, NLTK, Pandas, Scikit-learn

### Workflow
1. Data collection using Tweepy Client (API v2)
2. Text preprocessing (cleaning, tokenization, stopword removal, stemming)
3. Sentiment labeling and model training
4. Model evaluation using accuracy and confusion matrix

### Challenges
Twitter API access limitations were handled by migrating to API v2.

### Results
Achieved ~70–80% accuracy on test data.
