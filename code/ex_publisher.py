#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

vel=Twist()
vel.linear.x=1
vel.linear.y=1
vel.angular.x=150
vel.angular.y=150

rospy.init_node("IntroPublisher")
rate=rospy.Rate(10)
# pub = rospy.Publisher('intro', String, queue_size=10)
vel_pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)

while not rospy.is_shutdown():
    # pub.publish("Sending data on the intro topic")
    vel_pub.publish(vel)
    rate.sleep()

