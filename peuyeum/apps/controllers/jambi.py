import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'jambi'
		provloc = '103.616048, -1.610092'
		mapzoom = '9'
		kabkotcord = [
		'101.592764, -2.157274',
		'102.680876, -2.425497',
		'102.711088, -2.420009',
		'102.990716, -1.638899',
		'103.757669, -1.531895',
		'104.106413, -1.107999',
		'103.049654, -1.1474971',
		'102.355934, -1.282591',
		'101.846269, -1.672173',
		'103.604032, -1.614553',
		'101.411225, -2.066537'
		]
		listkabkot = [
		'%1501%','%1502%','%1503%','%1504%','%1505%','%1506%','%1507%','%1508%','%1509%'
		'%1571%','%1572%'
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