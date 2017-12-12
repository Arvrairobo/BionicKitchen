#!/usr/bin/python2.7
# -*- coding: utf8 -*-

from errorList import Error


class Dish:
	def __init__(self, data):
		try:
			if len(data) == 8: # Verify if is vip
				self.dish = 8
			elif len(data) == 9: # Verify if no order
				self.dish = 9
			elif data in Error(data).errorList: # Verify if is error
				self.dish = data
			elif data[5] == '1': # Verify if is served
				self.dish = 1
			else:
				self.dish = data[2].split() # Verify if is normal employee
		except TypeError:
			if data in Error(data).errorList:
				self.dish = data
			elif data[5] == '1':
				self.dish = 1
			else:
				self.dish = data[2].split()

	def dishName(self):
		if self.dish in Error(self.dish).errorList:
			return '{0}'.format(Error(int(self.dish)).errorDatabase(), )
		elif self.dish == 8:
			return 'Select the dish'
		elif self.dish == 9:
			return 'No order'
		elif self.dish == 1:
			return 'You already served'
		else:
			dishName = ''
			for spliting in self.dish[1:]:
				dishName += '{0} '.format(spliting)
			return dishName[1:-2]

	def dishType(self):
		if self.dish in Error(self.dish).errorList:
			return 'Status: Error {0}'.format(hex(int(self.dish)), )
		elif self.dish == 8:
			return 'Status: VIP'
		elif self.dish == 9:
			return 'Status: No food'
		elif self.dish == 1:
			return 'Status: Served'
		else:
			dishName = ''
			for spliting in self.dish[0:1]:
				dishName += '{0} '.format(spliting)
			return dishName

class Name:
	def __init__(self, data):
		if data in Error(data).errorList:
			self.name = data
		elif len(data) == 8 or len(data) == 9:
			self.name = data[1].split()
		else:
			self.name = data[7].split()

	def firstName(self):
		return self.name[0]

	def lastName(self):
		try:
			if len(self.name) == 4:
				return self.name[2]
			return self.name[1]
		except IndexError:
			return self.name

	def fullName(self):
		return '{0} {1}'.format(self.firstName(), self.lastName())

class Company:
	def __init__(self, data):
		if data in Error(data).errorList:
			self.company = data
		elif len(data) == 8 or len(data) == 9:
			self.company = data[7]
		else:
			self.company = data[13]
	
	def location(self):
		if self.company == 'Pinnacle Aerospace':
			return 'Texture/Logos/PA.png'
		elif self.company == 'Sonora Offshore':
			return 'Texture/Logos/OTSA.png'
		return 'Texture/Logos/OTSA.png'

class InteractiveBackground:
	def __init__(self, data):
		try:
			if data[5] == '1':
				pass
			else:
				self.thing = data[2].split()
		except IndexError:
			pass

	def chooseBackground(self):
		try:
			self.ib = self.thing[0:2][0]

			if self.ib == 'Guiso1':
				return 'Texture/Interactive_background_1.png'
			elif self.ib == 'Guiso2':
				return 'Texture/Interactive_background_2.png'
			elif self.ib == 'Guiso3':
				return 'Texture/Interactive_background_3.png'
			return 'Texture/Interactive_background_4.png'
		except AttributeError:
			return 'Texture/Interactive_background_4.png'

class Photo:
	def __init__(self, data):
		try:
			if len(data) == 8 or len(data) == 9:
				self.photo = data[4]
			else:
				self.photo = data[10]
		except IndexError:
			pass
	
	def location(self):
		try:
			if len(self.photo) <= 1:
				return 'Texture/Photos/00000-0-0.png'
			else:
				return 'Texture/Photos/{0}'.format(self.photo)
			return 'Texture/Photos/00000-0-0.png'
		except:
			return 'Texture/Photos/00000-0-0.png'

class OnScreen:
	def __init__(self, badge):
		self.badge = badge

	def joinAll(self):
		dishType = Dish(self.badge).dishType()
		dishName = Dish(self.badge).dishName()
		name = Name(self.badge).fullName()
		company = Company(self.badge).location()
		background = InteractiveBackground(self.badge).chooseBackground()
		photo = Photo(self.badge).location()
		return [dishType, dishName, name, company, background, photo]
