#!/usr/bin/env python

import rospy
import random


from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from r00184264.srv import TurtlesAmount, TurtlesAmountResponse
from std_msgs.msg import String
from r00184264_a1.msg import location


rospy.wait_for_service('/spawn')
serviceclient = rospy.ServiceProxy('/spawn', Spawn)
turtlelist = []

#create the floor_topic
pub = rospy.Publisher("floor_topic", location, queue_size=15)

def turtle_creator(request):
    rospy.loginfo("Initiating Cretion")
    counter = request.amount
    for i in range(0,counter):
        x_pos = random.uniform(0,10)
        y_pos = random.uniform(0,10)
        positionrequest = SpawnRequest(x_pos, y_pos, random.uniform(0,2),
                                       'post'+str(i))
        turtlelist.append(serviceclient(positionrequest))
        loct = location()
        loct.x = x_pos
        loct.y = y_pos
        loct.name = turtlelist[-1].name
        pub.publish(loct)

        response = TurtlesAmountResponse()
        response.total = len(turtlelist)
    return response


rospy.init_node('nest_server')
rospy.Service('/nest_service', TurtlesAmount, turtle_creator)

rospy.spin()
