import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'aceh'
		listkabkot = [
		'%1101%','%1102%','%1103%','%1104%','%1105%','%1106%','%1107%','%1108%','%1109%','%1110%',
		'%1111%','%1112%','%1113%','%1114%','%1115%','%1116%','%1117%','%1118%',
		'%1171%','%1172%','%1173%','%1174%','%1175%'
		]
		provloc = '96.678095, 4.311709'
		mapzoom = '9'	
		kabkotcord = [
		'96.083322, 2.583622',
		'97.922151, 2.384000',
		'97.402781, 3.190697',
		'97.591161, 3.296859',
		'97.617067, 4.740899',
		'96.854644, 4.495374',
		'96.099236, 4.296590',
		'95.576441, 5.309828',
		'96.022189, 5.018921',
		'96.583919, 5.050867',
		'97.014686, 4.999058',
		'96.960594, 3.850525',
		'97.489652, 3.961822',
		'97.932741, 4.182834',
		'96.551047, 4.217548',
		'95.723980, 4.838457',
		'97.005428, 4.702244',
		'96.243269, 5.054155',
		'95.339173, 5.560588',#71
		'95.3422588, 5.867014',
		'95.342258, 5.867014',
		'97.122396, 5.175647',
		'97.889437, 2.724339'
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