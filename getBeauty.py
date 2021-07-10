import sys
import io
import random

import requests as rs
from bs4 import BeautifulSoup

from datetime import datetime
import pytz

import crawlFunc as func
import sendNotify as line

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


def switch(var):
    return statment.get(var,'')


ptt = 'https://www.ptt.cc'
beauty = '/bbs/Beauty'

crawl = func.Crawl()
page = crawl.get_page(ptt+beauty)
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


draw = random.randrange(len(article_urls))
article_detail = article_urls[draw]
detail_page = crawl.get_page(article_detail)
images = crawl.soup_page(detail_page).select("#main-content>a")

image_list = []
for item in images:
    image_list.append(item.text)


notify = line.LineNotify()

#edge
token = ''

#default message
message = '\n你今天表特了嗎？\n'+article_detail

tz_Taipei = pytz.timezone('Asia/Taipei') 
now = datetime.now(tz_Taipei).strftime("%H")

statment = {
    '07': '早安！該起床囉！',
    '09': '有沒有認真工作啊！',
    '11': '加油！快吃午餐了！',
    '13': '起床囉！認真工作！',
    '15': '今天下午茶吃什麼呢？',
    '17': '下班囉！',
    '19': '晚餐吃了嗎？還沒吃可以先運動！',
    '21': '追劇時間',
    '23': '準備洗洗睡！晚安！',
    '01': '還不快睡覺'
}

if switch(now) != '':
    message = switch(now)+message
    result = notify.lineNotifyMessage(token, message, image_list[0])