#!/usr/bin/env python

import rospy
import random
from std_srvs.srv import Empty
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse


rospy.wait_for_service('/spawn')
serviceclient = rospy.ServiceProxy('/spawn', Spawn)
turtlelist = []


def turtle_creator(empty):
    print("Test called")
    positionrequest = SpawnRequest(random.uniform(0,10), random.uniform(0,10), random.uniform(0,2),'post'+str(random.randint(0,23)))
    turtlelist.append(serviceclient(positionrequest))
    return []


rospy.init_node('nest_server')
rospy.Service('/nest_service', Empty, turtle_creator)

rospy.spin()



