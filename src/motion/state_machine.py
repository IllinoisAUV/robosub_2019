#! /usr/bin/python

from motion_controller import *

import rospy
import sys
import time

import numpy as np

required_orientation = np.pi*3/4
take_layout = ["turn", "head_to_gate", "gate", "path", "buoys"]

class FSM(object):

    def __init__(self, sim):
        self.sim = sim
        self.state = take_layout[0]
        self.controller = Controller(self.sim)
        self.goal_reached = False

    def fsm_start(self):

        # ARM THE SUB IF NOT IN SIM
        while (True and not self.sim):
            data = self.controller.doArming()
            if data == False:
                print ("Arming Failed, Retrying")
            else:
                break

        # Turn REQUIRED amount to required_orientation
        self.Turn()

        # DIVE REQUIRED AMOUNT BASED ON SECONDS
        # ADD Support for dive by height using Pressure Sensor
        self.Dive(2.0)

    # TRY SETPOINT_ATTITUDE
    def Turn(self):

        global required_orientation

        vel = Twist()

        rospy.loginfo ("Current attitude: " + str(self.controller.attitude[2]))
        rospy.loginfo ("Required attitude: " + str(required_orientation))

        deg = self.controller.attitude[2] - required_orientation

        if deg < 0:
            deg += 2*np.pi

        if deg < np.pi:
            vel.angular.z = -0.25
        else:
            vel.angular.z = 0.25

        rospy.loginfo("STARTING TURNING")

        while abs(deg) > np.pi/8:

            deg = abs(self.controller.attitude[2] - required_orientation)

            rospy.loginfo(self.controller.attitude)

            if deg > np.pi:
                deg -= 2*np.pi
            # rospy.loginfo(str(self.controller.attitude))
            self.controller.pub_cmd_vel.publish(vel)
            rospy.sleep(1)

        vel.angular.z = 0.0
        self.controller.pub_cmd_vel.publish(vel)
        rospy.sleep(1)

        rospy.loginfo("TURNING DONE")

    def Dive(self, sec):
        # Add distance or seconds
        rospy.loginfo("DIVING")

        vel = Twist()
        vel.linear.z = -0.5

        rospy.loginfo("Speed: " + str(vel.linear.z))
        start_time = time.time()

        # sleep rate

        while time.time() <= start_time + sec:
            self.controller.pub_cmd_vel.publish(vel)
            rospy.sleep(1)

        vel = Twist()
        vel.angular.z = 0.0
        self.controller.pub_cmd_vel.publish(vel)
        rospy.sleep(1)
        rospy.loginfo("DIVING OVER")


def main():

    rospy.init_node("fsm")

    if len(sys.argv) != 0 and sys.argv[1] == "--sim":
        fsm = FSM(True)
    else:
        fsm = FSM(False)

    fsm.fsm_start()

if __name__ == "__main__":
    main()
