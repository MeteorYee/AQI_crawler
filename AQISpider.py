# -*- coding: utf-8 -*-
#
# Author: Synrey Yee
#
# Created at: 12/20/2016
#
# Description: A crawler to capture PM 2.5 data
#
# Last Modified at: 01/04/2018, by: Synrey Yee

from __future__ import print_function

from selenium import webdriver

import re
import time
import cPickle
import argparse


class DataSpider(object):

  # initialization
  def __init__(self, city_url, city_alias, timeout = 30):
    self._driver = webdriver.Chrome()
    self._driver.set_page_load_timeout(timeout)

    self._months = ['-01', '-02', '-03', '-04', '-05', '-06', '-07', '-08', '-09', '-10', '-11', '-12']
    # data list: [(date, AQI), ]
    self._data = []

    self._city_url = city_url
    self._city_alias = city_alias

  # download one page's data for a particular year, accurate to 1 day
  def GetOneYear(self, year):
    for mth in self._months:
      month = year + mth
      url = self._city_url + '&month=' + month
      
      if self._ExtractData(url, month):
        print ("Finish month: %s" % (month))
      else:
        print ("\nLack of month: %s\n" % (month))
      # take a break!
      time.sleep(5)

    self._Save1YearData(year)
    print ('Finish year ' + year)

  # extract one day's AQI data in a month
  def _ExtractData(self, url, month, try_time = 3):
    if try_time < 1:
      return False

    # download the page
    try:
      # r = requests.get(url, headers = self._headers, timeout = 20)
      page = self._driver.get(url)
    except Exception as e:
      print ('Downloading fail!')
      print (e)

      time.sleep(3)
      print("Try again #%d:" % (4 - try_time))

      return self._ExtractData(url, month, (try_time - 1))

    raw = self._driver.page_source

    st = '<td align="center">' + month + '(.*?)</td>.*?<td align="center">(.*?)</td>'
    pattern = re.compile(st, re.S)
    result = re.findall(pattern, raw)

    # make sure that the result is not empty
    if not result:
      print("month %s failed" % month)
      time.sleep(3)
      print("Try again #%d:" % (4 - try_time))

      return self._ExtractData(url, month, (try_time - 1))

    # store in list
    for pair in result:
      self._data.append((month + pair[0], pair[1]))

    return True

  # dump the data
  def _Save1YearData(self, year):
    filename = 'data/Data_' + year + '_' + self._city_alias
    with open(filename, 'wb') as opt:
      cPickle.dump(self._data, opt)

    self._data = []

if __name__ == '__main__':
  '''
  A usage sample:

  city_alias = 'bj'
  years = ['2015', '2016']
  # Beijing's URL
  city_url = 'https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC'
  dspd = DataSpider(city_url, city_alias)
  for year in years:
    dspd.GetOneYear(year)

  '''
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--city_para",
    type = str,
    default = "%E5%8C%97%E4%BA%AC",
    help = "source or target file prefix")

  parser.add_argument(
    "--city_alias",
    type = str,
    default = "bj",
    help = "source or target file prefix")

  parser.add_argument(
    "--years",
    type = str,
    nargs = '*',
    default = ['2017'],
    help = "source or target file prefix")

  args = parser.parse_args()
  # https://www.aqistudy.cn/historydata/monthdata.php?city=%E9%95%BF%E6%B2%BB

  base_url = 'https://www.aqistudy.cn/historydata/daydata.php?city='
  city_url = base_url + args.city_para
  dspd = DataSpider(city_url, args.city_alias)
  for year in args.years:
    dspd.GetOneYear(year)