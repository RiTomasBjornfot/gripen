#!/usr/bin/python3
import json, sys, time
import numpy as np
def to_int16(x):
  return [int(x[i+1]+x[i], 16) for i in range(0,len(x),2)]

if __name__ == '__main__':
  
  with open(sys.argv[1], "r") as fp:
    settings = json.load(fp)

  rdata = []
  #for i in range(settings["BlePackageSize"]):
  #for i in range(int(1e9)):
  i = 0
  while i < settings["BlePackageSize"]:
    with open(settings["BlePipe"], "r") as fp:
      z = fp.read().split(' ')
      t = float(z[0])
      #print(len(z))
      if len(z) == settings["DataLen"]:
        i += 1
        print(i)
        rdata.append(to_int16(z[1:-2])[:-9])
        # send to plotter
        if settings["Plot"]:
          with open(settings["PlotPipe"], "w") as pp:
            x, y, z = [rdata[-1][i::3] for i in range(3)]
            _str = ""
            for vals in [x, y, z]:
                _mean = np.mean(vals)
                _std = np.std(vals)
                _str += str(_mean)+" "+str(_std)+" "
            #print("time:", t, time.time())
            pp.write(_str[:-1])

  if settings["SaveToFile"]:
    print("Saving data to file")
    sname = settings["SavePipe"]+"_"+str(int(time.time()))
    #np.savetxt('data/'+sname, rdata, fmt="%.3f")
    np.savetxt('data/'+settings['FileName'], np.array(rdata))
  
  if settings["Upload"]:
    print("Uploading data")
    # sad
    
