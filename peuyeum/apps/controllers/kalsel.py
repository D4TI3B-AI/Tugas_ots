import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'kalsel'
		provloc = '115.411328, -2.914826'
		mapzoom = '8'
		kabkotcord = [
		'114.746151, -3.87518',
		'115.946248, -3.000615',
		'114.993114, -3.321817',
		'114.660896, -3.065219',
		'115.046361, -2.916234',
		'115.236989, -2.768951',
		'115.525051, -2.617050',
		'115.189187, -2.443547',
		'115.575024, -1.870056',
		'115.568143, -3.451090',
		'115.615610, -2.326337',
		'114.590072, -3.316572',#71
		'114.749540, -3.465992'
		]
		listkabkot = [
		'%6301%','%6302%','%6303%','%6304%','%6305%','%6306%','%6307%','%6308%','%6309%','%6310%',
		'%6311%',
		'%6371%','%6372%'
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