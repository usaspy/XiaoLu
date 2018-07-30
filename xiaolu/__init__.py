#-*- coding: UTF-8 -*-
#指令通道

from multiprocessing import Process,Manager

m = Manager()
dd = m.dict()

