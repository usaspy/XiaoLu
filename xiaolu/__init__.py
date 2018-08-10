#-*- coding: UTF-8 -*-
'''
1553B数据总线

用于各个组件之间的数据传输和指令下达。
格式如下：
key:
 如 _1553b[类型]
value:｛｝
[发送者]：send
[接受者]：to
[传输的数据]:datas 根据[类型]定义
[模式]:　mode １使用完清除　２使用完保留 3使用完置为默认值
[优先级]：priority 1～９　　默认１
[时间戳]：time 数据发送时间　=key

'''
from multiprocessing import Process,Manager

m = Manager()
_1553b = m.dict()

#定义各个子系统的系统ID
WHEEL_SYS = 0x01
INFRARED_SYS = 0x02
TFTLCD_SYS = 0x04