#!/usr/bin/env python

import rospy
import random


from std_srvs.srv import Empty
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from r00184264.srv import TurtlesAmount, TurtlesAmountResponse


rospy.wait_for_service('/spawn')
serviceclient = rospy.ServiceProxy('/spawn', Spawn)
turtlelist = []


def turtle_creator(request):
    rospy.loginfo("Initiating Cretion")
    counter = request.amount
    while counter > 0:
        print("Test called")
        positionrequest = SpawnRequest(random.uniform(0,10), random.uniform(0,10), random.uniform(0,2),
                                       'post'+str(counter))
        turtlelist.append(serviceclient(positionrequest))
        counter -= 1
    return [] #TODO


rospy.init_node('nest_server')
rospy.Service('/nest_service', TurtlesAmount, turtle_creator)

rospy.spin()
