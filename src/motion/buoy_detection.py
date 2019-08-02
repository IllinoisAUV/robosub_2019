#! /usr/bin/python

import numpy as np
import cv2
import time
import rospy

from darknet_ros_msgs.msg import BoundingBox, BoundingBoxes
from geometry_msgs import Twist
from sensor_msgs import Image

states = ["findFirst", "hitFirst", "findSecond", "hitSecond"]

class buoyDetecter(object):

    def __init__(self):
        self.buoy_sub = rospy.Subscriber("", BoundingBoxes, self.buoy_callback)

        self.image = None

        # ADD Camera Pixel Data
        self.cameraArea = 1

        self.state = "findFirst"

        self.targetVamp = "jia"

        self.detected = False

        self.detected_idx = 0

        self.detected_box = None

        self.prev_detection = None

        self.execute = False

    def buoy_callback(self, data):
        if self.execute:
            self.callExecute(data)

    def callExecute(self, data):

        if self.state == "findSecond" or self.state == "hitSecond":
            self.targetVamp = "asw"

        self.detected = False

        for i in range(len(data.bounding_boxes)):
            if data.bounding_boxes[i].Class == self.targetVamp:
                self.detected = True
                self.detected_idx = i
                self.detected_box = data.bounding_boxes[i]

        if self.detected:
            xmin = self.bounding_box.xmin
            xmax = self.bounding_box.xmax
            ymin = self.bounding_box.ymin
            ymax = self.bounding_box.ymax

            box_area = abs(xmin - xmax) * abs(ymin - ymax)


    def find_first(self, boxes):
        pass
