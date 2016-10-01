#!/usr/bin/python

from bluepy.btle import Scanner, DefaultDelegate
import time
import binascii
import csv
import os

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        for (adtype, desc, value) in dev.getScanData():
            if len(value) % 2 == 0:
                ba = bytearray(binascii.unhexlify(value))
                if ba[0] == 0x4C:
                    rh = 125 * (ba[22] * 256) / 65536 -6
                    temp = 175.72 * (ba[23] * 256) / 65536 - 46.85
                    t = time.localtime()
                    timeStr = time.strftime("%a, %d %b %Y %H:%M:%S", t)
                    outStr = '{0}, {1}, {2}, {3}, {4}'.format(dev.addr, timeStr, time.mktime(t), rh, temp)
                    with open('temp_data.csv', 'a') as csvfile:
                        csvfile.write(outStr)
                        csvfile.write('\n')

os.chdir('/home/pi/projects/ble_beacon')

while True:
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(100)

for dev in devices:
    print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    for (adtype, desc, value) in dev.getScanData():
        print "  %s = %s" % (desc, value)
   
