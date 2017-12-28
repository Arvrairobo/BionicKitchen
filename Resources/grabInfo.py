#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import os
from datetime import datetime
from createLog import logFile
from ViewMySQLdb import ViewMySQLdb


def catchResult(badge):
    vipList = ["5300C84782"]
    try:
        currentDay = str(datetime.now()).split()[0]
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
        return "100000"
    try:
        db = ViewMySQLdb().connDB()
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
        if e[0] == 1049:
            return "110000"
        elif e[0] == 1045:
            return "110010"
        else:
            return "110020"
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM Current_menu JOIN Employees, Company WHERE Current_menu.employee_id=Employees.employee_id AND Current_menu.company_id=Company.company_id")
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
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
            return "130000"
        return "130010"
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
        return "140000"

def updateStatus(row):
    try:
        db = ViewMySQLdb().connDB()
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
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
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
        return "150000"

def viewStatus(badge):
    try:
        currentDay = str(datetime.now()).split()[0]
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
        return "100000"
    try:
        db = ViewMySQLdb().connDB()
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
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
        logFile(str(e)+" in "+os.path.basename(__file__))
        return "120000"