# Gripen
A demonstrator

# Prerequisits
 - Linux
 - Python 3.x
 - BlueZ

# How to get started
 1. Download this repository to your __gripen__ folder
 2. Turn on the BLE and type ```sudo hcitool lescan``` in the terminal
 3. In the output, locate your device and copy the address. 
 4. Copy the *tyresensor.json* file to *newdevice.json*.
 5. Open *newdevice.json* and paste the ble address as __BleAddr__ value.
 6. Set a name for your named pipe as __BlePipe__ value.
 7. Create the named pipe ```mkfifo <name>```
 8. As above, set a name for your named pipe as __SavePipe__ value.
 9. Create the named pipe ```mkfifo <name>```

# A simple test
 1. Set __Upload__ to __false__ and __SaveToFile__ to __true__.
 2. Set __Packages__ to 1. 
 3. Set __WriteSize__ and __BlePackageSize__ to __5__.
 4. Open a terminal and type: ```./pygatt.py newdevice.json```
 5. Open a new terminal and type: ```./reader.py newdevice.json```
 6. Check the *.<__BlePipe__>.log* contains expected result
 7. Check that file and *<__BlePipe__>_<unixtime>.txt* contains data
 8. Check web page
