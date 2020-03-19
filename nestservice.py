#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse


def test_callback(request):
    print("Test called")
    return EmptyResponse


rospy.init_node('nest_server')
nest_service_server = rospy.Service('/nest_service', Empty, test_callback)




