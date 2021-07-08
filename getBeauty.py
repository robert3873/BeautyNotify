import sys
import io
import random

import requests as rs
from bs4 import BeautifulSoup

import crawlFunc as func

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# url = 'https://www.ptt.cc/bbs/Beauty/bbs/Beauty/M.1625639687.A.426.html'
# r = rs.get(url,cookies = {'over18': '1'})
# print(r.status_code)
# print(r.text)

# sys.exit()
ptt = 'https://www.ptt.cc/'
beauty = 'bbs/Beauty'

# r = rs.get(ptt, cookies = {'over18': '1'})
# print(r.text)
crawl = func.Crawl()
page = crawl.get_page(ptt+beauty)

# print(page)
soup = crawl.soup_page(page)
articles = soup.find_all("div", class_="r-ent")

article_urls = []

for article in articles:

    title = article.select_one(".title>a")
    if title:
        title_name = str(title.text)
        title_url = title.get('href')
    
    if '正妹' not in title_name:
        continue
    
    if '肉特' in title_name:
        continue
    
    title_url = ptt+title_url
    article_urls.append(title_url)

print(len(article_urls))
draw = random.randrange(len(article_urls))

print(draw)

article_detail = article_urls[draw]
print(article_detail)

detail_page = crawl.get_page(article_detail)
# print(detail_page)
images = crawl.soup_page(detail_page).select("#main-content>a")

image_list = []
for item in images:
    # print(item.text)
    image_list.append(item.text)

print(image_list)