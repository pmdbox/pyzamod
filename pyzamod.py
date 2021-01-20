import time
from station import *

TestStation = StationTCP()
TestStation.SetConnParams('192.168.102.167')
TestStation.addZabbixReceiver('192.168.100.17')
TestStation.addDevice(DIRISA40NEW,'KVP10',1)

TestStation2 = StationRTU()
TestStation2.SetConnParams('COM6','rtu',38400)
TestStation2.addZabbixReceiver('192.168.100.17')
TestStation2.addDevice(DIRISA30HOMETEST,'KVH5',5)

readCounter = 0
while True:
	TestStation.run()
	TestStation2.run()
	readCounter = readCounter + 1 
	print('Read count:',readCounter, flush=True)
	time.sleep(1.0)
