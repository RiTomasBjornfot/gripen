#!/usr/bin/python3
import json, sys, time, os
import numpy as np

def to_int16(x):
  return [int(x[i+1]+x[i], 16) for i in range(0,len(x),2)]

if __name__ == '__main__':
  
  with open(sys.argv[1], "r") as fp:
    settings = json.load(fp)
  
    # remvoving the old named pipe    
    try:
      print("Removing the old pipe")
      os.remove(settings["BlePipe"])    
    except FileNotFoundError as e:    
      print(e)
    
    # creating a new named pipe    
    try:
      print("Creating the new pipe")
      os.mkfifo(settings["BlePipe"])
    except FileExistsError as e:    
      print(e)
  for i in range(int(1e9)):
    with open(settings["BlePipe"], "r") as fp:
      z = fp.read()
      if len(z.split(' ')) == settings["DataLen"]:
        with open(settings["SavePipe"], "w") as fpp:
          fpp.write(z)
        if settings["Plot"]:
          raw, _str = to_int16(z.split(' ')[1:-2])[:-9], ""
          for j in range(3):
            _mean = np.mean(raw[j::3])
            _str += str(_mean)+" "
            try:
              with open(settings["PlotPipe"], "w") as pp:
                pp.write(_str[:-1])
            except Exception as e:
              print("reader.py:", e)

