#!/usr/local/bin/python2.7
# coding: utf-8
import urllib2
import sys
import re
from bs4 import BeautifulSoup

def getRate(url):
  html = urllib2.urlopen(url)
  soup = BeautifulSoup(html, 'lxml')
  
  rate = soup.find(attrs={"itemprop": "ratingValue"})['content']
  return round(float(rate), 1)

if __name__ == "__main__":
  for arg in sys.argv:
    if arg != __file__:
      print(arg)
      print(getRate(arg))
