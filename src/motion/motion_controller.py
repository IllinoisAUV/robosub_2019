#! /usr/bin/python

import numpy as np
import rospy
from geometry_msgs import Twist, TwistStamped
from mavros_msgs import State
from mavros_msgs.srv import *
from nav_msgs import Odometry

from mavros.srv import Arming

class Controller(object):

    def __init__(self):

        # SUBCRIBERS
        self.mavros_state = rospy.Subscriber("/mavros/state", \
                State, self.state_callback)

        self.odom = rospy.Subscriber("/mavros/local_position/odom", Odometry, \
        self.odom_callback)



        # PUBLISHERS
        self.pub_cmd_vel = rospy.Publisher("/mavros/setpoint_velocity/cmd_vel")

        self.pub_accel = rospy.Publisher("/mavros/setpoint_accel/accel")

        self.pub_attitude = rospy.Publisher("/mavros/setpoint_raw/attitude")


        # SERVICES
        self.arming_agent = rospy.ServiveProcy("/mavros/cmd/arming")

        # VARIABLES
        self.arm_state = False
        self.pose = Pose()

    # FUNCTION TO ARM THE SUB
    def doArming(self):
        data = self.arming_agent(True)
        rospy.loginfo("Arming Callback")
        print(data)

        # FUNCTION TO DISARM THE SUB
    def doDisarm(self):
        data = self.arming_agent(False)
        rospy.loginfo("Disarm Callback")
        print(data)

    def 
