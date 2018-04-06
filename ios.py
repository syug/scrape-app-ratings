#!/usr/local/bin/python2.7
# coding: utf-8
import urllib2
import sys
from bs4 import BeautifulSoup
import emoji

def getRate(url):
  html = urllib2.urlopen(url)
  soup = BeautifulSoup(html, 'lxml')
  rate = soup.find(class_="we-customer-ratings__averages__display").string
  rateNum = int(round(float(rate)))
  stars = []
  for i in range(rateNum):
    stars.append(':star:')
  thumsup = ':sparkles: :thumbs_up: :sparkles:' if (rateNum >= 4) else ''
  return emoji.emojize('Your rating is: ' + ' '.join(stars) + ' (' + rate + ') ' + thumsup, use_aliases=True)

if __name__ == "__main__":
  for arg in sys.argv:
    if arg != __file__:
      print('URL: ' + arg)
      print(getRate(arg))
