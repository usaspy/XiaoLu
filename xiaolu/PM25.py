#!/usr/bin/python3
# coding=utf-8
'''
夏普PM2.5测量模块
模拟数据需要模数转换ADC1115进行数据转换，然后树梅派通过I2C接口获取转换后的PM2.5浓度值
模拟电压越高表示PM2.5浓度越高。

系统每0.5秒检测一次浓度，如果有连续的两次浓度超过〉XXX，则执行重点清扫（原地打转清扫，直到浓度降下来）
'''
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

def pm25_detect(_1553b):
    while True:
        value = adc.read_adc(0, gain=GAIN)
        if value > 1000:
            pass
        time.sleep(0.5)
