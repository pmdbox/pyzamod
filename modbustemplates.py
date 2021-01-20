class ModbusVariable:

	def __init__(self, Name='', Address=0, Type='int', Min=-100.0, Max=100.0, realMin=-100.0, realMax=100.0, WordIndian='Big',ByteIndian='Big',AdditionalValue=0,ReadingSpeed='fast'):
		self.Name = Name
		self.Address = Address
		self.Type = Type
		self.Min = Min
		self.Max = Max
		self.realMin = realMin
		self.realMax = realMax
		self.Koef = (realMax-realMin)/(Max-Min)
		self.WordIndian = WordIndian
		self.ByteIndian = ByteIndian
		self.AdditionalValue = AdditionalValue
		self.ReadingSpeed = ReadingSpeed
		
	def setRawValue(self,RawValue):
		self.Value = self.AdditionalValue + self.realMin+(RawValue-self.Min)*self.Koef
			
	def getRealValue(self):
		return self.Value
		
	def getName(self):
		return self.Name		

	def getAddress(self):
		return self.Address		

	def getType(self):
		return self.Type		

	def getWordIndian(self):
		return self.WordIndian

	def getByteIndian(self):
		return self.ByteIndian

	def getReadingSpeed(self):
		return self.ReadingSpeed



		
class DeviceTemplate:

	def __init__(self,ZabbixName,ModbusAddress):
		self.Variables = []
		self.ZabbixName = ZabbixName
		self.ModbusAddress = ModbusAddress
		
	def addVariable(self,Variable):
		self.Variables.append(Variable)

	def getZabbixName(self):
		return self.ZabbixName

	def getModbusAddress(self):
		return self.ModbusAddress

	def getVariablesCount(self):
		return len(self.Variables)

	def getVariableName(self,variableIndex):
		variable = self.Variables[variableIndex]
		return variable.getName()
		
	def getVariableModbusAddress(self,variableIndex):
		variable = self.Variables[variableIndex]
		return variable.getAddress()

	def getVariableType(self,variableIndex):
		variable = self.Variables[variableIndex]
		return variable.getType()

	def setVariableValue(self,variableIndex,varibaleValue):
		variable = self.Variables[variableIndex]
		variable.setRawValue(varibaleValue)

	def getVariableValue(self,variableIndex):
		variable = self.Variables[variableIndex]
		return variable.getRealValue()

	def getByteIndian(self,variableIndex):
		variable = self.Variables[variableIndex]
		return variable.getByteIndian()

	def getWordIndian(self,variableIndex):
		variable = self.Variables[variableIndex]
		return variable.getWordIndian()

	def addVariablesList(self,deviceType):
		for deviceRegister in deviceType:
			Name = deviceRegister[0]
			Address = deviceRegister[1]
			Type = deviceRegister[2]
			Min = deviceRegister[3]
			Max = deviceRegister[4]
			MinReal = deviceRegister[5]
			MaxReal = deviceRegister[6]
			WordIndian = deviceRegister[10]
			ByteIndian = deviceRegister[11]
			AdditionalValue = deviceRegister[12]
			ReadingSpeed = deviceRegister[13]
			self.addVariable(ModbusVariable(Name,Address,Type,Min,Max,MinReal,MaxReal,WordIndian,ByteIndian,AdditionalValue,ReadingSpeed))