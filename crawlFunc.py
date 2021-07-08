import sys
import io

import requests as rs
from bs4 import BeautifulSoup

class Crawl:
    def get_page(self,url):
        print(url)
        r = rs.get(url,cookies = {'over18': '1'})
        if r.status_code != 200 :
            print('error')
            return False
        else:
            # print(r.text)
            return r.text
    def soup_page(self,page):
        soup = BeautifulSoup(page,"html5lib")
        return soup