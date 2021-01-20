from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.compat import iteritems
from collections import OrderedDict
from pymodbus.client.sync import ModbusTcpClient
import time
import datetime
from os import system, name 

def clear():
	if (name == 'nt'):
		_ = system('cls')
	else:
		_ = system('clear')


clear()
client = ModbusTcpClient('192.168.0.111')

while(True):
	try:
		client.connect()

		print("\033[0;0H==== Тестові дані з приладу ====\n")

		rr = client.read_holding_registers(0x200, 2, unit=1)
		decoder = BinaryPayloadDecoder.fromRegisters(rr.registers,byteorder=Endian.Big,wordorder=Endian.Big)
		decoded = OrderedDict([('32uint', decoder.decode_32bit_uint()),])
		for valuename, value in iteritems(decoded):
			decodedValue = value
		print ("\033[3;3HЛічильник мотогодин: ",str(datetime.timedelta(seconds=decodedValue)))
		#print ("\033[3;3HЛічильник мотогодин: ",decodedValue/3600)
		
		rr = client.read_holding_registers(0x9007, 2, unit=1)
		decoder = BinaryPayloadDecoder.fromRegisters(rr.registers,byteorder=Endian.Big,wordorder=Endian.Big)
		decoded = OrderedDict([('32uint', decoder.decode_32bit_uint()),])
		for valuename, value in iteritems(decoded):
			decodedValue = value
		print ("\033[4;3HЧастота, Гц: ",decodedValue/1000)
		
		rr = client.read_holding_registers(36867, 2, unit=1)
		decoder = BinaryPayloadDecoder.fromRegisters(rr.registers,byteorder=Endian.Big,wordorder=Endian.Big)
		decoded = OrderedDict([('32uint', decoder.decode_32bit_uint()),])
		for valuename, value in iteritems(decoded):
			decodedValue = value
		print ("\033[5;3HНапруга, В: ",decodedValue/100)
		
		print ("\033[6;3H                    ")
		client.close()
	except:
		print ("\033[6;4HError.              ")

	time.sleep(0.1)