#!/usr/bin/python2.7
# -*- coding: utf8 -*-

class ViewMySQLdb:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = "896-8660"
        self.db = "OTDC_Service"

    def connection(self):
        import MySQLdb
        self.db = MySQLdb.connect(host = self.host,
                                  user = self.user,
                                  passwd = self.passwd,
                                  db = self.db)
        return self.db

def catchResult(badge):
    from datetime import datetime


    vipList = ["5300C84782"]
    try:
        currentDay = str(datetime.now()).split()[0]
    except Exception as e:
        # Put error into log
        return "100000"
    try:
        db = ViewMySQLdb().connection()
    except Exception as e:
        # Put error into log
        if e[0] == 1049:
            return "110000"
        elif e[0] == 1045:
            return "110010"
        else:
            return "110020"
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM Current_menu JOIN Employees, Company WHERE Current_menu.employee_id=Employees.employee_id AND Current_menu.company_id=Company.company_id")
    except:
        # Put error into log
        return "120000"
    try:
        for row in cur.fetchall():
            if row[8] == badge:
                if str(row[4]).split()[0] == currentDay:
                    db.close()
                    return row
            elif badge in vipList:
                cur.execute("SELECT * FROM Employees JOIN Company WHERE Employees.company_id=Company.company_id AND badge=%s;", (badge, ))
                for vip in cur.fetchall():
                    return vip
        if badge not in vipList:
            cur.execute("SELECT * FROM Employees JOIN Company WHERE Employees.company_id=Company.company_id AND badge=%s;", (badge, ))
            for noVip in cur.fetchall():
                y = []
                for x in noVip:
                    y.append(x)
                y.append("0x0")
                return y
        db.close()
        if badge == "DEFCONMODE":
            # Put error into log
            return "130000"
        # Put error into log
        return "130010"
    except:
        # Put error into log
        return "140000"

def updateStatus(row):
    try:
        db = ViewMySQLdb().connection()
    except Exception as e:
        # Put error into log
        if e[0] == 1049:
            return "110000"
        elif e[0] == 1045:
            return "110010"
        else:
            return "110020"
    try:
        cur = db.cursor()
        served = cur.execute("UPDATE Current_menu SET served='1' WHERE menu_id=%s;", (row[0], ))
        cur.execute("UPDATE Current_menu SET date=NOW() WHERE menu_id=%s;", (row[0], ))
        db.commit()
        db.close()
        return served
    except:
        # Put error into log
        return "150000"

def viewStatus(badge):
    from datetime import datetime
    try:
        currentDay = str(datetime.now()).split()[0]
    except Exception as e:
        # Put error into log
        return "100000"
    try:
        db = ViewMySQLdb().connection()
    except Exception as e:
        # Put error into log
        if e[0] == 1049:
            return "110000"
        elif e[0] == 1045:
            return "110010"
        else:
            return "110020"
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM Current_menu JOIN Employees, Company WHERE Current_menu.employee_id=Employees.employee_id AND Current_menu.company_id=Company.company_id")
        for row in cur.fetchall():
            if row[8] == badge:
                if str(row[4]).split()[0] == currentDay:
                    db.close()
                    return row[5]
    except Exception as e:
        # Put error into log
        return "120000"