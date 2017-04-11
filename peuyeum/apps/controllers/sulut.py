import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sulut'
		provloc = '124.843228, 2.028072'
		mapzoom = '9'
		kabkotcord = [
		'123.999184, 0.664800',
		'124.940037, 1.167015',
		'125.544941, 3.548573',
		'126.815758, 4.276408',
		'124.448655, 1.134123',
		'125.000935, 1.571507',
		'123.495757, 0.764704',
		'125.412478, 2.346824',
		'124.715366, 1.004475',
		'123.889941, 0.405018',
		'124.580156, 0.725259',
		'1.473166, 0.725259',
		'125.129396, 1.443281',
		'124.841151, 1.322147',
		'124.322826, 0.723718',
		'124.459302, 0.763077'
		]
		listkabkot = [
		'%7101%','%7102%','%7103%','%7104%','%7105%','%7106%','%7107%','%7108%','%7109%','%7110%',
		'%7111%',
		'%7171%','%7172%','%7173%','%7174%','%7188%'
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