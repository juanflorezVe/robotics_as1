#!/usr/bin/env python

import rospy
import random


from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
from r00184264.srv import TurtlesAmount, TurtlesAmountResponse
from std_msgs.msg import String
from r00184264_a1.msg import location
from geometry_msgs.msg import Twist



#create the floor_topic
pub1 = rospy.Publisher("robot1_topic", location, queue_size=15)


#TODO get rid of these

# def turtle_twister(vel):
#    rospy.loginfo("Service /move_turtle_in_arc has been called")
#    move_turtle.linear.x = 0.5
#    move_turtle.angular.z = 0.5
#    pub.publish(move_turtle)
#    rospy.loginfo("Finished service /move_turtle_in_arc")
#    return SpawnResponse()

def turtle_collector(request):
    rospy.loginfo("Initiating Collection")
    counter = request.amount
    for i in range(0,counter):
        loct = location()
        loct.x = 1
        loct.y = 2
        loct.name = 'testname'
        pub1.publish(loct)
    return TurtlesAmountResponse()

#move_turtle = Twist()
rospy.init_node('pickup_server')
rospy.Service('/pickup_service', TurtlesAmount, turtle_collector)

rospy.spin()
