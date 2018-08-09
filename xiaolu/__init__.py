#-*- coding: UTF-8 -*-
'''
1553B数据总线

用于各个组件之间的数据传输和指令下达。
格式如下：
[发送者][接受者][传输的数据][模式][优先级][时间]

'''
from multiprocessing import Process,Manager

m = Manager()
b1553 = m.dict()


#定义各个子系统的系统ID
WHEEL_ID = 0x01
INFRARED_ID = 0x02
TFTLCD_ID = 0x04

