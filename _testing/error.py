class Error:
	def __init__(self, error):
		self.error = error
		self.errorList = [990, 1000, 1001, 1002, 1010, 1021, 1030]

	def errorDatabase(self):
		if self.error == 990:
			return 'Error to grab time'
		elif self.error == 1000:
			return 'Error connect to table of database'
		elif self.error == 1001:
			return 'Error in user or password for access to database'
		elif self.error == 1002:
			return 'Error to connecto database'
		elif self.error == 1010:
			return 'Error to match data in table of database'
		elif self.error == 1020:
			return 'Error found data of badge'
		elif self.error == 1021:
			return 'Fatal error'
		elif self.error == 1030:
			return 'Error to match info in tables'
		return self.error

if 990 in Error(990).errorList:
	print 'sad'
