#!/usr/bin/env python
#Listens to the topic for new spawned turtles in the floor,
#Listens to the topic for remoed turtles from the floor
#provides a service to tell what is the nearest object from the current
#position, or if there are no more objects.


import rospy
import numpy as np
from std_msgs.msg import String
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse, KillRequest, Kill
from r00184264_a1.msg import location
from r00184264_a1.srv import ClosestObj, ClosestObjResponse
from turtlesim.msg import Pose
from math import fabs

print "HELLO I AM DISPATCHER"
rospy.init_node("dispatcher")


#======================================
# Keep track of the position of Turtle1
turtle1_position = (0.0,0.0)
def update_position(data):
    turtle1_position = (data.x, data.y)
rospy.Subscriber("/Turtle1/pose", Pose, update_position)

#======================================
# Keep track of the turtles in the floor
rospy.loginfo("Dispatcher file activated")
turtlesinthefloor={}

def react_to_removed_turtle(data):
    rospy.loginfo("{} turtle was picked, so the floor gets updated".format(data.name))
    killrequest = KillRequest()
    killrequest.name = data.name

    rospy.wait_for_service("/kill")
    killerserviceclient = rospy.ServiceProxy('/kill', Kill)

    killerserviceclient(killrequest)
    del turtlesinthefloor[data.name]
    rospy.loginfo("{} was removed from the floor".format(data.name))


def react_to_new_turtle(data):
    rospy.loginfo("Dispatcher sees a new turtle is on the floor ")
    rospy.loginfo('{} -> {},{}'.format(data.name, data.x, data.y))
    turtlesinthefloor[data.name]=(data.x, data.y)

def listen_new_turtles():
    rospy.init_node("dispatcher")
    rospy.Subscriber("floor_topic", location, react_to_new_turtle)

def listen_removed_turtle():
    rospy.init_node("dispatcher")
    rospy.Subscriber("robot1_topic", location, react_to_removed_turtle)
#=======================================
listen_new_turtles()
listen_removed_turtle()
#=========================================





#===============================

#====================== Service to tell the next one ===============


def get_closest_turtle(location):
    '''
    Using the manhattan algo, get the closest turtle in the floor to the location
    '''
    #fk = ClosestObjResponse()
    #fk.name='post1'
    #return fk
    closesttrt = '1000000'
    closest = 100000
    for i in turtlesinthefloor:
        print i
        tmp = fabs((turtle1_position[0]-turtlesinthefloor[i][0])+
                       (turtle1_position[1]-turtlesinthefloor[i][1]))
        print tmp
        if tmp < closest:
            closest = tmp
            closesttrt = i
        print closesttrt

    nextturtle = ClosestObjResponse()
    nextturtle.name = closesttrt
    nextturtle.x = turtlesinthefloor[closesttrt][0]
    nextturtle.y = turtlesinthefloor[closesttrt][1]

    rospy.loginfo("Sending NExt CLOSEST T {} {} {}".format(nextturtle.name,
                                                 nextturtle.x, nextturtle.y))
    return nextturtle



rospy.Service('/next_closest_turtle', ClosestObj, get_closest_turtle)
rospy.loginfo("Turtle removing service activated")




rospy.spin()
