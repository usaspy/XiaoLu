#!/usr/bin/python3
# coding=utf-8
'''
xiaolu机器人功能需求：
前置条件：
    树莓派电源打开，主程序开始运行
动作：
    1.打开电源开关，此时边扫电机和吸尘电机均开始工作，但行走机构不动，LCD显示“小鲁准备就绪，”
    2.操作员press启动按钮，此时行走电机开始工作，向前缓慢行走，LCD显示“小路正在专心打扫中,请勿打扰..”
    3.以下动作在启动后自动执行：
        a) 三个红外传感器持续工作，进近检测距离为5CM. 分7种情况：001 010 100 011 110 101 111 另外000(正常) ,导航系统每0.2秒取一次三个值，决定行走方向
        b) 行走进程持续运行，根据公共总线上的信号执行机动
        c) input/output
            红外遥控input接受命令，启动/停止行走机构
            LCD显示屏从总线接受显示内容，并显示在屏幕上。
'''
# 主进程
from multiprocessing import Process
from xiaolu import _1553b #数据总线  进程间数据共享
#import affinity
from xiaolu import wheel
from xiaolu import infrared
from xiaolu import view_1553b
from xiaolu import tft_screen
from xiaolu import console

# noinspection PyInterpreter
if __name__ == "__main__":
    try:
        p1 = Process(target=wheel.standby,args=(_1553b,),name='0x01')
        p2 = Process(target=infrared.scan,args=(_1553b,),name='0x02')
        p3 = Process(target=tft_screen.display,args=(_1553b,),name='0x04')
    #    p0 = Process(target=view_1553b.view,args=(_1553b,),name='0x00')
        p4 = Process(target=console.webconsole.view,args=(_1553b,),name='0x08')

        p1.daemon = True
        p2.daemon = True
        p3.daemon = True
        p4.daemon = True
     #   p0.daemon = True

        p1.start()
        p2.start()
        p3.start()
        p4.start()
    #    p0.start()

     #   affinity.set_process_affinity_mask(p1.pid,7L)
     #   affinity.set_process_affinity_mask(p2.pid,7L)

        p1.join()
        p2.join()
        p3.join()
        p4.join()
   #     p0.join()
    except Exception as e:
        print(e)
    finally:
        print("系统停机...")