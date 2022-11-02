#!/usr/bin/env python3

import rospy
import std_msgs

rospy.init_node("IntroNode")
rate=rospy.Rate(10)

while not rospy.is_shutdown():
    rospy.loginfo("Hardwired Second Workshop at time")
    rate.sleep()

