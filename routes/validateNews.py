from flask import Blueprint, jsonify, request
import joblib
from utils.preprocessingtext import preprocess_text
import os

validate_news_bp = Blueprint('validate_news_bp', __name__)

MODEL_DIR = os.path.join(os.getcwd(), 'models')


model_path = os.path.join(MODEL_DIR, 'fakeNewsIdentifier_model.pkl')
model = joblib.load(model_path)


vectorizer_path = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')
vectorizer = joblib.load(vectorizer_path)

@validate_news_bp.route('/validate-news', methods=['POST'])
def validate_news():

    news_article = request.json['article']

    processed_article = preprocess_text(news_article)

    vectorized_article = vectorizer.transform([processed_article])

    prediction = model.predict(vectorized_article)[0]

    prediction_label = 'Fake' if prediction == 1 else 'Real'

    return jsonify({'prediction': prediction_label})
