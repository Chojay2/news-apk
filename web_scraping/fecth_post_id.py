
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

news_articles = [
    {"news_category": "Business", "id": 57},
    {"news_category": "Sci/Tech", "id": 60},
    {"news_category": "Education", "id": 62},
    {"news_category": "sports", "id": 58}
]
def get_news_category(id):
    for news_id in news_articles:
        if news_id["id"] == id:
            return news_id["news_category"]

post_ids = []
def get_post_id(url): 
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    post_id = query_params.get('p', [None])[0]
    return post_id

def save_post_id(post_blocks, id):
    for post in post_blocks:
        post_id_tag=post.find("a")
        post_id =post_id_tag.get("href")
        post_id= get_post_id(post_id)
        post_ids.append(post_id + str(id))

for article in news_articles:
    url = "http://www.bbs.bt/news/?cat=" + str(article["id"])
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    post_cards = soup.find_all("div", class_="td-module-thumb")
    save_post_id(post_cards, article["id"])

    post_list = soup.find_all("h3", class_="td-module-title")
    save_post_id(post_list, article["id"])



