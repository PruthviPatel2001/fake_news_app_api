from flask import Flask
from flask_cors import CORS
from routes.sampleNews import sample_news_bp
from routes.validateNews import validate_news_bp


app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

@app.route('/')
def welcome():
    return 'Welcome to the Fake News Identifier API!'

app.register_blueprint(sample_news_bp)
app.register_blueprint(validate_news_bp)


if __name__ == '__main__':
    app.run(debug=True)
