#!/usr/bin/env python
#Listens to the topic for new spawned turtles in the floor,
#Listens to the topic for remoed turtles from the floor
#provides a service to tell what is the nearest object from the current
#position, or if there are no more objects.


import rospy
from std_msgs.msg import String
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from r00184264_a1.msg import location
from r00184264_a1.srv import ClosestObj, ClosestObjResponse

print "HELLO I AM DISPATCHER"
rospy.loginfo("Dispatcher file activated")
turtlesinthefloor={}

def react_to_new_turtle(data):
    rospy.loginfo("Dispatcher sees a new turtle is on the floor ")
    rospy.loginfo('{} -> {},{}'.format(data.name, data.x, data.y))
    turtlesinthefloor[data.name]=(data.x, data.y)

def listen_new_turtles():
    rospy.init_node("dispatcher")
    rospy.Subscriber("floor_topic", location, react_to_new_turtle)


def react_to_removed_turtle(data):
    rospy.loginfo("{} was removed from the floor".format(data.name))
    #TODO: remove the turtle from the list

def listen_removed_turtle():
    rospy.init_node("dispatcher")
    rospy.Subscriber("robot1_topic", location, react_to_removed_turtle)
#===============================

listen_new_turtles()
listen_removed_turtle()
#====================== Service to tell the next one ===============

def get_closest_turtle(location):
    '''
    Using the manhattan algo, get the closest turtle in the floor to the location
    '''
    #TODO implement
    return ClosestObjResponse()

rospy.init_node("dispatcher")
rospy.Service('/next_closest_turtle', ClosestObj, get_closest_turtle)

rospy.spin()
