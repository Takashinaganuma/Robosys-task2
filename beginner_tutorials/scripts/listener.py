#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time

COUNT = 3
PIN = [4, 17, 5, 6]
GPIO.setmode(GPIO.BCM)
for pin in PIN:
    GPIO.setup(pin,GPIO.OUT)

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
    if(data.data == "a"):
        for pin in PIN:
            GPIO.output(pin,True)
            time.sleep(0.5)
            GPIO.output(pin,False)

    elif(data.data == "b"):
        for pin in PIN:
            GPIO.output(pin,True)
            time.sleep(1.0)
            GPIO.output(pin,False)
            time.sleep(1.5)

        
def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.spin()
    
           
if __name__ == '__main__':
    listener()
    
