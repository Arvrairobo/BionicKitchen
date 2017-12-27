#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

from json import load
from urllib import urlretrieve
from os import listdir, system, remove, getcwd
from os.path import isfile, join, basename, dirname, realpath
from grabInfo import ViewMySQLdb
from unidecode import unidecode


realPath = dirname(dirname(realpath(__file__)))
photosPath = "/Resources/Texture/Photos/"
jsonPath = "/Resources/Temp/getactiveemployees.json"
tmpPath = "./img/"
#http://vmrelease:1011/api/v1/employee/getactiveemployees

with open(realPath+jsonPath) as jsonData:
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

            company = "2"

            photoUrl = str(items[u'PhotoUrl'])
            tmpPhotoUrl = photoUrl.split("-")
            if namePhotoUrl.split("-")[2] == "1":
                setPhotoUrl = tmpPhotoUrl[0]+"-" +tmpPhotoUrl[1] +"-0-1.jpg"
            else:
                setPhotoUrl = photoUrl
            progress = urlretrieve(setPhotoUrl, (tmpPath + photoUrl[89:104]))
            print [fullName, idEmployee, company, setPhotoUrl, isActive]
            #ViewMySQLdb().addInformation(fullName, idEmployee, company, namePhotoUrl, isActive)
        except Exception as e:
            print e
'''
for files in listdir(photosPath):
    if isfile(join(photosPath, files)) and files.endswith(".jpg"):
        system('convert {0} -resize 300x300 {1}.png'.format((photosPath + files), (photosPath + files.split('.')[0])))
        remove(photosPath + files)
system('trash-empty')'''

class GetJSON(object):
    """docstring for GetJSON"""
    def __init__(self, arg):
        super(GetJSON, self).__init__()
        self.arg = arg