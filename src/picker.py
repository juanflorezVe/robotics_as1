#!/usr/bin/env python
from std_srvs.srv import Empty, EmptyRequest
from r00184264_a1.srv import TurtlesAmount, TurtlesAmountRequest


import rospy
import time

#After created, wait 3 secs and delete one
time.sleep(3)
rospy.init_node('picker')
rospy.wait_for_service('/pickup_service')
pickuprequest = TurtlesAmountRequest()
pickuprequest.amount = 1

pickupclient = rospy.ServiceProxy('/pickup_service', TurtlesAmount)

rs = pickupclient(pickuprequest)

print "the end"
