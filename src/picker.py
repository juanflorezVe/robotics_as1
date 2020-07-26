#!/usr/bin/env python
from std_srvs.srv import Empty, EmptyRequest
from r00184264_a1.srv import TurtlesAmount, TurtlesAmountRequest
from r00184264_a1.srv import ClosestObj, ClosestObjRequest


import rospy
import time


#After created, wait 3 secs and delete one
time.sleep(3)

#Ask the dispatcher what is the closest turtle to the current position.
print("I WILL START COLLECTING SOON")
rospy.init_node('picker')
rospy.wait_for_service('/next_closest_turtle')
#TODO: calculate starting position
nextlocationrequest = ClosestObjRequest()
rospy.loginfo('passed 456')



rospy.wait_for_service('/pickup_service')
pickuprequest = TurtlesAmountRequest()
pickuprequest.amount = 1

pickupclient = rospy.ServiceProxy('/pickup_service', TurtlesAmount)

rs = pickupclient(pickuprequest)

print "the end"
