import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'sumsel'
		provloc = '104.669016, -2.929209'
		mapzoom = '9'
		kabkotcord = [
		'104.087209, -4.009096',
		'105.501869, -3.206483',
		'104.022245, -3.557060',
		'103.544024, -3.783793',
		'103.246193, -3.128424',
		'103.816464, -2.471016',
		'104.750518, -2.634553',
		'103.944993, -4.577229',
		'104.598882, -4.018469',
		'104.668482, -3.355188',
		'102.945043, -3.712889',
		'104.010016, -3.208364',
		'102.785429, -2.766428',
		'104.759871, -2.974852',
		'104.243034, -3.420755',
		'103.234160, -4.042535',
		'102.859608, -3.299299',
		'103.907185, -4.831922'
		]
		listkabkot = [
		'%1601%','%1602%','%1603%','%1604%','%1605%','%1606%','%1607%','%1608%','%1609%','%1610%',
		'%1611%','%1612%','%1613%',
		'%1671%','%1672%','%1673%','%1674%','%1688%'
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