import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'bali'
		listkabkot = [
		'%5101%','%5102%','%5103%','%5104%','%5105%','%5106%','%5107%','%5108%',
		'%5171%'
		]
		provloc = '115.184055, -8.425745'
		mapzoom = '9'
		kabkotcord = [
		'114.701385, -8.295495',
		'115.055052, -8.435786',
		'115.178503, -8.534605',
		'115.323008, -8.230679',
		'115.542554, -8.719174',
		'115.354594, -8.454195',
		'115.570658, -8.382352',
		'114.958329, -8.227131',
		'115.211556, -8.669962'
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