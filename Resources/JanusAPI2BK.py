#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

import os.path as osp
from json import load as jload
from urllib import urlretrieve as urllibret
from os import listdir, system, remove, getcwd
from unidecode import unidecode as uni
from ViewMySQLdb import ViewMySQLdb as db


#http://vmrelease:1011/api/v1/employee/getactiveemployees
class JanusAPI2BK(object):
    """docstring for JanusAPI2BK"""
    def __init__(self):
        super(JanusAPI2BK, self).__init__()
        self.realPath = osp.dirname(osp.dirname(osp.realpath(__file__)))
        self.photosPath = "/Resources/Texture/Photos/"
        self.jsonPath = "/Resources/Temp/getactiveemployees.json"
        self.tmpPath = "/Resources/Temp/Img/"
        self.imageEditorPath = "/Resources/imageEditor.py"
        self.photoFormat = ".png"

    def __del__(self):
        #remove(realPath+photosPath+files)
        system("trash-empty")

    def objJSON(self, objIter):
        ''' This method get a object of JSON
        @param objIter: str - object name to iter
        '''
        with open(self.realPath+self.jsonPath) as jsonData:
            jsonObject = jload(jsonData)
            return jsonObject[objIter]

    def lenObjJSON(self):
        return len(self.objJSON("Items"))

    def getEmployeeName(self, num):
        ''' This method get a employee name
        @param num: int - is a current employee
        '''
        objEmployee = self.objJSON("Items")[num]
        return "{0} {1}".format(uni(objEmployee[u"FirstName"]),
                                uni(objEmployee[u"LastName"]))

    def getBambooHrId(self, num):
        ''' This method get a employee bamboohr id
        @param num: int - is a current employee
        '''
        objEmployee = self.objJSON("Items")[num]
        return str(objEmployee[u"BambooHrId"])

    def getPhotoURL(self, num):
        ''' This method get a url of employee photo in .jpg
        @param num: int - is a current employee
        '''
        objEmployee = self.objJSON("Items")[num]
        return str(objEmployee[u"PhotoUrl"]).split("1.jpg")[0]+"0.jpg"

    def getPhotoName(self, url):
        ''' This method get a photo name of employee in .png
        @param url: str - url of employee photo
        '''
        return url.split("/photos/")[1].split(".")[0]+self.photoFormat

    def downloadPhotos(self, url):
        ''' This method download a photo of employee in .jpg
        @param url: str - url of employee photo
        '''
        urllibret(url, (self.realPath+self.tmpPath+url[89:104]))

    def prepare2DB(self, num):
        ''' This method get ready all employee data in a list
        @param num: int - is a current employee
        '''
        return [self.getBambooHrId(num),
                self.getEmployeeName(num),
                self.getBambooHrId(num),
                "2",
                self.getPhotoName(self.getPhotoURL(num)),
                "1"]

    def push2DB(self):
        count = 0
        while(count < self.lenObjJSON()):
            url = self.getPhotoURL(count)
            toVerf = self.getBambooHrId(count)
            if not db.isDuplo(toVerf):
                db.addInfo(self.prepare2DB(count))
            self.downloadPhotos(url)
            count+=1
        system("find {0}/ -regex .*jpg | xargs python2.7 {1}".format(self.realPath, (self.realPath+self.imageEditorPath)))

if __name__ == '__main__':
    obj = JanusAPI2BK()
    obj.push2DB()
    del obj