import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'pabar'
		provloc = '133.164988, -1.337644'
		mapzoom = '9'
		kabkotcord = [
		'132.273454, -2.875830',
		'133.9436788, -3.288406',
		'134.410378, -2.965049',
		'133.272067, -1.872531',
		'133.894963, -0.862420',
		'132.206084, -1.733357',
		'131.299394, -0.882057',
		'130.883917, -1.035028',
		'132.408301, -0.649349',
		'132.293779, -1.286889',
		'133.981714, -0.902818',
		'134.062079, -0.863680',
		'131.312243, 0.885879'

		'131.255.828, -0.876163'
		]
		listkabkot = [
		'%9101%','%9102%','%9103%','%9104%','%9105%','%9106%','%9107%','%9108%','%9109%','%9110%',
		'%9111%','%9112%',
		'%9171%'
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