#!/usr/bin/env python
#-*- coding=utf-8 -*-

import requests
from std_msgs.msg import String
import rospy
import json
#import urllib2.urlopen
import sys
import urllib

text_input=""
def talker():
  
    url='http://openapi.tuling123.com/openapi/api/v2'
    
    #while not rospy.is_shutdown():

	#text_input = raw_input ('我:')

    data1 = {
	  'reqType':0,
	  'perception': {
	     'inputText': {
		 'text':text_input#'你是谁'
	     }
	     },
	     'userInfo': {
		  'apiKey':'af6e2529ff1345378bf87f52de838b28',
		  'userId':'quanfang'
	     }
    }
        
    r = requests.post(url,data=json.dumps(data1))
    response_dic = json.loads(r.text)
    results_text = response_dic['results'][0]['values']['text']
    print(results_text)
    pub.publish(results_text)
    rate.sleep()

def listener_callback(data):
    global text_input
    rospy.loginfo('Testing: %s',data.data)
    text_input=data.data
    talker()

def listener():
#    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('new_topic',String, listener_callback)
    rospy.spin()
   

if __name__ =='__main__':
    try:
      pub=rospy.Publisher('speak_string',String,queue_size=10)
      rospy.init_node('tuling_node',anonymous=True)
      rate=rospy.Rate(10)
#	talker()
      listener()
    except rospy.ROSInterruptException:
        pass


