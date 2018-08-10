'''
扫地机显示系统
功能：
1.系统开机后，现实欢迎界面，5秒后进入系统界面，显示系统默认状态，包括时间，当前运行状态（stopped）
2.用户按运行按钮，系统进入运行状态，此时，屏幕可以应该显示更多信息，包括实时的四个点位的避障数据、当前运行状态Runing,,启动运行的时长，后期再增加实时的PM10数值
3.用户按停止按钮，系统进入开机待运行状态，此时，屏幕回到1.
'''

import time
import BHack_ILI9225 as TFT
import xiaolu

def display():
    time.sleep(20)
    xiaolu.Runing = True