#!/usr/local/bin/python2.7
# coding: utf-8
import urllib2
import sys
import re
from bs4 import BeautifulSoup

# https://play.google.com/store/apps/details?id=jp.co.rakuten.research&hl=ja

def getRate(url):
  html = urllib2.urlopen(url)
  # html = urllib2.urlopen("https://play.google.com/store/apps/details?id=jp.co.rakuten.research&hl=ja")
  soup = BeautifulSoup(html, 'lxml')
  
  # container = soup.find(class_="pf5lIe")
  # label = container.div['aria-label']
  # start = re.match(u"平均評価: 星 ", label).end()
  # end = re.search(u'/5', label).start()
  # rate = label[start:end]

  # <meta itemprop="ratingValue" content="3.9394569396972656">
  rate = soup.find(attrs={"itemprop": "ratingValue"})['content']
  return round(float(rate), 1)

if __name__ == "__main__":
  for arg in sys.argv:
    if arg != __file__:
      print(arg)
      print(getRate(arg))
