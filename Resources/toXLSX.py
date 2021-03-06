#!/usr/bin/python2.7
# -*- coding: utf8 -*-

def convertXLSX():
    import os
    import shutil
    from xlsxwriter import Workbook
    from datetime import datetime
    from ViewMySQLdb import ViewMySQLdb
    from createLog import logFile


    realPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    tmpPath = "/Resources/Temp/"
    nowIs = str(datetime.now()).split()[0]
    try:
        db = ViewMySQLdb().connDB()
        cur = db.cursor()
        cur.execute("SELECT * FROM Current_menu JOIN Employees, Company WHERE Current_menu.employee_id=Employees.employee_id AND Current_menu.company_id=Company.company_id AND SUBSTR(Current_menu.date,1,10)=%s", (nowIs, ))
        rawData = cur.fetchall()
        if rawData:
            workbook = Workbook(realPath+tmpPath+"Current_menu.xlsx")
            worksheet = workbook.add_worksheet(nowIs)
            worksheet.set_column('A:E', 40)
            cellFormat = workbook.add_format({'valign': 'center',
                                              'fg_color': '#D7E4BC',
                                              'border': 1})

            data = []
            for row in rawData:
                arrangedData = [row[7]] + [row[13]] + [row[2]] + [str(row[4])] + [row[5]]
                data.append(arrangedData)

            worksheet.add_table('A1:E1000', {'data': data,
                                             'columns': [{'header': 'Name', 'format':cellFormat},
                                                         {'header': 'Company', 'format':cellFormat},
                                                         {'header': 'Dish', 'format':cellFormat},
                                                         {'header': 'Date', 'format':cellFormat},
                                                         {'header': 'Status', 'format':cellFormat},
                                                         ]})
            workbook.close()
            db.close()
            shutil.copy(realPath+tmpPath+"Current_menu.xlsx",
                        realPath+tmpPath+"Service Control/Current_menu.xlsx")
            os.rename(realPath+tmpPath+"Service Control/Current_menu.xlsx",
                      realPath+tmpPath+"Service Control/{0}.xlsx".format(nowIs))
        else:
            return "Error to read information from database!"
    except Exception as e:
        logFile(str(e)+" in "+os.path.basename(__file__))
        return "Fatal Error"