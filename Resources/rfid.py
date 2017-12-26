#!/usr/bin/python2.7
# -*- coding: utf8 -*-

def scannerBadge():
    from serial import Serial


    try:
        port = Serial('/dev/ttyUSB0', 2400, timeout = None)
        port.flushInput()
        badge = port.readlines(10)[1].strip()
        port.flushOutput()
        port.close()
        return badge
    except:
        return 'DEFCONMODE'