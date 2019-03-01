#!/usr/bin/env python
#-*- coding=utf-8 -*-



import sys
#import http.client
import time
from vlc import VideoMarqueeOption, Position, EventType,Instance


class VLC_Player():

    def __init__(self, url):
        self.url = url

    def start(self,timeout=60):
        instance = Instance()
        player = instance.media_player_new()
        Media = instance.media_new(self.url)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        time.sleep(timeout)

    def fangstop(self)
        player.stop()

if __name__ == "__main__":
    url = "https://playerservices.streamtheworld.com/api/livestream-redirect/938NOWAAC.aac"
    p = VLC_Player(url)
    p.start(60)
    




