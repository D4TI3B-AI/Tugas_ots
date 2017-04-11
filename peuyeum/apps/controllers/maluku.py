import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'maluku'
		provloc = '130.106357, -3.230494'
		mapzoom = '9'
		kabkotcord = [
		'131.434049, -7.567118',
		'132.732840, -5.773130',
		'129.367758, -3.105895',
		'126.79293683,-3.3927754',
		'134.55423686,-6.19034625',
		'128.4008357,-3.1271575',
		'130.2271243,-3.4233267',
		'126.3498097,126.-7.7851588',
		'126.6957216,-3.7273972',
		'128.19883329,-3.64745861',#71
		'1144087,132.34292329,-5.56769'
		]
		listkabkot = [
		'%8101%','%8102%','%8103%','%8104%','%8105%','%8106%','%8107%','%8108%','%8109%',
		'%8171%','%8172%'
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