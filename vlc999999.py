#!/usr/bin/python
#-*- coding=utf-8 -*-

import time
from multiprocessing import Process
import os

class PLAYURL:
  def __init__(self,url_str):
    self.url_str=url_str
    

  def playURL(self):
    
    os.system('vlc '+self.url_str) 
myPlay933 =PLAYURL('https://playerservices.streamtheworld.com/api/livestream-redirect/YES933AAC.aac')
myplay833 =PLAYURL('http://playerservices.streamtheworld.com/api/livestream-redirect/883JIA.mp3')
myplay958 =PLAYURL("https://playerservices.streamtheworld.com/api/livestream-redirect/CAPITAL958FMAAC.aac")
myplay893 =PLAYURL("http://playerservices.streamtheworld.com/api/livestream-redirect/MONEY_893.mp3")
myplay95 =PLAYURL("https://playerservices.streamtheworld.com/api/livestream-redirect/CLASS95AAC.aac")
myplay938 =PLAYURL("https://playerservices.streamtheworld.com/api/livestream-redirect/938NOWAAC.aac")
myplay958 =PLAYURL("https://playerservices.streamtheworld.com/api/livestream-redirect/CAPITAL958FMAAC.aac")



if __name__ == '__main__':
    p = Process(target=self.playURL)
    p.start()
    p.terminate() # 关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
    print(p.is_alive())  # True
    time.sleep(0.1)
    print(p.is_alive()) # Fals


    
    
    #myPlay =PLAYURL('https://playerservices.streamtheworld.com/api/livestream-redirect/YES933AAC.aac')
    #myPlay.playURL()
   


