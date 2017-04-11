import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL,keyuri
from lib.sampeu import getWMTS
from apps.models import calendar
from apps.templates import batik

class Controller(object):
	def home(self,uridt='null'):
		provinsi = 'jabar'
		provloc = '107.543382, -6.919011'
		mapzoom = '9'
		kabkotcord = [
		'106.597066, -5.796648',
		'106.932931, -6.931305',
		'107.146612, -6.815292',
		'107.628391, -6.907193',
		'107.782221, -7.358223',
		'108.223480, -7.370463',
		'108.333012, -7.327543',
		'108.594609, -7.045500',
		'108.578243, -6.736305',
		'108.362311, -6.800160',
		'107.951509, -6.807383',
		'108.146650, -6.436696',
		'107.726287, -6.439268',
		'107.504658, -6.568864',
		'107.477713, -6.275045',
		'106.975437, -6.270206',
		'107.392381, -6.861554',
		'108.515785, -7.606407',
		'106.904683, -6.593036',
		'106.956675, -6.858946',
		'107.570520, -7.116538',
		'108.715400, -6.860310',
		'106.975437, -6.270206',
		'106.852816, -6.392455',
		'107.547988, -6.888430',
		'108.221763, -7.341521', #rf
		'108.534659, -7.371715',
		'107.268667, -6.759950'#88
		]
		listkabkot = [
		'%3201%','%3202%','%3203%','%3204%','%3205%','%3206%','%3207%','%3208%','%3209%','%3210%',
		'%3211%','%3212%','%3213%','%3214%','%3215%','%3216%','%3217%','%3218%'
		'%3271%','%3272%','%3273%','%3274%','%3275%','%3276%','%3277%','%3278%','%3279%','%3288%'
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