#!/usr/bin/python3
import pexpect, time, json, sys
import numpy as np

class BleSensor:
    def __init__(self, addr, pname, sleep, count):
        self.addr = addr
        self.pname = pname
        self.sleep = sleep
        self.count = count

    def write_to_pipe(self):
      """
      Get data from a Bluetooth device
      """
      # init
      gatt = pexpect.spawn("gatttool -b " + self.addr + " -I")
      # init log
      logger = open("."+self.pname+".log", "a")
      logger.write(time.ctime()+'\n')
      # connect
      gatt.sendline("connect")
      gatt.expect("Connection successful")
      logger.write(gatt.after.decode()+'\n')
      # set mtu
      gatt.sendline("mtu 240")
      gatt.expect("MTU was exchanged successfully: 236")
      logger.write(gatt.after.decode()+' \n')

      # turn on notifications
      # remove?
      """
      gatt.sendline("char-write-req 0x28 0100")
      gatt.expect("Characteristic value was written successfully")
      """

      # writing ble data to pipe
      gatt.sendline("char-write-cmd 1E 53")
      t0 = time.time()
      for i in range(self.count):
        logger.write(str(i)+'\n')
        time.sleep(self.sleep)
        gatt.expect("\r\n")
        x = gatt.before.decode()[82:]
        t = np.round(time.time() - t0, 2)
        with open(self.pname, "w") as fp:
          fp.write(str(t)+" "+x+" \n")
      # stopping the notification
      gatt.sendline("char-write-cmd 1E 5A")
      # disconnecting and closing
      gatt.sendline("disconnect")
      gatt.close()
      logger.close()

if __name__ == '__main__':
  with open(sys.argv[1], "r") as fp:
    settings = json.load(fp)
  
  #ble = BleSensor("80:6F:B0:ED:38:98", "ppipe", 0.1, 20)
  ble = BleSensor(
      settings["BleAddr"],
      settings["BlePipe"], 
      settings["WriteSleep"], 
      settings["WriteSize"]
    )
  ble.write_to_pipe()
  
