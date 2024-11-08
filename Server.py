from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 설정

@app.route('/api/news', methods=['GET'])
def get_news():
    try:
        # 뉴스 데이터 (올바른 JSON 형식)
        news = [
            {"title": "Global Stocks Rally", "link": "https://example.com/news1", "source": "Investing.com"},
            {"title": "US Inflation Hits 40-Year High", "link": "https://example.com/news2", "source": "TradingView"},
            {"title": "Bitcoin Prices Surge", "link": "https://example.com/news3", "source": "CoinDesk"},
        ]
        return jsonify(news), 200  # JSON 데이터와 HTTP 200 응답
    except Exception as e:
        print(f"Error in get_news: {e}")  # 터미널에 에러 출력
        return jsonify({"error": "Internal Server Error"}), 500  # 에러 응답

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
