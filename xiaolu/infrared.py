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

#a,b,c,d分别对应4个传感器的输出脚
a_pin = 32
b_pin = 36
c_pin = 38
d_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup([a_pin,b_pin,c_pin,d_pin],GPIO.IN,pull_up_down=GPIO.PUD_UP)

def edge_change(pin):
    if pin == a_pin:
        a_scan = GPIO.input(pin)
    if pin == b_pin:
        b_scan = GPIO.input(pin)
    if pin == c_pin:
        c_scan = GPIO.input(pin)
    if pin == d_pin:
        d_scan = GPIO.input(pin)

#启动红外避障系统，实时刷新环境状态
def scan(dd):
    GPIO.add_event_detect(a_pin,GPIO.BOTH,callback=edge_change,bouncetime=100)
    GPIO.add_event_detect(b_pin,GPIO.BOTH,callback=edge_change,bouncetime=100)
    GPIO.add_event_detect(c_pin,GPIO.BOTH,callback=edge_change,bouncetime=100)
    GPIO.add_event_detect(d_pin,GPIO.BOTH,callback=edge_change,bouncetime=100)
    while True:
        print(a_pin,b_pin,c_pin,d_pin)
        time.sleep(10)


def stopWork():
    GPIO.cleanup([a_pin,b_pin,c_pin,d_pin])


if __name__ == '__main__':
    scan('zhang')