#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

def logFile(err):
    import time
    import os
    realPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    date = time.strftime("%d/%m/%Y")
    hour = time.strftime("%I:%M:%S")
    document = '/Resources/Temp/Logs/Logs.txt'
    error = hour + ' - ' + err

    log =  open(realPath+document, 'a+')
    if date+'\n' not in log.readlines():
        log.write('\n' + '\n' + date)

    log.write('\n' + error)
    log.close()