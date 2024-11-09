import requests
from bs4 import BeautifulSoup

def fetch_daum_economy_news():
    url = "https://media.daum.net/economic/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # 응답 상태 확인
    if response.status_code != 200:
        print(f"Failed to fetch Daum Economy News: {response.status_code}")
        return []

    # BeautifulSoup로 HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 필요한 부분만 추출
    articles = []
    news_items = soup.select("a.link_txt")  # 제목과 링크가 포함된 태그 선택

    for item in news_items:
        try:
            title = item.get_text(strip=True)  # 뉴스 제목
            link = item["href"]  # 뉴스 링크

            # 링크필터링
            if link.startswith("https://v.daum.net"):
                articles.append({"title": title, "link": link})
        except Exception as e:
            print(f"Error parsing item: {e}")
            continue

    return articles

if __name__ == "__main__":
    news = fetch_daum_economy_news()
    for article in news:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print("-" * 80)
