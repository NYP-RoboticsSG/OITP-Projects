#!/usr/bin/env python
#-*- coding=utf-8 -*-


import urllib2
import json
import rospy
import os
#from vlc933 import PLAYURL
from std_msgs.msg import String
from start import VLC111
#import start
import threading
from time import ctime,sleep
#import pubbb
text_input=''#raw_input('我:') 




#text_input=''

def boardcast():
    
    access_token = '24.68f00cd6498268b44cc7bd147d703c2b.2592000.1550572653.282335-15447525'
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token

    post_data = "{\"bot_session\":\"\",\"log_id\":\"7758521\",\"request\":{\"bernard_level\":1,\"client_session\":\"{\\\"client_results\\\":\\\"\\\", \\\"candidate_options\\\":[]}\",\"query\":\""+text_input+"\",\"query_info\":{\"asr_candidates\":[],\"source\":\"KEYBOARD\",\"type\":\"TEXT\"},\"updates\":\"\",\"user_id\":\"88888\"},\"bot_id\":\"33726\",\"version\":\"2.0\"}"

    request = urllib2.Request(url, post_data)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    response_dic = json.loads(content)

    results_text2 = response_dic['result']['response']['schema']['intent']
    #results_text3 = response_dic['result']['response']['action_list'][0]['say']

    url938=VLC111("https://playerservices.streamtheworld.com/api/livestream-redirect/938NOWAAC.aac")
    
    url933=VLC111('https://playerservices.streamtheworld.com/api/livestream-redirect/YES933AAC.aac')
    
    url958=VLC111("https://playerservices.streamtheworld.com/api/livestream-redirect/CAPITAL958FMAAC.aac")
    url95=VLC111("https://playerservices.streamtheworld.com/api/livestream-redirect/CLASS95AAC.aac")
    url833=VLC111('http://playerservices.streamtheworld.com/api/livestream-redirect/883JIA.mp3')
    url893=VLC111("http://playerservices.streamtheworld.com/api/livestream-redirect/MONEY_893.mp3")

    print(results_text2)

    #while True:
    
    if 'PLAY_BROADCAST'== results_text2:
         print("进来了")
        
         str1 = text_input;
         str2 = "九三三";
         str3 = "九十三点三";
         str4 = "八八三";
         str5 = "八十八点三";
         str6 = "九五八";
         str7 = "九十五点八";
         str8 = "八九三";
         str9 = "八十九点三";
         str10 = "九十五";
         str11 = "九三八";
         str12 = "九十三点八";
         str13 = "933";
         str14 = "883";
         str15 = "958";
         str16 = "893";
         str17 = "95";
         str18 = "938";
       
       #print str1.find(str2)
         if str1.find(str2) != -1:
           print ('play 九三三')
           url933.start()

         elif str1.find(str3) != -1:
           print ('play 九十三点三')
           #url933 =VLC111('https://playerservices.streamtheworld.com/api/livestream-redirect/YES933AAC.aac')
           url933.start()

         elif str1.find(str13) != -1:
           print ('play 933')
           print('播放这个')

         elif str1.find(str4) != -1:
           print ('play 八八三')
           url883.start()

         elif str1.find(str14) != -1:
           print ('play 883')
           url883.start()

         elif str1.find(str5) != -1:
           print ('play 八十八点三')
           url883.start()

         elif str1.find(str6) != -1:
           print ('play 九五八')
           url958.start()


         elif str1.find(str15) != -1:
           print ('play 958')
           url958.start()


         elif str1.find(str7) != -1:
           print ('play 九五点八')
           url958.start()
   
         elif str1.find(str16) != -1:
           print ('play 893')
           url893.start()


         elif str1.find(str8) != -1:
           print ('play 八九三')
           url893.start()

         
         elif str1.find(str9) != -1:
           print ('play 八九点三')
           url893.start()

 
         elif str1.find(str10) != -1:
           print ('play 九十五')
           url95.start()
       

         elif str1.find(str17) != -1:
           print ('play 95')
           url95.start()

         elif str1.find(str11) != -1:
           print ('play 九三八')
           url938.start()


         elif str1.find(str18) != -1:
           print ('play 938')
           url938.start()
    

         elif str1.find(str12) != -1:
           print ('play 九十三点八')
           url938.start()
         else:
           print("对不起没有你要的广播")

         Media = instance.media_new(url)
	 Media.get_mrl()
         player.set_media(Media)
	 player.play()




    elif 'CLOSE_BROADCAST'== results_text2:

          #url938=VLC111("https://playerservices.streamtheworld.com/api/livestream-redirect/938NOWAAC.aac")
	  url938.fangstop()
          #url933=VLC111('https://playerservices.streamtheworld.com/api/livestream-redirect/YES933AAC.aac')
          url933.fangstop()
          #url958=VLC111("https://playerservices.streamtheworld.com/api/livestream-redirect/CAPITAL958FMAAC.aac")
          url958.fangstop()
          #url95=VLC111("https://playerservices.streamtheworld.com/api/livestream-redirect/CLASS95AAC.aac")
          url95.fangstop()
          #url833=VLC111('http://playerservices.streamtheworld.com/api/livestream-redirect/883JIA.mp3')
          url833.fangstop()
          #url893=VLC111("http://playerservices.streamtheworld.com/api/livestream-redirect/MONEY_893.mp3")
          url893.fangstop()
          print("关闭广播")

  
    elif "POSITION"== results_text2:
         print("进来了么")
         pubbb.publish('请问厨房,桌子一号,桌子二号,桌子三号,桌子四号,桌子五号这五个地方去哪里')


    elif "REALPLACE"== results_text2:
          
         str1 = text_input;
         str2 = "厨房";
         str3 = "桌子一号";
         str4 = "桌子二号";
         str5 = "桌子三号";
         str6 = "桌子四号";
         str7 = "桌子五号";
      
         if str1.find(str2) != -1:
           print ('去厨房')
           pubb.publish('kitchen')

         elif str1.find(str3) != -1:
           print ('去桌子一号')
           pubb.publish('tableone')

         elif str1.find(str4) != -1:
           print ('去桌子二号')
           pubb.publish('tabletwo')

   
         elif str1.find(str5) != -1:
           print ('去桌子三号')
           pubb.publish('tablethree')


         elif str1.find(str6) != -1:
           print ('去桌子四号')
           pubb.publish('tablefour')


         elif str1.find(str3) != -1:
           print ('去桌子五号')
           pubb.publish('tablefive')

         else:
           print("没有这个地点")


    else: 
          
          pub.publish(text_input)
          rate.sleep()
           
          print("不用播放广播")
          



def boardcast_callback(data):
    global text_input
    rospy.loginfo('Testing: %s',data.data)
    text_input=data.data
    boardcast()



def broadcastsub():
    rospy.Subscriber('Rog_result',String, boardcast_callback)
    rospy.spin()



if __name__ =='__main__':
    try:
      pub=rospy.Publisher('new_topic',String,queue_size=1)
      pubbb = rospy.Publisher('speak_string', String, queue_size=1)
      pubb = rospy.Publisher('laizeyu', String, queue_size=1)
      rospy.init_node('broadcastnode',anonymous=True)
      rate=rospy.Rate(10)
#	talker()
      broadcastsub()
      #boardcaststop88()
    except rospy.ROSInterruptException:
        pass





