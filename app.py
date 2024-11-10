from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from bs4 import BeautifulSoup
import requests
from collections import Counter
import re

app = Flask(__name__)
CORS(app) 
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=5000)
def fetch_page_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def get_most_frequent_words(words, n=10):
    counter = Counter(words)
    return counter.most_common(n)

@app.route('/api/fetch', methods=['POST'])
def analyze_url():
    data = request.json
    url = data.get('url')
    words = fetch_page_text(url)
    frequent_words = get_most_frequent_words(words)
    result = [{'word': word, 'frequency': count} for word, count in frequent_words]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
