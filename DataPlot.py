# -*- coding: utf-8 -*-
#
# Author: Synrey Yee
#
# Created at: 12/20/2016
#
# Description: curve fitting
#
# Last Modified at: 01/04/2018, by: Synrey Yee

from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np

import cPickle
import argparse


def BuildPlot(years, city_alias, city_name = None, degree = 7):
  raw_list = None
  x = []
  y = []
  i = 1
  year_num = len(years)

  for year in years:
  	with open('data/Data_' + year + '_' + city_alias, 'rb') as ipt:
  		raw_list = cPickle.load(ipt)

  	for pair in raw_list:
  		x.append(i)
  		y.append(int(pair[1]))
  		i += 1

  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.plot(x, y, label = 'raw data', color = 'm', linestyle = '', marker = '.')

  degree = min((7 * year_num), 13)
  c = np.polyfit(x, y, degree)
  # 2000 points per year
  x_new = np.linspace(0, i, (2000 * year_num))
  f_liner = np.polyval(c, x_new)
  ax.plot(x_new, f_liner, label = 'curve fitting', color = 'g', linestyle = '-', linewidth = 2, marker = '')

  # degree = 1, for linear fit
  slope = np.polyfit(x, y, 1)
  # 2000 points per year
  sx = np.linspace(0, i, (2000 * year_num))
  sy = f_liner = np.polyval(slope, sx)
  ax.plot(sx, sy, label = 'trend', color = 'r', linestyle = ':', linewidth = 5, marker = '')

  # x-axis ranges within [0, 366 * #year]
  ax.set_xlim(0, (366 * year_num))
  ax.set_xlabel('days')
  ax.set_ylabel('AQI')

  title = ""
  if len(years) > 1:
    title = years[0] + '~' + years[-1] + ' AQI-'
  else:
    title = years[0] + ' AQI-'
  if city_name:
    title += city_name
  else:
    title += city_alias

  ax.set_title(title, bbox = {'facecolor' : '0.8', 'pad' : 5})
  ax.legend()
  plt.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--city_name",
    type = str,
    default = "Beijing",
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
  BuildPlot(args.years, args.city_alias, args.city_name)