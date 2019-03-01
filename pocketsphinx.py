#!/usr/bin/env python
#-*- coding=utf-8 -*-

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

import os
import pyaudio
import wave
import audioop
from collections import deque
import time
import math
from std_msgs.msg import Int16
from std_msgs.msg import Bool
import rospy
from pygame import mixer,mixer_music
from std_msgs.msg import String 
#from vlc933 import PLAYURL

#reload(sys)
#sys.setdefaultencoding('utf8')
#import sys
#from Queue import Queue

'''
Written by Sophie Li, 2016
http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/
'''

class SpeechDetector:
    def __init__(self):
# Microphone stream config.
        #rospy.init_node('wake_up')
        
	rospy.init_node('pocket')
        rospy.on_shutdown(self.shutdown)  
       
 	self.CHUNK = 1024# CHUNKS of bytes to read each time from mic
	self.FORMAT = pyaudio.paInt16
	self.CHANNELS = 1
	self.RATE = 16000
        self.url_str='https://playerservices.streamtheworld.com/api/livestream-redirect/YES933AAC.aac'
        

	self.SILENCE_LIMIT = 1 # Silence limit in seconds. The max ammount of seconds where
# only silence is recorded. When this time passes the
# recording finishes and the file is decoded

	self.PREV_AUDIO = 0.5 # Previous audio (in seconds) to prepend. When noise
# is detected, how much of previously recorded audio is
# prepended. This helps to prevent chopping the beginning
# of the phrase.

	self.THRESHOLD = 4500
	self.num_phrases = -1	

# These will need to be modified according to where the pocketsphinx folder is
	MODELDIR ='../../wakeup/src/hmm_lm/'
	#MODELDIR ='home/catkin_ws/src/wakeup/src/hmm_lm/'
	#DATADIR = 'pocketsphinx/test/data'

# Create a decoder with certain model
	config = Decoder.default_config()
	config.set_string('-hmm', os.path.join(MODELDIR, "zh_broadcastnews_ptm256_8000"))#Hidden Markov Model
	config.set_string('-lm', os.path.join(MODELDIR, '2594.lm'))#Language Model
	config.set_string('-dict', os.path.join(MODELDIR, '2594.dic'))#Dictionary Model
      

    def music(self):
        file='你好你好.mp3'
	init=mixer.init()
        track=mixer.music.load(file)
        play=mixer.music.play()
	timesleep=time.sleep(10)
	
    def pocket(self):
        #global String
        print("pocket")
	
        #rospy.init_node('pocket',anonymous=True)
	rate=rospy.Rate(10)
        #while not rospy.is_shutdown():
	
	while not rospy.is_shutdown():
            connections = self.pub.get_num_connections()
            rospy.loginfo('Connections: %d', connections)
            if connections > 0:
                self.pub.publish("嘿,现在你可以启动了")
                rospy.loginfo('Published')
                break
            rate.sleep()
     	#	rate.sleep()

    def playurl(self):
        os.system('vlc '+self.url_str)
        
    def setup_mic(self, num_samples=50):
        '''
     Gets average audio intensity of your mic sound. You can use it to
       get average intensities while you're  talking and/or silent. The average  is the avg of the .2 of the 
      largest intensities recorded
        '''

#print (“Getting intensity values from mic.”)
        rospy.loginfo("从麦克风获取强度值.")
	p = pyaudio.PyAudio()
	stream = p.open(format=self.FORMAT,
			channels=self.CHANNELS,
			rate=self.RATE,
			input=True,
			frames_per_buffer=self.CHUNK)

	values = [math.sqrt(abs(audioop.avg(stream.read(self.CHUNK), 4)))
		  for x in range(num_samples)]
	values = sorted(values, reverse=True)
	r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
	#rospy.loginfo(" 完成啦啦啦啦 ")
	#rospy.loginfo ('平均音频强度是: %s ' % r)
	stream.close()
	p.terminate()

	if r < 3000:
            self.THRESHOLD = 1000#3500
        else:
            self.THRESHOLD = r + 100

    def save_speech(self, data, p):
        '''
            Saves mic data to temporary WAV file. Returns filename of saved
            file
        '''
        filename = 'output_' + str(int(time.time()))
        # writes data to WAV file
        data = ''.join(data)
        wf = wave.open(filename + '.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)  # TODO make this value a function parameter?
        wf.writeframes(data)
        wf.close()
        return filename + '.wav'

    def decode_phrase(self, wav_file):
        self.decoder.start_utt()
        stream = open(wav_file, "rb")
        while True:
            buf = stream.read(1024)
            if buf:
                self.decoder.process_raw(buf, False, False)
            else:
                break
        self.decoder.end_utt()
        words = []
        [words.append(seg.word) for seg in self.decoder.seg()]
        return words
        #print('啊哈哈哈或或或或或或或或或或或或或或或或或或')

    def run(self):
        """
        Listens to Microphone, extracts phrases from it and calls pocketsphinx
        to decode the sound
        """
        self.setup_mic()

        #Open stream
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT, 
                        channels=self.CHANNELS, 
                        rate=self.RATE, 
                        input=True, 
                        frames_per_buffer=self.CHUNK)
        rospy.loginfo('麦克风启动.')
        audio2send = []
        cur_data = ''  # current chunk of audio data
        rel = self.RATE/self.CHUNK
        slid_win = deque(maxlen=self.SILENCE_LIMIT * rel)
        #Prepend audio from 0.5 seconds before noise was detected
        prev_audio = deque(maxlen=self.PREV_AUDIO * rel)
        started = False
        #self.pub=rospy.Publisher('wakeup',Int16,queue_size=2)
	msg=Int16()
        msg.data=True
	self.pub=rospy.Publisher('YYYYYY',String,queue_size=1)

        while True:
            cur_data = stream.read(self.CHUNK)
            slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))

	    #print(self.THRESHOLD,slid_win)
            if sum([x > self.THRESHOLD for x in slid_win]) > 0:
                if started == False:
                    #rospy.loginfo('开始录制短语')
                    started = True
                audio2send.append(cur_data)
		rospy.loginfo("audo test threshold")

            elif started:
                #rospy.loginfo('完成录制,开始解码')
                filename = self.save_speech(list(prev_audio) + audio2send, p)
                r = self.decode_phrase(filename)
		print(len(r))
                if len(r) > 3 and len(r)< 6:
	   	  text = r[1] + r[3]
                  print(text)	
                  temp=text.decode('utf-8')
		  print("777777777777777777777777")
                  print(temp)
		else:
                  temp = " "#r[1]
                print("1")
                print(temp)
                #rospy.loginfo('解码: %s',r)	
		
                # Removes temp audio file
                os.remove(filename)
		#leng=len(r)
		
                if '你好富丽华'== temp.encode('utf-8'):
		    msg.data = '你好富丽华'
                    print(12345)
   		    self.pocket()
		    self.music()
 	            
		      #pub.publish(msg)
	 	    rospy.loginfo(msg)
               
                # Reset all
                started = False
                slid_win = deque(maxlen=self.SILENCE_LIMIT * rel)
                prev_audio = deque(maxlen=0.5 * rel)
                audio2send = []
                #rospy.loginfo('听听听听听')

            else:
                prev_audio.append(cur_data)
                
        stream.close()
        p.terminate() 


    def shutdown(self):
        rospy.loginfo('wakeup关门了')
        os._exit(0)

if __name__ == "__main__":
    sd = SpeechDetector()
    sd.run()
    
