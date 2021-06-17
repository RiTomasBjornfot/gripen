#!/usr/bin/python3
import json, sys, time
import numpy as np
def to_int16(x):
  return [int(x[i+1]+x[i], 16) for i in range(0,len(x),2)]

if __name__ == '__main__':
  
  with open(sys.argv[1], "r") as fp:
    settings = json.load(fp)

  data = []
  for i in range(settings["ReadPackageSize"]):
    with open(settings["BlePipe"], "r") as fp:
      z = fp.read().split(' ')
      t = float(z[0])
      if len(z) == 201:
        data.append(to_int16(z[1:-2]))
        print("time:", t, "data:", data[-1][:10], "...")

  if settings["SendToServer"]:
    print("saving data")
    #sname = str(int(time.time()))
    #np.savetxt('data/'+sname, data, fmt="%.3f")
    #np.savetxt(settings["UploadPipe"], data, fmt="%.3f")
