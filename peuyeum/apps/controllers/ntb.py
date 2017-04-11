import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'ntb'
		provloc = '117.231158, -8.240186'
		mapzoom = '9'
		kabkotcord = [
		'116.101926, -8.667428',
		'116.347291, -8.720206',
		'116.526059, -8.508658',
		'117.473154,-8.732179',
		'118.193416, -8.487878',
		'118.745947, -8.463057',
		'116.927607, -8.847619',
		'116.259665, -8.369862',
		'116.103038, -8.577178',
		'118.743887, -8.464246'
		]
		listkabkot = [
		'%5201%','%5202%','%5203%','%5204%','%5205%','%5206%','%5207%','%5208%',
		'%5271%','%5272%'
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