# Gripen
This is the demonstator software for the Gripen project. The goal is to measure acceleration data and tempurature from bluetooth connected devices. The software shall work "out of box" with basic computer knowlage. Features can be set only by editing a text file (see __Features__). 

# Limitations
The system is not a real time system. Therefore, depending on the computer performance, there may be some time difference between the "live" plot and the actual event. Tests shows good performance on PC but poor performance on Raspberry Pi. When using Raspberry Pi, the recommendation is to set __plot__ to *false*. 

To give similar system performace regardless of number of BLE devices or feature settings, the system uses paralell processing. This works well up to to a certain number of BLE units.

The SW does not cover all possible situations. It is best to restart all programs and BLE's between runs. 

# Prerequisits
 - PC with linux OS
 - Raspberry Pi with latest Raspbian OS
 - Python 3.x
 - Julia 1.6.x

# How to get started (PC)
 1. Download this repository to your __gripen__ folder
 2. Turn on the BLE and type ```sudo hcitool lescan``` in the terminal
 3. In the output, locate your device and copy the address. 
 4. Copy the *unit1.json* file to *unit<x>.json* ```cp unit1.json unit<x>.json```.
 5. Open *<myunit>.json* and edit the features
 6. Copy the *run_unit1.sh* file to *run_unit<x>.sh* ```cp run_unit1.sh run_unit<x>.sh```
 7. Turn off the BLE device.
 8. Run run_unit<x>.sh ```./run_unit<x>.sh```
 9. Turn of the BLE device.
 10. Check the ```data``` folder for new files.
 11. Open a new terminal and type ```./web.jl```
 12. Open your web browser and paste ```http://0.0.0.0:8050/``` in the address field
 13. Update the BLE data in the web interface using F5
 14. When done, kill run_unit<x>.sh using __CTRL-C__ and run ```./killprograms```.

# Features
 This is a description of the features in the json file
 Key | Value | Description
 --- | --- | ---
  __BleAddr__ | String |The bluetooth address of the unit
  __Calibration__ | List | Calibration constants for accelerometer data
  __WriteSleep__ | Float | Not used
  __WriteSize__ | Int | Not used
  __BlePackageSize__ | Int | The number of readings in each package
  __Packages__ | Int | The number of packages to save.
  __DataLen__ | Int | The number of datapoints one grab.
  __SaveToFile__ | Bool | Set *true* to save raw data.
  __Upload__ | Bool | Not implemented
  __Plot__ | Bool | Set *true* to show the live plot.
  __Filename__ | String | The name of the saved data file.
  __BlePipe__ | String | The name of the named pipe to the bluetooth
 __SavePipe__ | String | The name of the save fifo.
  __PlotPipe__ | String | The name of the plot fifo.

