#!/usr/bin/python3
import sys, json
import numpy as np
import os

# read settings
with open(sys.argv[1], 'r') as fp:
  settings = json.load(fp)

# remvoving the named pipe            
try:        
  print("Removing the old pipe")
  os.remove(settings["SavePipe"])    
except FileNotFoundError as e:            
  print(e)        
        
# creating a new named pipe            
try:
  print("Creating a new pipe")
  os.mkfifo(settings["SavePipe"])     
except FileExistsError as e:        
  print(e)

# getting the data
data = []
for ii in range(settings["Packages"]):
  for i in range(settings["BlePackageSize"]):
    with open(settings['SavePipe'], 'r') as sp:
      data.append(sp.read())
    #print(i)
  if settings['SaveToFile']:
    print("Save data to file: "+settings['FileName']+"_"+str(ii))
    with open('data/'+settings['FileName']+"_"+str(ii), "w") as fp:
      [fp.write(d) for d in data]
  data.clear()

"""
data = []
for ii in range(settings["Packages"]):
  for i in range(settings["BlePackageSize"]):
    with open(settings['SavePipe'], 'r') as sp:
      data.append(sp.read().split(' '))
    #print(i)
  z = [[float(x) for x in d] for d in data]
  data.clear()

  if settings['SaveToFile']:
    print("Save data to file: "+settings['FileName'])
    np.savetxt('data/'+settings['FileName']+"_"+str(ii), np.array(z), fmt='%.2f')
    if settings['Upload']:
      print("Uploading to server")
"""
