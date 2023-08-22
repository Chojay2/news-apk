
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from fecth_post_id import post_ids as fecthed_ids, get_news_category

class NewsArticle:
    def __init__(self, title, author, views, publish_date, category, content):
        self.title = title
        self.author = author
        self.views = views
        self.publish_date = publish_date
        self.category = category
        self.content = content

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"views: {self.views}")
        print(f"Publish Date: {self.publish_date}")
        print(f"category: {self.category}")
        print("Content:")
        print(self.content)

for fetched_id in fecthed_ids:
  
  url = "http://www.bbs.bt/news/?p=" + fetched_id[:-2]
  category = get_news_category(int(fetched_id[-2:]))
  parsed_url = urlparse(url)
  query_params = parse_qs(parsed_url.query)
  post_id = query_params.get('p', [None])[0]

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")


  contentBlock = soup.find("div", class_="tdi_89")

  if contentBlock:
      news_content = contentBlock.find_all("p")
      author_name = news_content[len(news_content) - 1].text
      news_content = " ".join(tag.get_text() for tag in news_content)
      

      # Extract and print each image source
      images = contentBlock.find_all("img")
      for image in images:
          print("Image Source:", image["src"])
  else:
      print("Main div not found.")

  def elem(html_tag, html_class):
      return soup.find(html_tag, class_=html_class).text


news_obj = NewsArticle(elem("h1", "tdb-title-text"), author_name, elem('span', 'td-nr-views-' + post_id) , elem('time', 'entry-date'), category, news_content)

if news_obj:
    news_obj.display()
    print(fecthed_ids)
else:
    print("Div not found.")
