import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sumut'
		provloc = '99.188581, 2.312969'
		mapzoom = '9'
		kabkotcord = [
		'97.604550, 1.014795',
		'99.495703, 0.768582',
		'99.16264, 1.509810',
		'98.624952, 1.951664',
		'98.927957, 1.994440',
		'99.279916, 2.279898',
		'100.088714, 2.247921',
		'99.593711, 2.805695',
		'98.823982, 3.047948',
		'98.187366, 2.858667',
		'98.142541, 3.205378',
		'98.659970, 3.422239',
		'98.124419, 3.683218',
		'97.729156, 0.841165',
		'98.565878, 2.212137',
		'98.265733, 2.467432',
		'98.612349, 2.495827',
		'98.961789, 3.399369',
		'99.433258, 3.211224',
		'99.623017, 1.678944',
		'99.761596, 1.120830',
		'99.928608, 1.846106',
		'99.643374, 2.411790',
		'97.355786, 1.317017',
		'97.473903, 1.042729',
		'98.781743, 1.739830',
		'99.796590, 2.959028',
		'99.049414, 3.001106',
		'99.147946, 3.322582',
		'98.636521, 3.553873',
		'98.485410, 3.589259',
		'99.284581, 1.365369',
		'97.524199, 1.321364',
		'98.677986, 2.778086'
		]
		listkabkot = [
		'%1201%','%1202%','%1203%','%1204%','%1205%','%1206%','%1207%','%1208%','%1209%','%1210%',
		'%1211%','%1212%','%1213%','%1214%','%1215%','%1216%','%1217%','%1218%','%1219%','%1220%',
		'%1221%','%1222%','%1223%','%1224%','%1225%',
		'%1271%','%1272%','%1273%','%1274%','%1275%','%1276%','%1277%','%1278%','%1288%'
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		cal.close()
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		return dt