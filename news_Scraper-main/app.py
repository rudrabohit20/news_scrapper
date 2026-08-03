from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import os  # Added import for os module

app = Flask(__name__)

def scrape_news():
    url = "https://www.bbc.com/news"  # Target URL for scraping
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extract headlines (adjust based on target site's HTML structure)
    headlines = soup.find_all('h2')  # Modify selector as per the site
    news_data = []
    for headline in headlines:
        text = headline.get_text().strip()
        link = "https://www.bbc.com"  # Fixed to BBC homepage as per your request
        news_data.append({'text': text, 'url': link})
    return news_data

@app.route('/')
def index():
    news_data = scrape_news()
    return render_template('index.html', news_data=news_data)

@app.route('/headlines')
def headlines():
    news_data = scrape_news()
    return jsonify({'headlines': [{'text': item['text'], 'url': item['url']} for item in news_data]})

@app.route('/favicon.ico')
def favicon():
    try:
        return app.send_static_file('favicon.ico')
    except Exception as e:
        print(f"Error loading favicon: {e}")
        return '', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))  # Use Render's port