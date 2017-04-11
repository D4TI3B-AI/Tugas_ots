import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'ntt'
		provloc = '122.044789, -9.679998'
		mapzoom = '7'
		kabkotcord = [
		'119.394054, -9.677304',
		'120.232420, -9.875238',
		'123.606649, -10.177821',
		'124.382450, -9.867609',
		'124.582117, -9.390578',
		'125.047361, -9.113389',
		'124.721194, -8.275054',
		'123.496242, -8.467600',
		'122.815447, -8.359727',
		'122.220342, -8.736092',
		'121.653925, -8.852580',
		'121.039836, -8.576664',
		'120.387238, -8.343910',
		'123.108127, -10.747515',
		'119.831468, -8.583570',
		'119.657199, -9.544262',
		'119.137351, -9.473212',
		'121.301746, -8.603097',
		'120.673915, -8.568518'
		]
		listkabkot = [
		'%5301%','%5302%','%5303%','%5304%','%5305%','%5306%','%5307%','%5308%','%5309%','%5310%',
		'%5311%','%5312%','%5313%','%5314%','%5315%','%5316%','%5317%','%5318%','%5319%','%5320%',
		'%5321%',
		'%5371%'
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