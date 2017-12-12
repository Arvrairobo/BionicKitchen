#!/usr/bin/python2.7
# -*- coding: utf8 -*-

class Error:
	def __init__(self, error):
		self.error = error
		self.errorList = ['100000', '110000', '110010', '110020', '120000', '130000', '130010', '140000', '150000']

	def errorDatabase(self):
		if int(self.error) == 100000:
			return 'Error to grab time'
		elif int(self.error) == 110000:
			return 'Error connect to table of database'
		elif int(self.error) == 110010:
			return 'Error in user or password for access to database'
		elif int(self.error) == 110020:
			return 'Error to connect database'
		elif int(self.error) == 120000:
			return 'Error to match data in table of database'
		elif int(self.error) == 130000:
			return 'Error found data of badge'
		elif int(self.error) == 130010:
			return 'Error to found data of badge in database'
		elif int(self.error) == 140000:
			return 'Error to match info in tables'
		elif int(self.error) == 150000:
			return 'Error to submit and update info to log service'
		return self.error
