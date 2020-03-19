#!/usr/bin/env python
from std_srvs.srv import Empty, EmptyRequest
import rospy

rospy.init_node('trigger_pusher')
rospy.wait_for_service('/nest_service')
serviceclient = rospy.ServiceProxy('/nest_service', Empty)

request_object = EmptyRequest()

result = serviceclient(request_object)

print result
