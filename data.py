#!/usr/bin/env python
# -*- coding: utf8 -*-
import numpy as np

def plot(data, rng, absval = False):
  if rng is not None:
    # otherwise plot all data
    data = data[-rng:]

  # cols: Timestamp   Open    High    Low Close   Volume (BTC)    Volume (Currency)   Weighted Price
  weighted = np.asarray([ l[-1] for l in data ])
  diffs = weighted[1:] - weighted[:-1]
  reldiff = 100. * (diffs / weighted[:-1])
  if absval:
    reldiff = np.abs(reldiff)
  #print 'relative differences:'
  #print [ '%.2f' % _ for _ in reldiff ]

  # moving average
  n = 7
  #weights = np.ones(n) # SMA
  weights = np.exp(np.linspace(-1.0, 0.0, n)) # EMA
  window = weights / weights.sum()
  smooth = np.convolve(reldiff, window, 'same')

  n = 21
  weights = np.exp(np.linspace(-1.0, 0.0, n)) # EMA
  window = weights / weights.sum()
  smooth2 = np.convolve(reldiff, window, 'same')

  import datetime as dt
  today = dt.date.today()
  start = rng if rng is not None else len(weighted)
  xdates = [ today - dt.timedelta(days=i) for i in range(start, 0, -1) ]

  import matplotlib.pyplot as plt
  import matplotlib.dates as mdates

  plt.subplots_adjust(hspace=.05)
  plt.gcf().autofmt_xdate()

  fig = plt.figure(1)
  ax1 = fig.add_subplot(311)
  ax1.grid()
  ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
  ax1.set_yscale('symlog', linthreshy=1)
  ax1.plot(xdates[1:], weighted[1:])

  ax2 = fig.add_subplot(3, 1, 2, sharex=ax1)
  ax2.grid()
  ymax = 20
  ymin = 0 if absval else -ymax
  ax2.set_ylim(ymin, ymax)
  ax2.plot(xdates[1:], reldiff)

  ax3 = fig.add_subplot(3, 1, 3, sharex=ax1)
  ax3.grid()
  ymax = 15
  ymin = 0 if absval else -ymax
  ax3.set_ylim(ymin, ymax)
  ax3.plot(xdates[1:], smooth,  color='red',  alpha = .7)
  ax3.plot(xdates[1:], smooth2, color='blue', alpha = 1)

  # disable x axes
  xticklabels = ax1.get_xticklabels()+ax2.get_xticklabels()
  plt.setp(xticklabels, visible=False)
  plt.setp(ax3.xaxis.get_majorticklabels(), rotation=70)

  #plt.show()
  abs_str = '-abs' if absval else ''

  if rng is not None:
    fn = 'mtgox-last-%d%s.png' % (rng, abs_str)
  else:
    fn = 'mtgox-all%s.png' % abs_str
  fig.savefig(fn, dpi=300)
  plt.clf()

if __name__=="__main__":
  import requests
  req = requests.get("http://bitcoincharts.com/charts/chart.json?m=mtgoxUSD&SubmitButton=Draw&r=&i=Daily&c=0&s=&e=&Prev=&Next=&t=S&b=&a1=&m1=10&a2=&m2=25&x=0&i1=&i2=&i3=&i4=&v=0&cv=0&ps=0&l=0&p=0&")
  data = req.json()
  if data is None:
    print("bitcoincharts rate limit, please wait …")
    exit()
  for absval in [True, False]:
    plot(data, 400,  absval)
    plot(data, None, absval)
