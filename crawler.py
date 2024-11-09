import requests
from bs4 import BeautifulSoup

def fetch_daum_rss():
    rss_url = "https://media.daum.net/rss/entire/economic.xml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Safari/537.36"
    }
    response = requests.get(rss_url, headers=headers)

    # 응답 상태 코드 확인
    if response.status_code != 200:
        print(f"Failed to fetch RSS: {response.status_code}")
        return []

    # BeautifulSoup로 XML 파싱
    soup = BeautifulSoup(response.content, "xml")  # xml 파서 사용

    # XML 구조 확인
    print(soup.prettify())

    articles = []
    for item in soup.find_all("item"):
        title = item.title.text if item.title else "No Title"
        link = item.link.text if item.link else "No Link"
        description = item.description.text if item.description else "No Description"
        articles.append({"title": title, "link": link, "description": description})

    return articles

if __name__ == "__main__":
    # RSS 데이터 가져오기
    news = fetch_daum_rss()
    for article in news:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Description: {article['description']}")
        print("-" * 80)