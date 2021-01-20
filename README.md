# Modbus2Zabbix python scripts

### To-do
* **Ansibe**-script for automatic install libraries
* standalone config file
* add new devices:
  * Socomec (~~Diris A10/A20/A30/A40/A40new~~, Digiware)
  * Lovato DMK
  * OWEN (input modules)
  * Autonics TK4
* multiple registers request
* Docker-image
* logging (console/file/syslog)
* send data to Prometheus.io 
* send data to InfluxBD
* report generator engine
* async sending data to DB or Zabbix as group of values



### Zabbix template generation

`#python zabbixtemplategenerator.py <DEVICENAME>`
`DEVICENAME` - name of parameters list from devicemodel.py
Generated xml template `DEVICENAME.xml` save into folder zabbix_templates.

Example: `#python zabbixtemplategenerator.py TEST`