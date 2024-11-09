from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

def scrape_naver_economy_news():
    url = "https://news.naver.com/section/101"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    news_items = soup.select(".type06_headline li")  # CSS Selector

    for item in news_items:
        try:
            title = item.select_one("a").get_text(strip=True)  # 뉴스 제목
            link = item.select_one("a")["href"]  # 뉴스 링크
            summary = item.select_one(".lede").get_text(strip=True) if item.select_one(".lede") else "No summary available"
            
            articles.append({
                "title": title,
                "link": link,
                "summary": summary,
            })
        except Exception as e:
            print(f"Error parsing news item: {e}")
            continue

    return articles

@app.route('/api/news', methods=['GET'])
def get_news():
    try:
        news = scrape_naver_economy_news()
        return jsonify(news), 200
    except Exception as e:
        print(f"Error in get_news: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
