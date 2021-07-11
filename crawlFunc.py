import sys
import io
import re

import requests as rs
from bs4 import BeautifulSoup

class Crawl:
    def get_page(self,url):
        r = rs.get(url,cookies = {'over18': '1'})
        if r.status_code != 200 :
            print('error')
            return False
        else:
            return r.text
            
    def soup_page(self,page):
        soup = BeautifulSoup(page,"html5lib")
        return soup

    def check_images(self,images):
        image_list = []
        for item in images:
            pattern = re.compile('.*\.(jpg|gif|png)$')
            if pattern.match(item.text):
                image_list.append(item.text)
        
        if len(image_list) > 0:
            return image_list
        else:
            return False