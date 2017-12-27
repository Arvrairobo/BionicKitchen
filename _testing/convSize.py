#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

from json import load
from urllib import urlretrieve
from os import listdir, system, remove, getcwd
import os.path
from grabInfo import ViewMySQLdb
from unidecode import unidecode


realPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
photosPath = "/Resources/Texture/Photos/"
jsonPath = "/Resources/Temp/getactiveemployees.json"
tmpPath = "/Resources/Temp/Img/"
#http://vmrelease:1011/api/v1/employee/getactiveemployees

with open(realPath+jsonPath) as jsonData:
    jsonObject = load(jsonData)
    for items in jsonObject['Items']:
        try:
            fullName = unidecode(items[u'FirstName']) + ' ' + unidecode(items[u'LastName'])

            isActive = bool(items[u'IsActive'])
            if isActive:
                isActive = 1
            else:
                isActive = 0

            idEmployee = str(items['BambooHrId'])

            company = 2

            prePhotoUrl = str(items[u'PhotoUrl'])
            tmpPhotoUrl = prePhotoUrl.split("-")
            photoUrl = "-".join([tmpPhotoUrl[0], tmpPhotoUrl[1], tmpPhotoUrl[2], "0.jpg"])
            photoName = (photoUrl[89:99]+"png")
            #progress = urlretrieve(photoUrl, (realPath + tmpPath + photoUrl[89:104]))
            print [fullName, idEmployee, company, photoName, isActive]
            #ViewMySQLdb().addInformation(fullName, idEmployee, company, photoName, isActive)
        except Exception as e:
            print e
'''
remove(photosPath + files)
system('trash-empty')'''

class GetJSON(object):
    """docstring for GetJSON"""
    def __init__(self, arg):
        super(GetJSON, self).__init__()
        self.arg = arg