import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sultra'
		provloc = '121.769973, -3.549536'
		mapzoom = '9'
		kabkotcord = [
		'122.983317, -5.2259',
		'122.621585,-4.899507',
		'122.047537,-3.814249',
		'121.6582, -4.033874',
		'122.350264, -4.184038',
		'121.820088, -4.612818',
		'123.575173,-5.295817',
		'121.146659, -3.120356',
		'122.993251, -4.582295',
		'121.9762, -3.35638',
		'121.418748, -3.58453',
		'122.516099, -3.998061',
		'122.595951, -5.469694'
		]
		listkabkot = [
		'%7401%','%7402%','%7403%','%7404%','%7405%','%7406%','%7407%','%7408%','%7409%','%7410%',
		'%7411%',
		'%7471%','%7472%'
		]
		batik.provinsi(provinsi,listkabkot,provloc,mapzoom,kabkotcord)
		cal = calendar.Calendar()
		dt = {}
		for kabkot in listkabkot:
			dt[kabkot]=cal.getYearCountKabKot(str(int(kabkot[1:3])),str(int(kabkot[3:5])),uridt)
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%'+provinsi+'%home'+'%'+str(int(uridt)+1))
		cal.close()
		return dt