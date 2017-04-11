import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'papua'
		provloc = '135.220428, -5.231223'
		mapzoom = '7'
		kabkotcord = [
		'139.041312, -7.783833',
		'138.799512, -4.000448',
		'139.854727, -2.987923',
		'135.501625, -3.372225',
		'136.170901, -1.746936',
		'135.980085, -1.038102',
		'136.362469, -3.787644',
		'137.159507, -4.078728',
		'136.4922, -4.722688'


		'140.3481835, -5.7400018',
		'139.6911374, -6.7606468',
		'138.3988186, -5.0573958',
		'139.5279996, -4.4939717',
		'140.5135589, -4.5589872',
		'138.4787258, -3.481132',
		'139.2030851, -2.4678144',
		'140.7624493, -3.3449536',
		'136.670534, -2.8435717',
		'135.6385125, -0.7295099',

		'137.7637565, -2.5331255',
		'138.2393528, -4.4069496',
		'138.3190276, -3.971033',
		'138.3190276, -2.3745692',
		'139.4466005, -3.7852847',
		'137.6061625, -3.8649098',
		'135.6763443, -4.0454139',
		'136.569279, -3.392247',
		'136.4393054,-4.0974893',
		'140.6689995, -2.5916025'

		]
		listkabkot = [
		'%9401%','%9402%','%9403%','%9404%','%9408%','%9409%','%9410%',
		'%9411%','%9412%','%9413%','%9414%','%9415%','%9416%','%9417%','%9418%','%9419%','%9420%',
		'%9426%','%9427%','%9428%','%9429%','%9430%',
		'%9431%','%9432%','%9434%','%9435%','%9436%'
		'%9471%'
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