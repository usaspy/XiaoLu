#!/usr/bin/python3
# coding=utf-8
#红外避障系统
'''


'''

import RPi.GPIO as GPIO
import time

#周边扫描数据，默认1111代表无障碍
a_scan = 1
b_scan = 1
c_scan = 1
d_scan = 1

GPIO.setmode(GPIO.BOARD)

#a,b,c分别对应4个传感器的输出脚
#a
a_pin = 32
b_pin = 36
c_pin = 38
d_pin = 40

GPIO.setup([a_pin,b_pin,c_pin,d_pin],GPIO.IN,pull_up_down=GPIO.PUD_UP)

def a_change(a_pin):
    print("1111")
#
def scan(dd):
    GPIO.add_event_detect(a_pin,GPIO.BOTH,callback=a_change)
    print("stooo")

def stopWork():
    GPIO.cleanup([a_pin,b_pin,c_pin,d_pin])