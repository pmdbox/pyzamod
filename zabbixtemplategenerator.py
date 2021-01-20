import sys
from datetime import datetime
import xml.etree.ElementTree as ET
import xml.dom.minidom
from devicemodels import *

#Settings
now = datetime.now()
historyBackupPeriod = '365d'
trendBackupPeriod = '3650d'
templateFolder = "zabbix_templates/"

# Select device
deviceRegistersName = sys.argv[1]
deviceRegisters = globals()[deviceRegistersName]

applicationsList = []
for deviceRegister in deviceRegisters:
	if(applicationsList.count(deviceRegister[9])<1):
		applicationsList.append(deviceRegister[9])


zabbix_export = ET.Element("zabbix_export")

ET.SubElement(zabbix_export, "version").text = "4.0"
ET.SubElement(zabbix_export, "date").text = now.strftime("%Y-%m-%dT%H:%M:%SZ") 

groups = ET.SubElement(zabbix_export, "groups")
group = ET.SubElement(groups, "group")
ET.SubElement(group, "name").text = 'PyZaMod' 

templates = ET.SubElement(zabbix_export, "templates")
template = ET.SubElement(templates, "template")
ET.SubElement(template, "template").text = deviceRegistersName
ET.SubElement(template, "name").text = deviceRegistersName
ET.SubElement(template, "description")

groups = ET.SubElement(template, "groups")
group = ET.SubElement(groups, "group")
ET.SubElement(group, "name").text = 'PyZaMod' 

applications = ET.SubElement(template, "applications")
for applicationRow in applicationsList:
	application = ET.SubElement(applications, "application")
	ET.SubElement(application, "name").text = applicationRow 

items = ET.SubElement(template, "items")

for deviceRegister in deviceRegisters:
	item = ET.SubElement(items, "item")
	ET.SubElement(item, "name").text = deviceRegister[0]
	ET.SubElement(item, "type").text = '2'
	ET.SubElement(item, "snmp_community").text = ''
	ET.SubElement(item, "snmp_oid").text = ''
	ET.SubElement(item, "key").text = deviceRegister[0]
	ET.SubElement(item, "delay").text = '0'
	ET.SubElement(item, "history").text = historyBackupPeriod
	ET.SubElement(item, "trends").text = trendBackupPeriod
	ET.SubElement(item, "status").text = '0'
	ET.SubElement(item, "value_type").text = '0'
	ET.SubElement(item, "allowed_hosts").text = ''
	ET.SubElement(item, "units").text = deviceRegister[8]
	ET.SubElement(item, "snmpv3_contextname").text = ''
	ET.SubElement(item, "snmpv3_securityname").text = ''
	ET.SubElement(item, "snmpv3_securitylevel").text = '0'
	ET.SubElement(item, "snmpv3_authprotocol").text = '0'
	ET.SubElement(item, "snmpv3_authpassphrase").text = ''
	ET.SubElement(item, "snmpv3_privprotocol").text = '0'
	ET.SubElement(item, "snmpv3_privpassphrase").text = ''
	ET.SubElement(item, "params").text = ''
	ET.SubElement(item, "ipmi_sensor").text = ''
	ET.SubElement(item, "authtype").text = '0'
	ET.SubElement(item, "username").text = ''
	ET.SubElement(item, "password").text = ''
	ET.SubElement(item, "publickey").text = ''
	ET.SubElement(item, "privatekey").text = ''
	ET.SubElement(item, "port").text = ''
	ET.SubElement(item, "description").text = deviceRegister[7]
	ET.SubElement(item, "inventory_link").text = '0'

	applications = ET.SubElement(item, "applications")
	application = ET.SubElement(applications, "application")
	ET.SubElement(application, "name").text = deviceRegister[9]

	ET.SubElement(item, "valuemap").text = ''
	ET.SubElement(item, "logtimefmt").text = ''
	ET.SubElement(item, "preprocessing").text = ''
	ET.SubElement(item, "jmx_endpoint").text = ''
	ET.SubElement(item, "timeout").text = '3s'
	ET.SubElement(item, "url").text = ''
	ET.SubElement(item, "query_fields").text = ''
	ET.SubElement(item, "posts").text = ''
	ET.SubElement(item, "status_codes").text = '200'
	ET.SubElement(item, "follow_redirects").text = '1'
	ET.SubElement(item, "post_type").text = '0'
	ET.SubElement(item, "http_proxy").text = ''
	ET.SubElement(item, "headers").text = ''
	ET.SubElement(item, "retrieve_mode").text = '0'
	ET.SubElement(item, "request_method").text = '0'
	ET.SubElement(item, "output_format").text = '0'
	ET.SubElement(item, "allow_traps").text = '0'
	ET.SubElement(item, "ssl_cert_file").text = ''
	ET.SubElement(item, "ssl_key_file").text = ''
	ET.SubElement(item, "ssl_key_password").text = ''
	ET.SubElement(item, "verify_peer").text = '0'
	ET.SubElement(item, "verify_host").text = '0'
	ET.SubElement(item, "master_item").text = ''


discovery_rules = ET.SubElement(template, "discovery_rules")
httptests = ET.SubElement(template, "httptests")
macros = ET.SubElement(template, "macros")

templates2 = ET.SubElement(template, "templates")
template2 = ET.SubElement(templates2, "template")
ET.SubElement(template2, "name").text = 'PyZaModPollingInfo'

screens = ET.SubElement(template, "screens")


# Save to file
tree = ET.tostring(zabbix_export, encoding='utf-8', method='xml').decode("utf-8")
xmlfile = open(templateFolder+deviceRegistersName+".xml", "w", encoding="utf-8")
xmlfile.write(tree)
xmlfile.close()


# Pretty XML and save to file
#print(str(tree))
#dom = xml.dom.minidom.parseString(tree)
#tree = dom.toprettyxml()
#xmlfile = open(deviceRegistersName+"template.xml", "w", encoding="utf-8")
#xmlfile.write(tree)
#xmlfile.close()
