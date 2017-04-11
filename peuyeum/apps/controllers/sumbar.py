import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sumbar'
		provloc = '100.562894, -0.706683'
		mapzoom = '9'
		kabkotcord = [
		'99.111353, -1.632146',
		'100.727108, -1.470586',
		'100.645164, -0.785734',
		'101.023388, -0.592427',
		'100.549821, -0.425873',
		'100.120617, -0.651857',
		'100.101498, -0.231207',
		'100.544888,0.049669',
		'100.060971,0.550926',
		'101.182893,-1.393285',
		'101.585028,-1.036393',
		'99.58297,0.244264',
		'100.39263,-0.932656',
		'100.651001,-0.782816',
		'100.742198,-0.645677',
		'100.401388,-0.466746',
		'100.373096,-0.300014',
		'100.625714,-0.219539',
		'100.138625,-0.595904',
		'100.522962,-0.574756'
		]
		listkabkot = [
		'%1301%','%1302%','%1303%','%1304%','%1305%','%1306%','%1307%','%1308%','%1309%','%1310%',
		'%1311%','%1312%',
		'%1371%','%1372%','%1373%','%1374%','%1375%','%1376%','%1377%','%1388%'
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