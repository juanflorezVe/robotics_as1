#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse

rospy.wait_for_service('/spawn')
serviceclient = rospy.ServiceProxy('/spawn', Spawn)
turtlelist = []
counter = 0

def turtle_creator(empty):
    print("Test called")
    positionrequest = SpawnRequest(float(2), float(3), 0.6, (counter += 1).str() )
    turtlelist.append(serviceclient(positionrequest))
    return []


rospy.init_node('nest_server')
rospy.Service('/nest_service', Empty, turtle_creator())

rospy.spin()



