#!/usr/bin/python3
# coding=utf-8
#红外避障系统

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#a,b,c分别对应左中右三个传感器的输出脚
#a
a_pin = 38
b_pin = 40
c_pin = 32

GPIO.setup(a_pin,GPIO.IN,pull_up_down=1)

while True:
    time.sleep(0.2)
    print("------")
    print(GPIO.input(a_pin))
    break

GPIO.cleanup([a_pin,b_pin,c_pin])