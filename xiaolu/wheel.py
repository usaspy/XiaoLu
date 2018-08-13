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

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#BOARD
#in1 =29
#in2 = 31
#in3 =33
#in4 = 35
#enda = 40
#endb = 37

#BCM
in1 =5
in2 = 6
in3 =13
in4 = 19
#enda = 21
endb = 26

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

def __forward():
    __left_forward()
    __right_forward()

def __backaway():
    __left_backaway()
    __right_backaway()

def __turn_left():
    __left_backaway()
    __right_forward()

def __turn_right():
    __left_forward()
    __right_backaway()

def __stop():
    __left_stop()
    __right_stop()

def action_1111():
    print("1111")
    __forward()

def action_1110():
    print('1110')
    __turn_left()
    time.sleep(0.5)
    __forward()

def action_1100():
    print('1100')
    __turn_left()
    time.sleep(1)
    __forward()

def action_1000():
    print('1000')
    __turn_left()
    time.sleep(1.5)
    __forward()

def action_0001():
    print('0001')
    __turn_right()
    time.sleep(1.5)
    __forward()

def action_0011():
    print('0011')
    __turn_right()
    time.sleep(1)
    __forward()

def action_0111():
    print('0111')
    __turn_right()
    time.sleep(0.5)
    __forward()

def action_0010():
    print('0010')
    __turn_right()
    time.sleep(2)
    __forward()

def action_0110():
    print('0110')
    __turn_right()
    time.sleep(2)
    __forward()

def action_0101():
    print('0101')
    __turn_right()
    time.sleep(1.5)
    __forward()

def action_1101():
    print('1101')
    __turn_left()
    time.sleep(1.5)
    __forward()

def action_0100():
    print('0100')
    __turn_left()
    time.sleep(2)
    __forward()

def action_0000():
    print('0000')
    __backaway()
    time.sleep(0.5)
    __turn_left()
    time.sleep(2)
    __forward()

def action_1001():
    print('1001')
    __backaway()
    time.sleep(0.5)
    __turn_left()
    time.sleep(2)
    __forward()

def action_1011():
    print('1011')
    __backaway()
    time.sleep(0.5)
    __turn_right()
    time.sleep(2)
    __forward()

def action_1010():
    print('1011')
    __backaway()
    time.sleep(1)
    __turn_left()
    time.sleep(2)
    __forward()

def standby(_1553b):
    while True:
        if _1553b.get('STATUS') != True:
            time.sleep(3)
            continue
        else:
            fire()
            try:
                if '0x02_0x01' in _1553b:
                    data = _1553b['0x02_0x01'].get('data')
                    if data == [1,1,1,0]:
                        action_1110()
                    elif data == [1,1,0,0]:
                        action_1100()
                    elif data == [1,0,0,0]:
                        action_1000()
                    elif data == [0,0,0,1]:
                        action_0001()
                    elif data == [0,0,1,1]:
                        action_0011()
                    elif data == [0,1,1,1]:
                        action_0111()
                    elif data == [0,0,1,0]:
                        action_0010()
                    elif data == [0,1,1,0]:
                        action_0110()
                    elif data == [0,1,0,1]:
                        action_0101()
                    elif data == [1,1,0,1]:
                        action_1101()
                    elif data == [0,1,1,0]:
                        action_0110()
                    elif data == [0,1,0,0]:
                        action_0100()
                    elif data == [0,0,0,0]:
                        action_0000()
                    elif data == [1,0,0,1]:
                        action_1001()
                    elif data == [1,0,1,0]:
                        action_1010()
                    elif data == [1,0,1,1]:
                        action_1011()
                    elif data == [1,1,1,1]:
                        action_1111()
                    else:
                        print("whats happen????%s"% data)

                else:
                    action_1111()
                time.sleep(0.5)
            except Exception as e:
                continue
