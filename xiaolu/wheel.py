#!/usr/bin/python3
# coding=utf-8
'''
行走子系统
具备下列功能：
 1.程序启动以后，行走系统初始化完成，等待红外遥控的指令
 2.接收到红外遥控发来的启动命令FLAG=Start，行走系统进入自动运行状态,FLAG=Stop，行走系统回到初始化完成状态
 3.每0.2秒从探头获取当前的避障数据（数据格式：1110,0100），并根据其进行行走控制。
'''
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

in1 =29
in2 = 31
in3 =33
in4 = 35
#enda = 40
endb = 37

def fire():
    GPIO.setup(in1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(in2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(in3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(in4,GPIO.OUT,initial=GPIO.LOW)
   # GPIO.setup(enda,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(endb,GPIO.OUT,initial=GPIO.HIGH)

def misfire():
    GPIO.cleanup([in1, in2, in3, in4, endb])

def __left_backaway():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

def __left_forward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)

def __left_stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

def __right_backaway():
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def __right_forward():
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def __right_stop():
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

def forward():
    __left_forward()
    __right_forward()

def backaway():
    __left_backaway()
    __right_backaway()

def turn_left():
    __left_backaway()
    __right_forward()

def turn_right():
    __left_forward()
    __right_backaway()

def stop():
    __left_stop()
    __right_stop()


def standby(dd):
    fire()
    stop()
    time.sleep(3)
    misfire()