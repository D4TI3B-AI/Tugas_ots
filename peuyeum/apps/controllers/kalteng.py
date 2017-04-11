import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'kalteng'
		provloc = '113.913977,-2.2161048'
		mapzoom = '7'
		kabkotcord = [
		'111.555839, -2.456964',
		'112.737093, -2.098138',
		'114.380207, -2.920394',
		'114.8092691, -1.875943',
		'115.094045, -0.9587136',
		'111.214997, -2.552622',
		'111.423987, -1.788008',
		'112.224984, -2.607866',
		'113.371653, -1.917755',
		'113.970421, -2.778195',
		'113.52656, -1.066509',
		'115.102025, -2.009314',
		'114.192568, 0.007267',
		'113.914539, -2.216049'
		]
		listkabkot = [
		'%6201%','%6202%','%6203%','%6204%','%6205%','%6206%','%6207%','%6208%','%6209%','%6210%',
		'%6211%','%6212%','%6213%',
		'%6271%'
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