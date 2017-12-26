#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
from subprocess import call


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.wait_for_edge(3, GPIO.FALLING)

call(['shutdown', '-h', 'now'], shell=False)