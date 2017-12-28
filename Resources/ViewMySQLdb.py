#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

from MySQLdb import connect


class ViewMySQLdb(object):
    """docstring for ViewMySQLdb"""
    def __init__(self):
        super(ViewMySQLdb, self).__init__()
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = '896-8660'
        self.db = 'OTDC_Service'

    def connDB(self):
        return connect(host = self.host,
                       user = self.user,
                       passwd = self.passwd,
                       db = self.db)

    def addInfo(self, arg1, arg2, arg3, arg4, arg5):
        ''' Add information of employee to DB
        @param arg1: str - employee name
        @param arg2: str - id of badge
        @param arg3: str - company
        @param arg4: str - photo name
        @param arg5: str - is active employee or not
        '''
        objDB = self.connDB()
        cur = objDB.cursor()
        cur.execute("INSERT INTO Employees(name, badge, company_id, photo, is_active) VALUES (%s, %s, %s, %s, %s);", (arg1, arg2, arg3, arg4, arg5))
        objDB.commit()
        objDB.close()

    def isDuplo(self, value):
        ''' Check is if duplicate employee
        @param value: str - bambooHR employee id
        '''
        objDB = self.connDB()
        cur = objDB.cursor()
        cur.execute("SELECT * FROM Employees")
        objDB.close()
        for k in cur.fetchall():
            if value in k:
                return True
        return False

    def truncTable(self, arg1):
        ''' Truncate all information of table
        @param arg1: str - table name
        '''
        objDB = self.connDB()
        cur = objDB.cursor()
        cur.execute("TRUNCATE TABLE %s", (arg1, ))
        objDB.commit()
        objDB.close()