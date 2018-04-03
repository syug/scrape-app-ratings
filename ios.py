#!/usr/local/bin/python2.7
# coding: utf-8
import urllib2
import sys
from bs4 import BeautifulSoup

# https://itunes.apple.com/jp/app/楽天市場/id419267350?mt=8
# https://itunes.apple.com/jp/app/rakuten-music-楽天ミュージック/id1073815664?mt=8
# https://itunes.apple.com/jp/app/楽天ブログ/id385897920?mt=8

def getRate(url):
  html = urllib2.urlopen(url)
  # html = urllib2.urlopen("https://itunes.apple.com/jp/app/%E6%A5%BD%E5%A4%A9%E5%B8%82%E5%A0%B4/id419267350?mt=8")
  soup = BeautifulSoup(html, 'lxml')
  rate = soup.find(class_="we-customer-ratings__averages__display").string
  return rate

if __name__ == "__main__":
  for arg in sys.argv:
    if arg != __file__:
      print(arg)
      print(getRate(arg))
