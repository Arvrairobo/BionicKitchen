# -*- coding: utf-8 -*-
#!/usr/bin/python

def log_file (err):
	import time
	#date = time.strftime("%d/%m/%Y")
	date = '30/12/2017'
	hour = time.strftime("%I:%M:%S")
	document = '/home/victor_abad/Desktop/BionicKitchen-master/_testing/LOG.txt'
	error = hour + ' - ' + err


	log =  open(document, 'a+')
	if date+'\n' in log.readlines():
		print 'Day already in the log file'
	else:
		log.write('\n' + '\n' + date)

	log.write('\n' + error)
	log.close()

log_file('D') 