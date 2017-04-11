import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'lampung'
		provloc = '105.248220, -5.295055'
		mapzoom = '9'
		kabkotcord = [
		'104.187577, -5.037602',
		'104.589094, -5.271250',
		'105.530334, -5.537350',
		'105.591926, -5.131215',
		'105.388058, -4.739790',
		'104.803865, -4.760434',
		'104.570260, -4.482889',
		'105.420658, -4.351302',
		'105.148091, -5.477959',
		'104.924224, -5.352675',
		'105.429819, -3.990466',
		'105.115601, -4.315114',
		'104.046358, -5.259768',
		'105.264212, -5.399865',#71
		'105.307924, -5.118348',
		'103.922607, -4.932111'
		]
		listkabkot = [
		'%1801%','%1802%','%1803%','%1804%','%1805%','%1806%','%1807%','%1808%','%1809%','%1810%',
		'%1811%','%1812%','%1813%',
		'%1871%','%1872%','%1888%'
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