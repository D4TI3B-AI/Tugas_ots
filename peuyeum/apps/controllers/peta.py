import sys
import os
from datetime import datetime
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		try :
			uridt = int(uridt)
		except ValueError:
			uridt = datetime.now().year
		uridt = str(uridt)
		provcord=[
		'97.157133, 4.408571','99.024808, 2.039450','100.562894, -0.706683','101.683500, 0.336998','102.595365, -1.618351','103.990629, -3.275716','102.3268839, -3.6343766','105.188138, -4.886557','107.110746, -2.771050','104.232328, 1.056545',
		'106.842041, -6.198240','107.594144, -6.891804','109.945218, -7.284288','110.384671, -7.828832','112.351224, -7.698205','106.143949, -6.460788','115.184055, -8.425745','117.430759, -8.675622','121.199070, -8.681052','111.421238, -0.241252',
		'113.376804, -1.713165','115.200535, -3.096190','116.365086, 0.659612','116.584812, 3.491935','123.616062, 0.725525','121.506687, -1.493524','120.100437, -3.600696','121.880222, -3.644554','122.443724, 0.717559','119.389525, -2.739325',
		'129.804564, -3.178191','127.695189, 1.631968','133.252734, -1.337635','138.141650, -4.261678'
		]
		listprov=[
		'aceh','sumut','sumbar','riau','jambi','sumsel','bengkulu','lampung','babel','kepri',
		'jakarta','jabar','jateng','yogya','jatim','banten','bali','ntb','ntt','kalbar',
		'kalteng','kalsel','kaltim','kaltara','sulut','sulteng','sulsel','sultra','gorontalo','sulbar',
		'maluku','malut','pabar','papua'
		]
		listkodeprov=[
		'%11%','%12%','%13%','%14%','%15%','%16%','%17%','%18%','%19%','%21%',
		'%31%','%32%','%33%','%34%','%35%','%36%','%51%','%52%','%53%','%61%',
		'%62%','%63%','%64%','%65%','%71%','%72%','%73%','%74%','%75%','%76%',
		'%81%','%82%','%91%','%94%'
		]
		petaloc = '118.015776, -2.6000285'
		mapzoom = '5'
		periode = uridt
		batik.nasional('peta',listkodeprov,petaloc,mapzoom,provcord)
		cal = calendar.Calendar()
		dt = {}
		for namaprov,kodeprov in zip(listprov,listkodeprov):
			dt[kodeprov]=cal.getYearCountProv(kodeprov[1:3],uridt)
			dt[kodeprov[:3]+' uri%'] = urlEncode16(keyuri+'%'+namaprov+'%home%'+periode)
		cal.close()
		dt['%WMTS%']=getWMTS()
		dt['%PERIODE%']=uridt
		dt['%LAMAN INDONESIA%']=urlEncode16(keyuri+'%peta%home'+'%'+uridt)
		dt['%TAHUN SEBELUMNYA%']=urlEncode16(keyuri+'%peta%home'+'%'+str(int(uridt)-1))
		dt['%TAHUN SETELAHNYA%']=urlEncode16(keyuri+'%peta%home'+'%'+str(int(uridt)+1))
		return dt