from pymodbus.client.sync import ModbusSerialClient
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.compat import iteritems
from collections import OrderedDict
from pyzabbix import ZabbixMetric, ZabbixSender
from modbustemplates import *
from devicemodels import *
import psycopg2
import time
from time import localtime, strftime, gmtime
from datetime import datetime

class Station:

	def __init__(self):
		self.Devices = []		
		self.modbusTypesLength = {
		    'int': 1,
		    'uint': 1,
		    'dint': 2,
		    'duint': 2,
		    'real': 2,
		    'float': 2,
		    'word': 1,
		    'dword': 2
		}
		self.ZabbixHost = None
		self.ConnectString = None
		self.conn = None

	def addZabbixReceiver(self,ZabbixHostAddress,ZabbixHostPort=10051):
		self.ZabbixHost = ZabbixSender(ZabbixHostAddress,ZabbixHostPort)

	def addDb(self,ip,port,database,login,password):
		self.ConnectString = "postgres://"+login+":"+password+"@"+ip+":"+port+"/"+database

	def addDevice(self,deviceType,deviceName,deviceAddress):
		Device = DeviceTemplate(deviceName,deviceAddress)
		Device.addVariablesList(deviceType)
		self.Devices.append(Device)

	def __sendToZabbix(self,deviceName,metricName,metricValue):
		if hasattr(self,'ZabbixHost'):
			#print(deviceName,metricName,metricValue)
			metrics = []
			metric = ZabbixMetric(deviceName, metricName, metricValue)
			metrics.append(metric)
			result = self.ZabbixHost.send(metrics)

	def __addToDb(self,stationCode,tagName,tagValue):
			self.sql = self.sql + "(" + "'" + stationCode + "'," + "'" + tagName + "'," + "'" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "'," + str(tagValue) + "),"

	def __sendToDb(self):
		# self.sql = "SET TIMEZONE ='Europe/Kiev';INSERT INTO data (location,tagname,datetime,tagvalue) VALUES " + self.sql
		self.sql = "INSERT INTO data (location,tagname,datetime,tagvalue) VALUES " + self.sql
		self.sql = self.sql[:-1]
		self.sql = self.sql + " ON CONFLICT DO NOTHING;"
		# print(self.sql)
		#print("DB connect.")

		if self.conn is None or self.conn.closed:
			try:
				self.conn = psycopg2.connect(self.ConnectString)
				self.cursor = self.conn.cursor()
			except psycopg2.OperationalError:
				self.conn = None
				print("DB connect except.")

		if self.conn is not None and not self.conn.closed:
			try:
				self.cursor.execute(self.sql)
				self.conn.commit()
			except (Exception, psycopg2.Error) as error:
				print(error.pgerror)

		self.sql = ""

	def runCycleInstance(self):
		#self.modbusClient = ModbusTcpClient(self.ipAddress,self.ipPort)
		if self.modbusClient.connect():
			for runnedDevice in self.Devices:
				self.__processVariable(runnedDevice)
			self.modbusClient.close() 

	def __processVariable(self,device):
		self.sql = ""
		lastPoll = 0
		variablesCount = device.getVariablesCount()
		onePollPart = 100/variablesCount
		for i in range(variablesCount):
			try:
				varibaleValue = self.__readVariableFromModbus(device.getModbusAddress(),device.getVariableModbusAddress(i),device.getVariableType(i),device.getByteIndian(i),device.getWordIndian(i),device.getCommand(i))
				device.setVariableValue(i,varibaleValue)
				lastPoll = lastPoll + onePollPart
				self.__addToDb(device.getZabbixName(),device.getVariableName(i),device.getVariableValue(i))
				if self.ZabbixHost != None:
					self.__sendToZabbix(device.getZabbixName(),device.getVariableName(i),device.getVariableValue(i))
				#print(device.getVariableValue(i))
			except:
				print ('Error reading register:',device.getModbusAddress(),device.getVariableName(i))

		self.__addToDb(device.getZabbixName(),'LASTPOLL', lastPoll)
		if self.ZabbixHost != None:
			self.__sendToZabbix(device.getZabbixName(),'LASTPOLL', lastPoll)
		self.__sendToDb()


	def __readVariableFromModbus(self,modbusAddress,modbusVariableAddress,type,byteIndian,wordIndian,useCommand):
		if(byteIndian=='Big'):
			byteorder = Endian.Big
		else:
			byteorder = Endian.Little

		if(wordIndian=='Big'):
			wordorder = Endian.Big
		else:
			wordorder = Endian.Little

		if (useCommand == 3):
			rr = self.modbusClient.read_holding_registers(modbusVariableAddress, self.modbusTypesLength[type], unit=modbusAddress)
		elif (useCommand == 4):
			rr = self.modbusClient.read_input_registers(modbusVariableAddress, self.modbusTypesLength[type], unit=modbusAddress)

		if (not rr.isError()):
			responseValue = self.__convertModbusResponseValue(type,rr,byteorder,wordorder)
			#print (responseValue)
		return responseValue

	def __convertModbusResponseValue(self,type,response,byteorder,wordorder):
		decoder = BinaryPayloadDecoder.fromRegisters(response.registers,byteorder=byteorder,wordorder=wordorder)
		if (type == 'int'):
			decoded = OrderedDict([('16int', decoder.decode_16bit_int()),])
		if (type == 'uint'):
			decoded = OrderedDict([('16uint', decoder.decode_16bit_uint()),])
		if (type == 'dint'):
			decoded = OrderedDict([('32int', decoder.decode_32bit_int())],)
		if (type == 'duint'):
			decoded = OrderedDict([('32uint', decoder.decode_32bit_uint()),])

		for name, value in iteritems(decoded):
			decodedValue = value

		return decodedValue


class StationTCP(Station):
	def SetConnParams(self,ipAddress,ipPort=502):
		self.ipAddress = ipAddress
		self.ipPort = ipPort
	def run(self):
		self.modbusClient = ModbusTcpClient(self.ipAddress,self.ipPort)		
		self.runCycleInstance()

class StationRTU(Station):
	def SetConnParams(self,serialPort,method='rtu',baudrate=9600,timeout=3,stopbits=1,parity='N',bytesize=8):
		self.serialPort = serialPort
		self.method=method
		self.baudrate=baudrate
		self.bytesize=bytesize
		self.stopbits=stopbits
		self.parity=parity
		self.timeout=timeout
	def run(self):
		self.modbusClient = ModbusSerialClient(port=self.serialPort,method=self.method,baudrate=self.baudrate,timeout=self.timeout,stopbits=self.stopbits,parity=self.parity,bytesize=self.bytesize)		
		self.runCycleInstance()		