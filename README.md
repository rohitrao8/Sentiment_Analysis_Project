# Social Media Sentiment Analysis Pipeline

## Overview
This project performs sentiment analysis on Twitter data using Natural Language Processing and Machine Learning.

## Technologies Used
- Python
- Pandas
- NLTK
- Scikit-learn
- Tweepy (optional for live data)

## Dataset
- twitter_training.csv
- twitter_validation.csv

## Pipeline Steps
1. Data collection (CSV / Tweepy)
2. Text preprocessing (cleaning, tokenization, stopword removal, stemming)
3. Feature extraction using Bag of Words
4. Model training using Naive Bayes
5. Model evaluation using accuracy and confusion matrix

## Results
- Model Accuracy: **78%**
- Evaluated using confusion matrix and classification report

## Sample Prediction
"I love this game" → Positive  
"This update is terrible" → Negative

## Conclusion
Naive Bayes performs well for baseline sentiment analysis and can be improved using TF-IDF or deep learning models.
