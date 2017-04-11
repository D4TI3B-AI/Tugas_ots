import sys
import MySQLdb
import time
sys.path.append('../../')
from lib import config


class Calendar():
	def __init__(self):
		self.conn = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpassword,config.mysqldb)
		self.db = self.conn.cursor()

	def getCountKabKot(self,id_prov,id_kabkot):
		countline = self.db.execute("select calendardata from oc_clndr_objects where calendardata like '%LOCATION:"+str(id_prov)+"|"+str(id_kabkot)+"%'")
		return str(countline)
	
	def getYearCountKabKot(self,id_prov,id_kabkot,year):
		countline = self.db.execute("select calendardata from oc_clndr_objects where YEAR(startdate) = '"+str(year)+"' AND calendardata like '%LOCATION:"+str(id_prov)+"|"+str(id_kabkot)+"%'")
		return str(countline)

	def getCountProv(self,id_prov):
		countline = self.db.execute("select calendardata from oc_clndr_objects where calendardata like '%LOCATION:"+str(id_prov)+"%'")
		return str(countline)
	
	def getYearCountProv(self,id_prov,year):
		countline = self.db.execute("select calendardata from oc_clndr_objects where YEAR(startdate) = '"+str(year)+"' AND calendardata like '%LOCATION:"+str(id_prov)+"%'")
		return str(countline)
		
	def getAllDataKabkot(self,id_prov,id_kabkot):
		self.db.execute("select calendardata from oc_clndr_objects where calendardata like '%LOCATION:"+str(id_prov)+"|"+str(id_kabkot)+"%'")
		return self.db.fetchall()
		
	def getYearAllDataKabKot(self,id_prov,id_kabkot,year):
		self.db.execute("select calendardata from oc_clndr_objects where YEAR(startdate) = '"+str(year)+"' AND calendardata like '%LOCATION:"+str(id_prov)+"|"+str(id_kabkot)+"%'")
		return self.db.fetchall()

	def getAllDataProv(self,id_prov):
		self.db.execute("select calendardata from oc_clndr_objects where calendardata like '%LOCATION:"+str(id_prov)+"%'")
		return self.db.fetchall()
	
	def getListAgenda(self,kabkotno):
		self.db
	
	def close(self):
		self.conn.close()