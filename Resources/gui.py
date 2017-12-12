#!/usr/bin/python2.7
# -*- coding: utf8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.properties import StringProperty

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
from os import system
from time import sleep
import sys

from arrangedInfo import OnScreen
from grabInfo import catchResult, updateStatus, viewStatus
from rfid import scannerBadge
from toXLSX import convertXLSX


Builder.load_file('design.kv')

class MainScreen(Screen):
	source_photo = StringProperty(None)
	source_photo = 'Texture/Photos/00000-0-0.png'
	source_company = StringProperty(None)
	source_ib = StringProperty(None)
	source_ib = 'Texture/Interactive_background_2.png'
	#source_poweroff = StringProperty(None)

	def update_data(self, sec):
		if GPIO.input(17) == True:
			self.badge = catchResult(scannerBadge())
			self.employee.text = OnScreen(self.badge).joinAll()[2]
			self.dish.text = OnScreen(self.badge).joinAll()[1]
			self.dishid.text = OnScreen(self.badge).joinAll()[0]
			self.photo.source = OnScreen(self.badge).joinAll()[5]
			self.company.source = OnScreen(self.badge).joinAll()[3]
			self.ib.source = OnScreen(self.badge).joinAll()[4]
			self.status = viewStatus(scannerBadge())
		elif GPIO.input(27) == True:
			try:
				if self.status == '0':
					print 'last stage'
					print self.employee.text
					updateStatus(self.badge)
					self.dishid.text = 'Status: Served'
			except Exception as e:
				print e
				pass
		elif GPIO.input(22) == True:
			#self.poweroff.source = 'Texture/Interactive_background_2.png'
			convertXLSX()
			#sleep(5)
			sys.exit()

class MyScreenManager(ScreenManager):
	pass

class ScreenManagerApp(App):
	def build(self):
		sm = ScreenManager()
		self.first_screen = MainScreen(name = 'first')
		sm.add_widget(self.first_screen)
		return sm

	def on_start(self):
		Clock.schedule_interval(self.first_screen.update_data, 0.1) # 0.1 second

if __name__ == '__main__':
	ScreenManagerApp().run()
