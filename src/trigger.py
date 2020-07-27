#!/usr/bin/env python
from std_srvs.srv import Empty, EmptyRequest
from r00184264_a1.srv import TurtlesAmount, TurtlesAmountRequest
from turtlesim.srv import TeleportAbsoluteRequest
import rospy

rospy.init_node('trigger_pusher')


rospy.wait_for_service('/nest_service')
serviceclient = rospy.ServiceProxy('/nest_service', TurtlesAmount)

request_object = TurtlesAmountRequest()
request_object.amount = 0

result = serviceclient(request_object)

print "We created "
print result
