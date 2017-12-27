#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import serial


SERIAL_PORT = '/dev/ttyUSB0'  # The location of our serial port.  This may
                              # vary depending on OS and RPi version.  The
#SERIAL_PORT = '/dev/ttyAMA0' # RPi 3 has apparently used 'ttyAMA0' for
                              # Bluetooth and assigned 'ttyS0' to the GPIO
#SERIAL_PORT = '/dev/ttyS0'   # serial port, so uncomment the appropriate
                              # SERIAL_PORT definition for your setup.
                              # Failing that, check the output of:
                              #   $ dmesg | grep serial
                              # to get an idea as to where serial has been
                              # assigned to.

                              
def validateRFID(code):
    # A valid code will be 12 characters long with the first char being
    # a line feed and the last char being a carriage return.
    s = code.decode("ascii")

    if (len(s) == 12) and (s[0] == "\n") and (s[11] == "\r"):
        # We matched a valid code.  Strip off the "\n" and "\r" and just
        # return the RFID code.
        return s[1:-1]
    else:
        # We didn't match a valid code, so return False.
        return False

def throwInData():
    # Set up the serial port as per the Parallax reader's datasheet.
    ser = serial.Serial(baudrate = 2400,
                        bytesize = serial.EIGHTBITS,
                        parity   = serial.PARITY_NONE,
                        port     = SERIAL_PORT,
                        stopbits = serial.STOPBITS_ONE,
                        timeout  = None)

    # Wrap everything in a try block to catch any exceptions.
    try:
        # Read in 12 bytes from the serial port.
        data = ser.read(12)

        # Attempt to validate the data we just read.
        code = validateRFID(data)

        # If validateRFID() returned a code, display it.
        if code:
            return code
    except:
        return "DEFCONMODE"