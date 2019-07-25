#!/usr/local/bin/python2.7
# coding: utf-8
import urllib2
import sys
import re
import json
from bs4 import BeautifulSoup
import emoji

def getRatingValue(url):
  html = urllib2.urlopen(url)
  soup = BeautifulSoup(html, 'lxml')
  
  jsonldString = soup.find(name="script", attrs={"type": "application/ld+json"})
  jsonld = json.loads(jsonldString.get_text())
  rateRaw = jsonld['aggregateRating']['ratingValue']
  return float(rateRaw)

def getResultMessage(ratingValue):
  rate = str(round(float(ratingValue), 1))
  rateNum = int(round(float(ratingValue)))
  stars = []
  for i in range(rateNum):
    stars.append(':star:')
  thumsup = ':sparkles: :thumbs_up: :sparkles:' if (rateNum >= 4) else ''
  return emoji.emojize('Your rating is: ' + ' '.join(stars) + ' (' + rate + ') ' + thumsup, use_aliases=True)
  # return round(float(rate), 1)

if __name__ == "__main__":
  for arg in sys.argv:
    if arg != __file__:
      print('URL: ' + arg)
      ratingValue = getRatingValue(arg)
      message = getResultMessage(ratingValue=ratingValue)
      print(message)
