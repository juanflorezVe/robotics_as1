#!/usr/bin/env python

import rospy
import random


from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from r00184264.srv import TurtlesAmount, TurtlesAmountResponse
from std_msgs.msg import String


rospy.wait_for_service('/spawn')
serviceclient = rospy.ServiceProxy('/spawn', Spawn)
turtlelist = []

#create the floor_topic
pub = rospy.Publisher("floor_topic", String, queue_size=15)

def turtle_creator(request):
    rospy.loginfo("Initiating Cretion")
    counter = request.amount
    for i in range(0,counter):
        positionrequest = SpawnRequest(random.uniform(0,10), random.uniform(0,10), random.uniform(0,2),
                                       'post'+str(i))
        turtlelist.append(serviceclient(positionrequest))
        pub.publish('post'+str(i))

    return [counter] #TODO


rospy.init_node('nest_server')
rospy.Service('/nest_service', TurtlesAmount, turtle_creator)

rospy.spin()
