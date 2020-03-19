#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty


def test_callback(empty):
    print("Test called")
    return []


rospy.init_node('nest_server')
rospy.Service('/nest_service', Empty, test_callback)

rospy.spin()



