#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

rospy.init_node("IntroSubscriber")

# def callback_intro(data):
#   rospy.loginfo(data.data)

def vel_callback(data):
  print("linear.x=",data.linear.x,", linear.y=",data.linear.y,", angular.x=",data.angular.x,", angular.y=",data.angular.y)

# sub = rospy.Subscriber('intro', String, callback_intro)
vel_sub=rospy.Subscriber('cmd_vel',Twist,vel_callback)
rospy.spin()

