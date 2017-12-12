#!/usr/bin/python2.7
# -*- coding: utf8 -*-

class ViewMySQLdb:
	def __init__(self):
		self.host = 'localhost'
		self.user = 'root'
		self.passwd = '896-8660'
		self.db = 'OTDC_Service'

	def connectionDatabase(self):
		from MySQLdb import connect
		self.db = connect(host = self.host,
						  user = self.user,
						  passwd = self.passwd,
						  db = self.db)
		return self.db

	def singleSelectInformation(self, arg1):
		''' arg1
		'''
		self.cur = self.connectionDatabase().cursor()
		self.cur.execute("SELECT * FROM %s"%arg1)
		return self.cur.fetchall()

	def multipleSelectInformation(self, selector, arg1, arg2, arg3, arg4, arg5, arg6):
		''' selector is the option to choose, if is 1 you use 'WHERE',
			if is 2 you use 'JOIN & WHERE' and if is 3 you use 'JOIN, WHERE & AND'
			arg1
			arg2
			arg3
		'''
		if selector == 1:
			self.cur.execute("SELECT * FROM %s WHERE %s=%s;", (arg1, arg3, arg4, ))
		elif selector == 2:
			self.cur.execute("SELECT * FROM %s JOIN %s WHERE %s=%s;", (arg1, arg2, arg3, arg4, ))
		elif selector == 3:
			self.cur.execute("SELECT * FROM %s JOIN %s WHERE %s=%s AND %s=%s;", (arg1, arg2, arg3, arg4, arg5, arg6, ))
		return self.cur.fetchall()

	def addInformation(self, arg1, arg2, arg3, arg4, arg5):
		''' arg1 is employee name
			arg2 is id of badge
			arg3 is company
			arg4 is photo name
			arg5 is if is active employee or not
		'''
		self.cur = self.connectionDatabase().cursor()
		self.cur.execute("INSERT INTO Employees(name, badge, company_id, photo, is_active) VALUES (%s, %s, %s, %s, %s);", (arg1, arg2, arg3, arg4, arg5))
		self.db.commit()
		self.db.close()

	def updateInformation(self, arg1, arg2, arg3, arg4, arg5):
		''' arg1
			arg2
			arg3
			arg4
			arg5
		'''
		self.cur.execute("UPDATE %s SET %s=%s WHERE %s=%s;", (arg1, arg2, arg3, arg4, arg5, ))
		self.db.commit()
		self.db.close()

	def truncateTable(self, arg1):
		'''arg1 is name of table'''
		self.cur.execute("TRUNCATE TABLE %s;", (arg1, ))
		self.db.commit()
		self.db.close()
