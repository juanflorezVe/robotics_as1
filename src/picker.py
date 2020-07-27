#!/usr/bin/env python
from std_srvs.srv import Empty, EmptyRequest
from r00184264_a1.srv import TurtlesAmount, TurtlesAmountRequest
from r00184264_a1.srv import ClosestObj, ClosestObjRequest, ClosestObjResponse
from turtlesim.srv import Kill, KillRequest


import rospy
import time


#After created, wait 3 secs and delete one
time.sleep(3)

#Ask the dispatcher what is the closest turtle to the current position.
print("I WILL START COLLECTING SOON")
rospy.init_node('picker')

#Ugly global variable for current position
rospy.wait_for_service('/next_closest_turtle')
nextturtleclient = rospy.ServiceProxy('/next_closest_turtle', ClosestObj)
rospy.loginfo("THE SERVICE FOR PICKER IS UP")
#TODO: make the loop
nextlocationrequest = ClosestObjRequest()
nextobjectresponse = nextturtleclient(nextlocationrequest)

print "the end"
