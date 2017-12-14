#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

from json import load
from urllib import urlretrieve
from os import listdir, system, remove, getcwd
from os.path import isfile, join, basename, dirname, realpath
from grabInfo import ViewMySQLdb
from unidecode import unidecode


photosPath = '../Resources/Texture/Photos/'
#http://vmrelease:1011/api/v1/employee/getactiveemployees

with open('../Resources/GetAllEmployees.json') as jsonData:
	jsonObject = load(jsonData)
	for items in jsonObject['Items']:
		try:
			fullName = unidecode(items[u'FirstName']) + ' ' + unidecode(items[u'LastName'])
			namePhotoUrl = str(items[u'PhotoUrl'][89:104]).split('.')[0] + '.png'

			isActive = bool(items[u'IsActive'])
			if isActive == True:
				isActive = '1'
			else:
				isActive = '0'

			idEmployee = str(items['BambooHrId'])

			company = str(items['Email']).split('@')[1]
			if company == 'pinnacleaerospace.com' or company == 'sonorasoft.com' or company == 'pseinternship.com':
				company = '2'
			else:
				company = '1'

			photoUrl = str(items[u'PhotoUrl'])
			progress = urlretrieve(photoUrl, (photosPath + photoUrl[89:104]))
			ViewMySQLdb().addInformation(fullName, idEmployee, company, namePhotoUrl, isActive)
		except Exception as e:
			print e
			pass

for files in listdir(photosPath):
	if isfile(join(photosPath, files)) and files.endswith(".jpg"):
		system('convert ' + (photosPath + files) + ' -resize 300x300 ' + (photosPath + files.split('.')[0] + '.png'))
		remove(photosPath + files)
system('trash-empty')

class GetJSON(object):
	"""docstring for GetJSON"""
	def __init__(self, arg):
		super(GetJSON, self).__init__()
		self.arg = arg