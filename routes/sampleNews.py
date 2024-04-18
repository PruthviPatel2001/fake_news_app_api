from flask import Blueprint, jsonify, request
import random
import pandas as pd

sample_news_bp = Blueprint('sample_news_bp', __name__)

sample_news_df = pd.read_csv('/Users/pruthvipatel/Documents/projects/FakeNewsApp_API/sampleData/news_sample.csv')

@sample_news_bp.route('/get-sample-news', methods=['GET'])
def get_sample_news():
  
    random_index = random.randint(0, len(sample_news_df) - 1)
    
    
    random_row = sample_news_df.iloc[random_index]
    
    
    content = random_row['author'] + ": " + random_row['title'] + " - " + random_row['text']
    
  
    return jsonify({'content': content})
