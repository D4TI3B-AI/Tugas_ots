import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'kalbar'
		provloc = '110.744972, -0.106978'
		mapzoom = '9'
		kabkotcord = [
		'109.295939, 1.342138',
		'109.530715, 0.970699',
		'109.583605, 0.477897',
		'109.34734, -0.024408',
		'110.57515, 0.17518',
		'109.990429, -1.824806',
		'111.462683, 0.120501',
		'112.623024, 0.784983',
		'110.870048, 0.007041',
		'111.693579, -0.707734',
		'110.009022, -1.053846',
		'109.47712, -0.4197',
		'109.345623, -0.025095', #71
		'108.974741, 0.910971'
		]
		listkabkot = [
		'%6101%','%6102%','%6103%','%6104%','%6105%','%6106%','%6107%','%6108%','%6109%','%6110%',
		'%6111%','%6112%',
		'%6171%','%6172%'
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