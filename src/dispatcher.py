#!/usr/bin/env python
#Listens to the topic for new spawned turtles in the floor,
#Listens to the topic for remoed turtles from the floor
#provides a service to tell what is the nearest object from the current
#position, or if there are no more objects.


import rospy
from std_msgs.msg import String

print "HELLO I AM DISPATCHER"
rospy.loginfo("Dispatcher file activated")

def react_to_new_turtle(data):
    rospy.loginfo("Dispatcher sees a new turtle is on the floor ")

def lister_new_turtles():
    rospy.init_node("dispatcher")
    rospy.Subscriber("floor_topic", String, react_to_new_turtle)


lister_new_turtles()
rospy.spin()
