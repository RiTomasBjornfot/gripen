#!/usr/bin/python3
import matplotlib.pyplot as plt
import json, sys
import numpy as np
import time

def to_int16(x):
  return [int(x[i+1]+x[i], 16) for i in range(0,len(x),2)]

if __name__ == '__main__':
  with open(sys.argv[1], "r") as fp:
    settings = json.load(fp)
  
  x = np.array([i for i in range(10)])
  y = [np.empty(10), np.empty(10)]
  p = [plt.subplot(211), plt.subplot(212)]
  [_p.grid() for _p in p]

  #for i in range(settings["BlePackageSize"]):
  while True:
    with open(settings["PlotPipe"], "r") as fp:
      try:
        data = [float(x) for x in fp.read().split(' ')]
        #print(data)
        for i in range(2):
          y[i][:-1] = y[i][1:]
          y[i][-1] = data[-2+i]
          p[i].lines = []
          p[i].set_ylim(min(y[i]) - 1, max(y[i]) + 1)
          p[i].plot(x, y[i], '.-', color='C0')
        print(time.time())
        plt.pause(1e-9)
      except Exception as e:
        print(e)
    
