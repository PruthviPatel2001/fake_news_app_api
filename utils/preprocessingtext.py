import nltk
import re
from nltk.stem import PorterStemmer
import os

stemmer = PorterStemmer()


stopwords_path = os.path.join(os.path.dirname(__file__), '..', 'nltk_data', 'stopwords.txt')

with open(stopwords_path, 'r') as file:
    stop_words = set(file.read().splitlines())

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [stemmer.stem(word) for word in tokens]
    processed_text = ' '.join(tokens)
    return processed_text

