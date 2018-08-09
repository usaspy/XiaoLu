#!/usr/bin/python3
# coding=utf-8
'''
红外避障系统
1.启动扫描，当探测到障碍时，将X_scan设置为0,没有障碍时设置为1
2. a,b,c,d分别代表从左向右数第一、二、三、四个探头
'''

import RPi.GPIO as GPIO
import time
tmp = ""
#周边扫描数据，默认1111代表无障碍
a_scan = 1
b_scan = 1
c_scan = 1
d_scan = 1

#对应4个传感器的输出脚
a_pin = 32
b_pin = 36
c_pin = 38
d_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup([a_pin,b_pin,c_pin,d_pin],GPIO.IN,pull_up_down=GPIO.PUD_UP)

def edge_change(pin):
    global  a_scan,b_scan,c_scan,d_scan
    global tmp
    if pin == a_pin:
        a_scan = GPIO.input(pin)
    if pin == b_pin:
        b_scan = GPIO.input(pin)
    if pin == c_pin:
        c_scan = GPIO.input(pin)
    if pin == d_pin:
        d_scan = GPIO.input(pin)

    __1553b_set(tmp,a_scan, b_scan, c_scan, d_scan)

#往1553B数据总线发送数据
def __1553b_set(_1553b,a_scan, b_scan, c_scan, d_scan):
    data = {}
    data['send'] = 0x02
    data['to'] = 0x01
    data['mode'] = 1
    data['priority'] = 1
    data['timestamp'] = time.time()
    data['data'] = [a_scan, b_scan, c_scan, d_scan]
    _1553b['0x02_0x01'] = data

    data['send'] = 0x02
    data['to'] = 0x04
    data['mode'] = 1
    data['priority'] = 1
    data['timestamp'] = time.time()
    data['data'] = [a_scan, b_scan, c_scan, d_scan]
    _1553b['0x02_0x04'] = data


#启动红外避障系统，实时刷新环境状态
#四个监听器，实时报告该方向是否有障碍
def scan(_1553b):
    global tmp
    tmp = _1553b
    GPIO.add_event_detect(a_pin,GPIO.BOTH,callback=edge_change,bouncetime=50)
    GPIO.add_event_detect(b_pin,GPIO.BOTH,callback=edge_change,bouncetime=50)
    GPIO.add_event_detect(c_pin,GPIO.BOTH,callback=edge_change,bouncetime=50)
    GPIO.add_event_detect(d_pin,GPIO.BOTH,callback=edge_change,bouncetime=50)
    while True:
        time.sleep(1)

def stopWork():
    GPIO.cleanup([a_pin,b_pin,c_pin,d_pin])


if __name__ == '__main__':
    scan('zhang')