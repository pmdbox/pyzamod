""""
LIST ROW description

0. tagname
1. registry address
2. data type
3. device min
4. device max
5. real min
6. real max
7. comment
8. unit
9. Zabbix group
10. word indian
11. byte indian
12. value additional
13. read speed
"""

TEST = [
['HOURMETER',512,'duint',0,3600.0,0,1.0,'Hour Meter','h','Status','Big','Big',0,'slow'],
['F',0,'duint',0,1000.0,0,1.0,'Hour Meter','Hz','Status','Big','Big',0,'slow']
]

# Socomec DIRIS A30 HOME TEST
DIRISA30HOMETEST = [
['HOURMETER',50512,'duint',0,100,0,1,'Total operating hours counter ','h','Status','Big','Big',0,'slow'],
['V1',50520,'duint',0,100,0,1,'Ph-N Voltage : V1','V','Voltage','Big','Big',0,'fast'],
['F',50526,'duint',0,100,0,1,'Frequency','Hz','Voltage','Big','Big',0,'fast'],
['Vsys',50572,'duint',0,100,0,1,'System Ph-N Voltage','V','Voltage','Big','Big',0,'fast'],
['THDV1',51539,'uint',0,10,0,1,'Ph-N Voltage total harmonic distortion : THD V1','%','THD','Big','Big',0,'fast']
]

# Socomec DIRIS A10 
DIRISA10 = [
['HOURMETER',50512,'duint',0,100,0,1,'Hour Meter','h','Status','Big','Big',0,'slow'],
['U12',50514,'duint',0,100,0,1,'Phase to Phase Voltage: U12','V','Voltage','Big','Big',0,'fast'],
['U23',50516,'duint',0,100,0,1,'Phase to Phase Voltage: U23','V','Voltage','Big','Big',0,'fast'],
['U31',50518,'duint',0,100,0,1,'Phase to Phase Voltage: U31','V','Voltage','Big','Big',0,'fast'],
['V1',50520,'duint',0,100,0,1,'Simple voltage : V1','V','Voltage','Big','Big',0,'fast'],
['V2',50522,'duint',0,100,0,1,'Simple voltage : V2','V','Voltage','Big','Big',0,'fast'],
['V3',50524,'duint',0,100,0,1,'Simple voltage : V3','V','Voltage','Big','Big',0,'fast'],
['F',50526,'duint',0,100,0,1,'Frequency : F','Hz','Voltage','Big','Big',0,'fast'],
['I1',50528,'duint',0,1000,0,1,'Current : I1','A','Current','Big','Big',0,'fast'],
['I2',50530,'duint',0,1000,0,1,'Current : I2','A','Current','Big','Big',0,'fast'],
['I3',50532,'duint',0,1000,0,1,'Current : I3','A','Current','Big','Big',0,'fast'],
['In',50534,'duint',0,1000,0,1,'Neutral Current : In','A','Current','Big','Big',0,'fast'],
['P',50536,'dint',0,1,0,10,'Active Power +/- : P','W','Power','Big','Big',0,'fast'],
['Q',50538,'dint',0,1,0,10,'Reactive Power +/- : Q','var','Power','Big','Big',0,'fast'],
['S',50540,'duint',0,1,0,10,'Apparent Power : S','VA','Power','Big','Big',0,'fast'],
['PFsys',50542,'dint',0,1000,0,1,'Power Factor : -: leading et + : lagging : PF','0','PowerFactor','Big','Big',0,'fast'],
['P1',50544,'dint',0,1,0,10,'Active Power phase 1 +/- : P1','W 10','Power','Big','Big',0,'fast'],
['P2',50546,'dint',0,1,0,10,'Active Power phase 2 +/- : P2','W 10','Power','Big','Big',0,'fast'],
['P3',50548,'dint',0,1,0,10,'Active Power phase 3 +/- : P3','W 10','Power','Big','Big',0,'fast'],
['Q1',50550,'dint',0,1,0,10,'Reactive Power phase 1 +/- : Q1','var 10','Power','Big','Big',0,'fast'],
['Q2',50552,'dint',0,1,0,10,'Reactive Power phase 2 +/- : Q2','var 10','Power','Big','Big',0,'fast'],
['Q3',50554,'dint',0,1,0,10,'Reactive Power phase 3 +/- : Q3','var 10','Power','Big','Big',0,'fast'],
['S1',50556,'duint',0,1,0,10,'Apparent Power phase 1 : S1','VA 10','Power','Big','Big',0,'fast'],
['S2',50558,'duint',0,1,0,10,'Apparent Power phase 2 : S2','VA 10','Power','Big','Big',0,'fast'],
['S3',50560,'duint',0,1,0,10,'Apparent Power phase 3 : S3','VA 10','Power','Big','Big',0,'fast'],
['PF',50574,'dint',0,1000,0,1,'Total power factor','0','PowerFactor','Big','Big',0,'fast'],
['PF1',50576,'dint',0,1000,0,1,'Power factor : PF1','0','PowerFactor','Big','Big',0,'fast'],
['PF2',50578,'dint',0,1000,0,1,'Power factor : PF2','0','PowerFactor','Big','Big',0,'fast'],
['PF3',50580,'dint',0,1000,0,1,'Power factor : PF3','0','PowerFactor','Big','Big',0,'fast'],
['HOURMETERPARTIAL',50768,'duint',0,100,0,1,'Hour meter partial energies','h','Status','Big','Big',0,'slow'],
['THDU12',51536,'uint',0,10,0,1,'thd U12','%','THD','Big','Big',0,'fast'],
['THDU23',51537,'uint',0,10,0,1,'thd U23','%','THD','Big','Big',0,'fast'],
['THDU31',51538,'uint',0,10,0,1,'thd U31','%','THD','Big','Big',0,'fast'],
['THDV1',51539,'uint',0,10,0,1,'thd V1','%','THD','Big','Big',0,'fast'],
['THDV2',51540,'uint',0,10,0,1,'thd V2','%','THD','Big','Big',0,'fast'],
['THDV3',51541,'uint',0,10,0,1,'thd V3','%','THD','Big','Big',0,'fast'],
['THDI1',51542,'uint',0,10,0,1,'thd I1','%','THD','Big','Big',0,'fast'],
['THDI2',51543,'uint',0,10,0,1,'thd I2','%','THD','Big','Big',0,'fast'],
['THDI3',51544,'uint',0,10,0,1,'thd I3','%','THD','Big','Big',0,'fast'],
['Eapos',51311,'uint',0,1,0,1,'Total Positive Active Energy (no resetable) : Ea+','MWh','Energies','Big','Big',0,'slow'],
['Eaneg',51312,'uint',0,1,0,1,'Total Negative Active Energy (no resetable) : Ea -','MWh','Energies','Big','Big',0,'slow'],
['Erpos',51313,'uint',0,1,0,1,'Total Positive Reactive Energy (no resetable) : Er +','Mvarh','Energies','Big','Big',0,'slow'],
['Erneg',51314,'uint',0,1,0,1,'Total Negative Reactive Energy (no resetable) : Er -','Mvarh','Energies','Big','Big',0,'slow']
]

# Socomec DIRIS A20 
DIRISA20 = [
['HOURMETER',50512,'duint',0,100,0,1,'Hour Meter','h','Status','Big','Big',0,'slow'],
['U12',50514,'duint',0,100,0,1,'Phase to Phase Voltage: U12','V','Voltage','Big','Big',0,'fast'],
['U23',50516,'duint',0,100,0,1,'Phase to Phase Voltage: U23','V','Voltage','Big','Big',0,'fast'],
['U31',50518,'duint',0,100,0,1,'Phase to Phase Voltage: U31','V','Voltage','Big','Big',0,'fast'],
['V1',50520,'duint',0,100,0,1,'Simple voltage : V1','V','Voltage','Big','Big',0,'fast'],
['V2',50522,'duint',0,100,0,1,'Simple voltage : V2','V','Voltage','Big','Big',0,'fast'],
['V3',50524,'duint',0,100,0,1,'Simple voltage : V3','V','Voltage','Big','Big',0,'fast'],
['F',50526,'duint',0,100,0,1,'Frequency : F','Hz','Voltage','Big','Big',0,'fast'],
['I1',50528,'duint',0,1000,0,1,'Current : I1','A','Current','Big','Big',0,'fast'],
['I2',50530,'duint',0,1000,0,1,'Current : I2','A','Current','Big','Big',0,'fast'],
['I3',50532,'duint',0,1000,0,1,'Current : I3','A','Current','Big','Big',0,'fast'],
['In',50534,'duint',0,1000,0,1,'Neutral Current : In','A','Current','Big','Big',0,'fast'],
['P',50536,'dint',0,1,0,10,'Active Power +/- : P','W','Power','Big','Big',0,'fast'],
['Q',50538,'dint',0,1,0,10,'Reactive Power +/- : Q','var','Power','Big','Big',0,'fast'],
['S',50540,'duint',0,1,0,10,'Apparent Power : S','VA','Power','Big','Big',0,'fast'],
['PFsys',50542,'dint',0,1000,0,1,'Power Factor : -: leading et + : lagging : PF','0','PowerFactor','Big','Big',0,'fast'],
['P1',50544,'dint',0,1,0,10,'Active Power phase 1 +/- : P1','W 10','Power','Big','Big',0,'fast'],
['P2',50546,'dint',0,1,0,10,'Active Power phase 2 +/- : P2','W 10','Power','Big','Big',0,'fast'],
['P3',50548,'dint',0,1,0,10,'Active Power phase 3 +/- : P3','W 10','Power','Big','Big',0,'fast'],
['Q1',50550,'dint',0,1,0,10,'Reactive Power phase 1 +/- : Q1','var 10','Power','Big','Big',0,'fast'],
['Q2',50552,'dint',0,1,0,10,'Reactive Power phase 2 +/- : Q2','var 10','Power','Big','Big',0,'fast'],
['Q3',50554,'dint',0,1,0,10,'Reactive Power phase 3 +/- : Q3','var 10','Power','Big','Big',0,'fast'],
['S1',50556,'duint',0,1,0,10,'Apparent Power phase 1 : S1','VA 10','Power','Big','Big',0,'fast'],
['S2',50558,'duint',0,1,0,10,'Apparent Power phase 2 : S2','VA 10','Power','Big','Big',0,'fast'],
['S3',50560,'duint',0,1,0,10,'Apparent Power phase 3 : S3','VA 10','Power','Big','Big',0,'fast'],
['PF1sys',50562,'dint',0,1000,0,1,'Power Factor phase 1 -: leading and + : lagging : PF1 ','0','PowerFactor','Big','Big',0,'fast'],
['PF2sys',50564,'dint',0,1000,0,1,'Power Factor phase 2 -: leading and + : lagging : PF2 ','0','PowerFactor','Big','Big',0,'fast'],
['PF3sys',50566,'dint',0,1000,0,1,'Power Factor phase 3 -: leading and + : lagging : PF3 ','0','PowerFactor','Big','Big',0,'fast'],
['Isys',50568,'duint',0,1000,0,1,'System value I Sys : ( I1+I2+I3) / 3 ','A','Current','Big','Big',0,'fast'],
['Usys',50570,'duint',0,100,0,1,'System value U Sys : (U12 + U23 + U31 ) / 3 ','V','Voltage','Big','Big',0,'fast'],
['Vsys',50572,'duint',0,100,0,1,'System value V Sys : (V1 + V2 + V3 ) / 3 ','V','Voltage','Big','Big',0,'fast'],
['PF',50574,'dint',0,1000,0,1,'Total power factor (IEC) ','0','PowerFactor','Big','Big',0,'fast'],
['PF1',50576,'dint',0,1000,0,1,'Power factor : PF1 (IEC) ','0','PowerFactor','Big','Big',0,'fast'],
['PF2',50578,'dint',0,1000,0,1,'Power factor : PF2 (IEC) ','0','PowerFactor','Big','Big',0,'fast'],
['PF3',50580,'dint',0,1000,0,1,'Power factor : PF3 (IEC) ','0','PowerFactor','Big','Big',0,'fast'],
['Vnba',50586,'duint',0,100,0,1,'Vnba','%','Current','Big','Big',0,'fast'],
['Unba',50588,'duint',0,100,0,1,'Unba','%','Voltage','Big','Big',0,'fast'],
['Inba',50590,'duint',0,100,0,1,'Inba','%','Voltage','Big','Big',0,'fast'],
['HOURMETERPARTIAL',50768,'duint',0,100,0,1,'Hour meter partial energies','h','Status','Big','Big',0,'slow'],
['Eapos',50780,'duint',0,1,0,1,'Total Positive active Energy : Ea+','kWh','Energies','Big','Big',0,'slow'],
['Erpos',50782,'duint',0,1,0,1,'Total Positive reactive Energy : Er+','kvarh','Energies','Big','Big',0,'slow'],
['Eap',50784,'duint',0,1,0,1,'Total Apparent Energy : Eap','kVAh','Energies','Big','Big',0,'slow'],
['Eaneg',50786,'duint',0,1,0,1,'Total Negative active Energy : Ea-','kWh','Energies','Big','Big',0,'slow'],
['Erneg',50788,'duint',0,1,0,1,'Total Negative reactive Energy : Er-','kvarh','Energies','Big','Big',0,'slow'],
['THDU12',51536,'uint',0,10,0,1,'thd U12','%','THD','Big','Big',0,'fast'],
['THDU23',51537,'uint',0,10,0,1,'thd U23','%','THD','Big','Big',0,'fast'],
['THDU31',51538,'uint',0,10,0,1,'thd U31','%','THD','Big','Big',0,'fast'],
['THDV1',51539,'uint',0,10,0,1,'thd V1','%','THD','Big','Big',0,'fast'],
['THDV2',51540,'uint',0,10,0,1,'thd V2','%','THD','Big','Big',0,'fast'],
['THDV3',51541,'uint',0,10,0,1,'thd V3','%','THD','Big','Big',0,'fast'],
['THDI1',51542,'uint',0,10,0,1,'thd I1','%','THD','Big','Big',0,'fast'],
['THDI2',51543,'uint',0,10,0,1,'thd I2','%','THD','Big','Big',0,'fast'],
['THDI3',51544,'uint',0,10,0,1,'thd I3','%','THD','Big','Big',0,'fast'],
['THDIn',51545,'uint',0,10,0,1,'thd In','%','THD','Big','Big',0,'fast']
]

# Socomec DIRIS A30/A40 
DIRISA30 = [
['HOURMETER',50512,'duint',0,100,0,1,'Total operating hours counter ','h','Status','Big','Big',0,'slow'],
['U12',50514,'duint',0,100,0,1,'Ph-Ph Voltage : U12','V','Voltage','Big','Big',0,'fast'],
['U23',50516,'duint',0,100,0,1,'Ph-Ph Voltage : U23','V','Voltage','Big','Big',0,'fast'],
['U31',50518,'duint',0,100,0,1,'Ph-Ph Voltage : U31','V','Voltage','Big','Big',0,'fast'],
['V1',50520,'duint',0,100,0,1,'Ph-N Voltage : V1','V','Voltage','Big','Big',0,'fast'],
['V2',50522,'duint',0,100,0,1,'Ph-N Voltage : V2','V','Voltage','Big','Big',0,'fast'],
['V3',50524,'duint',0,100,0,1,'Ph-N Voltage : V3','V','Voltage','Big','Big',0,'fast'],
['F',50526,'duint',0,100,0,1,'Frequency','Hz','Voltage','Big','Big',0,'fast'],
['I1',50528,'duint',0,1000,0,1,'Current : I1','А','Current','Big','Big',0,'fast'],
['I2',50530,'duint',0,1000,0,1,'Current : I2','А','Current','Big','Big',0,'fast'],
['I3',50532,'duint',0,1000,0,1,'Current : I3','А','Current','Big','Big',0,'fast'],
['In',50534,'duint',0,1000,0,1,'Current : In','А','Current','Big','Big',0,'fast'],
['P',50536,'dint',0,1,0,10,'Total active power','W','Power','Big','Big',0,'fast'],
['Q',50538,'dint',0,1,0,10,'Total reactive power','var','Power','Big','Big',0,'fast'],
['S',50540,'duint',0,1,0,10,'Total apparent power','VA','Power','Big','Big',0,'fast'],
['PF',50542,'dint',0,1000,0,1,'Total power factor','0','PowerFactor','Big','Big',0,'fast'],
['P1',50544,'dint',0,1,0,10,'Active power : P1','W','Power','Big','Big',0,'fast'],
['P2',50546,'dint',0,1,0,10,'Active power : P2','W','Power','Big','Big',0,'fast'],
['P3',50548,'dint',0,1,0,10,'Active power : P3','W','Power','Big','Big',0,'fast'],
['Q1',50550,'dint',0,1,0,10,'Reactive power : Q1','var','Power','Big','Big',0,'fast'],
['Q2',50552,'dint',0,1,0,10,'Reactive power : Q2','var','Power','Big','Big',0,'fast'],
['Q3',50554,'dint',0,1,0,10,'Reactive power : Q3','var','Power','Big','Big',0,'fast'],
['S1',50556,'duint',0,1,0,10,'Apparent power : S1','VA','Power','Big','Big',0,'fast'],
['S2',50558,'duint',0,1,0,10,'Apparent power : S2','VA','Power','Big','Big',0,'fast'],
['S3',50560,'duint',0,1,0,10,'Apparent power : S3','VA','Power','Big','Big',0,'fast'],
['PF1',50562,'dint',0,1000,0,1,'Power factor : PF1','0','PowerFactor','Big','Big',0,'fast'],
['PF2',50564,'dint',0,1000,0,1,'Power factor : PF2','0','PowerFactor','Big','Big',0,'fast'],
['PF3',50566,'dint',0,1000,0,1,'Power factor : PF3','0','PowerFactor','Big','Big',0,'fast'],
['ISys',50568,'duint',0,1000,0,1,'System Current','А','Current','Big','Big',0,'fast'],
['Usys',50570,'duint',0,100,0,1,'System Ph-Ph Voltage','V','Voltage','Big','Big',0,'fast'],
['Vsys',50572,'duint',0,100,0,1,'System Ph-N Voltage','V','Voltage','Big','Big',0,'fast'],
['Inba',50586,'duint',0,10,0,1,'Inba','%','Current','Big','Big',0,'fast'],
['Unba',50588,'duint',0,10,0,1,'Unba','%','Voltage','Big','Big',0,'fast'],
['Vnba',50590,'duint',0,10,0,1,'Vnba','%','Voltage','Big','Big',0,'fast'],
['Eapos',50780,'duint',0,1,0,1,'Total Positive active Energy : Ea+','kWh','Energies','Big','Big',0,'slow'],
['Erpos',50782,'duint',0,1,0,1,'Total Positive reactive Energy : Er+','kvarh','Energies','Big','Big',0,'slow'],
['Eap',50784,'duint',0,1,0,1,'Total Apparent Energy : Eap','kVAh','Energies','Big','Big',0,'slow'],
['Eaneg',50786,'duint',0,1,0,1,'Total Negative active Energy : Ea-','kWh','Energies','Big','Big',0,'slow'],
['Erneg',50788,'duint',0,1,0,1,'Total Negative reactive Energy : Er-','kvarh','Energies','Big','Big',0,'slow'],
['KFactorI1',51472,'uint',0,100,0,1,'K-Factor I1','0','THD','Big','Big',0,'fast'],
['KFactorI2',51473,'uint',0,100,0,1,'K-Factor I2','0','THD','Big','Big',0,'fast'],
['KFactorI3',51474,'uint',0,100,0,1,'K-Factor I3','0','THD','Big','Big',0,'fast'],
['KFactorIn',51475,'uint',0,100,0,1,'K-Factor In','0','THD','Big','Big',0,'fast'],
['TDDI1',51476,'uint',0,10,0,1,'Total demand distortion : TDD I1','%','THD','Big','Big',0,'fast'],
['TDDI2',51477,'uint',0,10,0,1,'Total demand distortion : TDD I2','%','THD','Big','Big',0,'fast'],
['TDDI3',51478,'uint',0,10,0,1,'Total demand distortion : TDD I3','%','THD','Big','Big',0,'fast'],
['TDDIn',51479,'uint',0,10,0,1,'Total demand distortion : TDD In','%','THD','Big','Big',0,'fast'],
['THDU12',51536,'uint',0,10,0,1,'Ph-Ph Voltage total harmonic distortion : THD U12','%','THD','Big','Big',0,'fast'],
['THDU23',51537,'uint',0,10,0,1,'Ph-Ph Voltage total harmonic distortion : THD U23','%','THD','Big','Big',0,'fast'],
['THDU31',51538,'uint',0,10,0,1,'Ph-Ph Voltage total harmonic distortion : THD U31','%','THD','Big','Big',0,'fast'],
['THDV1',51539,'uint',0,10,0,1,'Ph-N Voltage total harmonic distortion : THD V1','%','THD','Big','Big',0,'fast'],
['THDV2',51540,'uint',0,10,0,1,'Ph-N Voltage total harmonic distortion : THD V2','%','THD','Big','Big',0,'fast'],
['THDV3',51541,'uint',0,10,0,1,'Ph-N Voltage total harmonic distortion : THD V3','%','THD','Big','Big',0,'fast'],
['THDI1',51542,'uint',0,10,0,1,'Curent total harmonic distortion : THD I1','%','THD','Big','Big',0,'fast'],
['THDI2',51543,'uint',0,10,0,1,'Curent total harmonic distortion : THD I2','%','THD','Big','Big',0,'fast'],
['THDI3',51544,'uint',0,10,0,1,'Curent total harmonic distortion : THD I3','%','THD','Big','Big',0,'fast'],
['THDIn',51545,'uint',0,10,0,1,'Curent total harmonic distortion : THD In','%','THD','Big','Big',0,'fast']
]


# Socomec DIRIS A40 new 
DIRISA40NEW = [
['HOURMETER',512,'duint',0,3600,0,1,'Total operating hours counter (лічильник мотогодин)','h','Status','Big','Big',0,'slow'],
['HOURMETERPARTIAL',514,'duint',0,3600,0,1,'Partial operating hours counter ','h','Status','Big','Big',0,'slow'],
['Vsys',36867,'duint',0,100,0,1,'System Ph-N Voltage','V','Voltage','Big','Big',0,'fast'],
['Usys',36869,'duint',0,100,0,1,'System Ph-Ph Voltage','V','Voltage','Big','Big',0,'fast'],
['F',36871,'duint',0,1000,0,1,'Frequency','Hz','Voltage','Big','Big',0,'fast'],
['V1',36873,'duint',0,100,0,1,'Ph-N Voltage : V1','V','Voltage','Big','Big',0,'fast'],
['V2',36875,'duint',0,100,0,1,'Ph-N Voltage : V2','V','Voltage','Big','Big',0,'fast'],
['V3',36877,'duint',0,100,0,1,'Ph-N Voltage : V3','V','Voltage','Big','Big',0,'fast'],
['Vn',36879,'duint',0,100,0,1,'Ph-N Voltage : Vn','V','Voltage','Big','Big',0,'fast'],
['U12',36881,'duint',0,100,0,1,'Ph-Ph Voltage : U12','V','Voltage','Big','Big',0,'fast'],
['U23',36883,'duint',0,100,0,1,'Ph-Ph Voltage : U23','V','Voltage','Big','Big',0,'fast'],
['U31',36885,'duint',0,100,0,1,'Ph-Ph Voltage : U31','V','Voltage','Big','Big',0,'fast'],
['Vdir',36887,'duint',0,100,0,1,'Vdir','V','Voltage','Big','Big',0,'fast'],
['Vinv',36889,'duint',0,100,0,1,'Vinv','V','Voltage','Big','Big',0,'fast'],
['Vhom',36891,'duint',0,100,0,1,'Vhom','V','Voltage','Big','Big',0,'fast'],
['Vnb',36893,'uint',0,100,0,1,'Vnb','%','Voltage','Big','Big',0,'fast'],
['Udir',36894,'duint',0,100,0,1,'Udir','V','Voltage','Big','Big',0,'fast'],
['Uinv',36896,'duint',0,100,0,1,'Uinv','V','Voltage','Big','Big',0,'fast'],
['Unb',36898,'uint',0,100,0,1,'Unb','%','Voltage','Big','Big',0,'fast'],
['Vnba',36899,'uint',0,100,0,1,'Vnba','%','Voltage','Big','Big',0,'fast'],
['Unba',36900,'uint',0,100,0,1,'Unba','%','Voltage','Big','Big',0,'fast'],
['THDV1',37144,'uint',0,100,0,1,'Ph-N Voltage total harmonic distortion : THD V1','%','THD','Big','Big',0,'fast'],
['THDV2',37145,'uint',0,100,0,1,'Ph-N Voltage total harmonic distortion : THD V2','%','THD','Big','Big',0,'fast'],
['THDV3',37146,'uint',0,100,0,1,'Ph-N Voltage total harmonic distortion : THD V3','%','THD','Big','Big',0,'fast'],
['THDU12',37147,'uint',0,100,0,1,'Ph-Ph Voltage total harmonic distortion : THD U12','%','THD','Big','Big',0,'fast'],
['THDU23',37148,'uint',0,100,0,1,'Ph-Ph Voltage total harmonic distortion : THD U23','%','THD','Big','Big',0,'fast'],
['THDU31',37149,'uint',0,100,0,1,'Ph-Ph Voltage total harmonic distortion : THD U31','%','THD','Big','Big',0,'fast'],
['THDV',37150,'uint',0,100,0,1,'System THD V','%','THD','Big','Big',0,'fast'],
['THDU',37151,'uint',0,100,0,1,'System THD U','%','THD','Big','Big',0,'fast'],
['CRESTV1',37152,'uint',0,1000,0,1,'Crest factor : V1','0','THD','Big','Big',0,'fast'],
['CRESTV2',37153,'uint',0,1000,0,1,'Crest factor : V2','0','THD','Big','Big',0,'fast'],
['CRESTV3',37154,'uint',0,1000,0,1,'Crest factor : V3','0','THD','Big','Big',0,'fast'],
['CRESTU12',37155,'uint',0,1000,0,1,'Crest factor : U12','0','THD','Big','Big',0,'fast'],
['CRESTU23',37156,'uint',0,1000,0,1,'Crest factor : U23','0','THD','Big','Big',0,'fast'],
['CRESTU31',37157,'uint',0,1000,0,1,'Crest factor : U31','0','THD','Big','Big',0,'fast'],
['ISys',18440,'duint',0,1000,0,1,'System Current','A','Current','Big','Big',0,'fast'],
['I1',18458,'duint',0,1000,0,1,'Current : I1','A','Current','Big','Big',0,'fast'],
['I2',18460,'duint',0,1000,0,1,'Current : I2','A','Current','Big','Big',0,'fast'],
['I3',18462,'duint',0,1000,0,1,'Current : I3','A','Current','Big','Big',0,'fast'],
['In',18464,'duint',0,1000,0,1,'Current : In','A','Current','Big','Big',0,'fast'],
['Inba',18466,'uint',0,100,0,1,'Inba','%','Current','Big','Big',0,'fast'],
['Idir',18467,'duint',0,1000,0,1,'Idir','A','Current','Big','Big',0,'fast'],
['Iinv',18469,'duint',0,1000,0,1,'Iinv','A','Current','Big','Big',0,'fast'],
['Ihom',18471,'duint',0,1000,0,1,'Ihom','A','Current','Big','Big',0,'fast'],
['Inb',18473,'uint',0,100,0,1,'Inb','%','Current','Big','Big',0,'fast'],
['Snom',18474,'duint',0,1,0,1,'Snom','VA','Power','Big','Big',0,'fast'],
['P',18476,'dint',0,1,0,1,'Total active power','W','Power','Big','Big',0,'fast'],
['Q',18478,'dint',0,1,0,1,'Total reactive power','var','Power','Big','Big',0,'fast'],
['Qlag',18480,'dint',0,1,0,1,'Total lagging reactive power','var','Power','Big','Big',0,'fast'],
['Qlead',18482,'dint',0,1,0,1,'Total leading reactive power','var','Power','Big','Big',0,'fast'],
['S',18484,'duint',0,1,0,1,'Total apparent power','VA','Power','Big','Big',0,'fast'],
['PF',18486,'int',0,1000,0,1,'Total power factor','0','PowerFactor','Big','Big',0,'fast'],
['P1',18488,'dint',0,1,0,1,'Active power : P1','W','Power','Big','Big',0,'fast'],
['P2',18490,'dint',0,1,0,1,'Active power : P2','W','Power','Big','Big',0,'fast'],
['P3',18492,'dint',0,1,0,1,'Active power : P3','W','Power','Big','Big',0,'fast'],
['Q1',18494,'dint',0,1,0,1,'Reactive power : Q1','var','Power','Big','Big',0,'fast'],
['Q2',18496,'dint',0,1,0,1,'Reactive power : Q2','var','Power','Big','Big',0,'fast'],
['Q3',18498,'dint',0,1,0,1,'Reactive power : Q3','var','Power','Big','Big',0,'fast'],
['S1',18512,'duint',0,1,0,1,'Apparent power : S1','VA','Power','Big','Big',0,'fast'],
['S2',18514,'duint',0,1,0,1,'Apparent power : S2','VA','Power','Big','Big',0,'fast'],
['S3',18516,'duint',0,1,0,1,'Apparent power : S3','VA','Power','Big','Big',0,'fast'],
['PF1',18518,'int',0,1000,0,1,'Power factor : PF1','0','PowerFactor','Big','Big',0,'fast'],
['PF2',18519,'int',0,1000,0,1,'Power factor : PF2','0','PowerFactor','Big','Big',0,'fast'],
['PF3',18520,'int',0,1000,0,1,'Power factor : PF3','0','PowerFactor','Big','Big',0,'fast'],
['THDI1',18757,'uint',0,100,0,1,'Curent total harmonic distortion : THD I1','%','THD','Big','Big',0,'fast'],
['THDI2',18758,'uint',0,100,0,1,'Curent total harmonic distortion : THD I2','%','THD','Big','Big',0,'fast'],
['THDI3',18759,'uint',0,100,0,1,'Curent total harmonic distortion : THD I3','%','THD','Big','Big',0,'fast'],
['THDIn',18760,'uint',0,100,0,1,'Curent total harmonic distortion : THD In','%','THD','Big','Big',0,'fast'],
['KFactorI1',18761,'uint',0,100,0,1,'K-Factor I1','0','THD','Big','Big',0,'fast'],
['KFactorI2',18762,'uint',0,100,0,1,'K-Factor I2','0','THD','Big','Big',0,'fast'],
['KFactorI3',18763,'uint',0,100,0,1,'K-Factor I3','0','THD','Big','Big',0,'fast'],
['KFactorIn',18764,'uint',0,100,0,1,'K-Factor In','0','THD','Big','Big',0,'fast'],
['THDI',18767,'uint',0,100,0,1,'System THD I','%','THD','Big','Big',0,'fast'],
['CRESTI1',18768,'uint',0,1000,0,1,'Crest factor : I1','0','THD','Big','Big',0,'fast'],
['CRESTI2',18769,'uint',0,1000,0,1,'Crest factor : I2','0','THD','Big','Big',0,'fast'],
['CRESTI3',18770,'uint',0,1000,0,1,'Crest factor : I3','0','THD','Big','Big',0,'fast'],
['CRESTIn',18771,'uint',0,1000,0,1,'Crest factor : In','0','THD','Big','Big',0,'fast'],
['TDDI1',18772,'uint',0,100,0,1,'Total demand distortion : TDD I1','%','THD','Big','Big',0,'fast'],
['TDDI2',18773,'uint',0,100,0,1,'Total demand distortion : TDD I2','%','THD','Big','Big',0,'fast'],
['TDDI3',18774,'uint',0,100,0,1,'Total demand distortion : TDD I3','%','THD','Big','Big',0,'fast'],
['TDDIn',18775,'uint',0,100,0,1,'Total demand distortion : TDD In','%','THD','Big','Big',0,'fast'],
['TDDI',18776,'uint',0,100,0,1,'System TDD I','%','THD','Big','Big',0,'fast'],
['Eapos',19843,'duint',0,1,0,1,'Total Positive active Energy : Ea+','kWh','Energies','Big','Big',0,'slow'],
['Eaneg',19846,'duint',0,1,0,1,'Total Negative active Energy : Ea-','kWh','Energies','Big','Big',0,'slow'],
['Erpos',19849,'duint',0,1,0,1,'Total Positive reactive Energy : Er+','kvarh','Energies','Big','Big',0,'slow'],
['Erneg',19852,'duint',0,1,0,1,'Total Negative reactive Energy : Er-','kvarh','Energies','Big','Big',0,'slow'],
['Eap',19855,'duint',0,1,0,1,'Total Apparent Energy : Eap','kVAh','Energies','Big','Big',0,'slow']
]
