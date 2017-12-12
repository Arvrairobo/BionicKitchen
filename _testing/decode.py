#!/usr/bin/python2.7
# -*- encoding: utf-8 -*-

def _to_ascii(s):
	if isinstance(s, str):
		return s.encode('ascii')
	else:
		return s

#print(unicode('Yanko Gabriel  Navarro López', errors = 'replace'))
#print(ord('Yanko Gabriel  Navarro López'))

s = u'Yanko Gabriel Navarro López'

#u = 'ó'
s.encode('utf-8')
print(type(s))
#print(ord(u[-1]))
