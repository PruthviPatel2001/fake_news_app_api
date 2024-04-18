from flask import Flask, request, jsonify
import joblib
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Remove stop words
    tokens = [word for word in tokens if word not in stop_words]
    # Stem each word
    tokens = [stemmer.stem(word) for word in tokens]
    # Join the tokens back into a single string
    processed_text = ' '.join(tokens)
    return processed_text

