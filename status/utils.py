import time

import serial
import datetime
import serial.win32


def scan():
    device = 'COM5'
    try:
        arduino = serial.Serial(device, 9600, timeout=5)
        data = arduino.readline()
        if data:
            string = ''
            for i in range(0, 12):
                string = string + chr(data[i])
                string = string.strip()
            return string
    except serial.serialutil.SerialException:
        time.sleep(5)
        arduino = serial.Serial(device, 9600, timeout=10)
        data = arduino.readline()
        if data:
            string = ''
            for i in range(0, 12):
                string = string + chr(data[i])
                string = string.strip()
            return string


def time_now():
    return str(datetime.datetime.now())[:19]