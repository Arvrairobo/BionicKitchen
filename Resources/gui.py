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
import sys

from arrangedInfo import OnScreen
from grabInfo import catchResult, updateStatus, viewStatus
from rfid import throwInData
from toXLSX import convertXLSX


Builder.load_file("design.kv")

class MainScreen(Screen):
    def __init__(self, **kwargs): # For avoid the black images
        super(MainScreen, self).__init__(**kwargs)

    source_photo = StringProperty(None)
    source_photo = "Texture/Photos/00000-0-0.png"
    source_company = StringProperty(None)
    source_ib = StringProperty(None)
    source_ib = "Texture/Interactive_background_2.png"

    def update_data(self, sec):
        if GPIO.input(17):
            badgeData = throwInData()
            self.badge = catchResult(badgeData)
            self.employee.text = OnScreen(self.badge).joinAll()[2]
            self.dish.text = OnScreen(self.badge).joinAll()[1]
            self.dishid.text = OnScreen(self.badge).joinAll()[0]
            self.photo.source = OnScreen(self.badge).joinAll()[5]
            self.company.source = OnScreen(self.badge).joinAll()[3]
            self.ib.source = OnScreen(self.badge).joinAll()[4]
            self.status = viewStatus(badgeData)
        elif GPIO.input(27):
            try:
                if self.status == "0":
                    updateStatus(self.badge)
                    self.dishid.text = "Status: Served"
            except Exception as e:
                # Put error into log
                pass
        elif GPIO.input(22):
            convertXLSX() # Put error into log
            sys.exit()

class MyScreenManager(ScreenManager):
    pass

class ScreenManagerApp(App):
    def build(self):
        sm = ScreenManager()
        self.first_screen = MainScreen(name = "first")
        sm.add_widget(self.first_screen)
        return sm

    def on_start(self):
        Clock.schedule_interval(self.first_screen.update_data, 0.01) # 0.01 second

if __name__ == "__main__":
    ScreenManagerApp().run()