import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'banten'
		listkabkot = [
		'%3601%','%3602%','%3603%','%3604%',
		'%3671%','%3672%','%3673%','%3674%'
		]
		provloc = '106.143949, -6.460788'
		mapzoom = '9'
		kabkotcord = [
		'105.755996, -6.673431',
		'106.200032, -6.630999',
		'105.755996, -6.673431',
		'106.163997, -6.110311',
		'106.652091, -6.201259',
		'106.010346, -6.003815',
		'106.163997, -6.110311',
		'106.710786, -6.281848'
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