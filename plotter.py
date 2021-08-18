#!/usr/bin/python3
import matplotlib.pyplot as plt
import json, sys, os
import numpy as np

with open(sys.argv[1], "r") as fp:
  settings = json.load(fp)

x = np.array([0, 1, 2])
y = np.empty((5, 3))
ax = plt.subplot(111)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["x", "y", "z"])
                                 
# remvoving the old named pipe    
try:    
  print("Removing the old pipe")
  os.remove(settings["PlotPipe"])    
except FileNotFoundError as e:    
  print(e)    
# creating a new named pipe    
try:    
  print("Creating a new pipe")
  os.mkfifo(settings["PlotPipe"])           
except FileExistsError as e:    
  print(e)

cal = settings["Calibration"]
for i in range(int(1e9)):
  with open(settings["PlotPipe"], "r") as fp:
    try:
      y = np.array([float(y) for y in fp.read().split(' ')])
      y = y*4.3/pow(2, 12)
      y -= cal
      y *= 1/6.5e-3
      pbar = ax.bar(x, y, color='C0')
      plt.pause(1e-9)
      pbar.remove()
    except Exception as e:
      print(e)

