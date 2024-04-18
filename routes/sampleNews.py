from flask import Blueprint, jsonify
import random
import pandas as pd
import os

sample_news_bp = Blueprint('sample_news_bp', __name__)
SAMPLE_DATA_DIR = os.path.join(os.getcwd(), 'sampleData')

sample_data_path = os.path.join(SAMPLE_DATA_DIR, 'news_sample.csv')

sample_news_df = pd.read_csv(sample_data_path)

@sample_news_bp.route('/get-sample-news', methods=['GET'])
def get_sample_news():
  
    random_index = random.randint(0, len(sample_news_df) - 1)
    
    
    random_row = sample_news_df.iloc[random_index]
    
    
    content = random_row['author'] + ": " + random_row['title'] + " - " + random_row['text']
    
  
    return jsonify({'content': content})
