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
  
  x = np.array([0, 1, 2])
  y = np.empty((5, 3))
  ax = plt.subplot(111)
  ax.set_xticks([0, 1, 2])
  ax.set_xticklabels(["x", "y", "z"])

  for i in range(int(1e9)):
    with open(settings["PlotPipe"], "r") as fp:
      try:
        data = [float(x) for x in fp.read().split(' ')]
        # mean
        y[i % 5, 0] = data[0]
        y[i % 5, 1] = data[2]
        y[i % 5, 2] = data[4]
        pbar = ax.bar(x, np.mean(y, axis=0), color='C0')
        plt.pause(1e-9)
        pbar.remove()
        print(i, ':', data)
      except Exception as e:
        print(e)
    
