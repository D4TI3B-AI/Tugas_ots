import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sulteng'
		provloc = '121.569374, -1.088512'
		mapzoom = '7'
		kabkotcord = [
		'122.532670, -0.969612',
		'122.345902, -1.051996',
		'121.939852, -2.704650',
		'120.753889, -1.395064',
		'119.824081, -0.493822',
		'120.766576, 0.939380',
		'121.195815, 1.021996',
		'120.196286, 0.446431',
	
		'122.59768409999992, -5.4700112',
		'122.51297420000003, -3.9984597 122',
		'121.90179539999997, -4.2279225',
		'122.08374449999997, -3.3803291',
		'123.03387670000006, -4.702342400000001 ',
		]
		listkabkot = [
		'%7201%','%7202%','%7203%','%7204%','%7205%','%7206%','%7207%','%7208%'
		,'%7472%'
		,'%7471%','%7411%','%7410%','%7409%'
		
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