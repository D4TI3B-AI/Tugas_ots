import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'riau'
		provloc = '101.683500, 0.336998'
		mapzoom = '9'
		kabkotcord = [
		'101.256639, -0.397666',
		'102.27297, -0.665561',
		'103.120766, -0.062549',
		'102.070138, 0.139318',
		'101.660183, 0.759335',
		'101.113333, 0.496102',
		'100.471105,0.92068',
		'101.56657, 1.173689',
		'102.717474, 0.942233',
		'102.717474, 0.942233',
		'101.455592, 0.496625',
		'101.392573, 1.685077'
		]
		listkabkot = [
		'%1401%','%1402%','%1403%','%1404%','%1405%','%1406%','%1407%','%1408%','%1409%','%1410%',
		'%1471%','%1473%'
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