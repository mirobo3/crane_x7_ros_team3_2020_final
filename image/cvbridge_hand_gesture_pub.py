#!/usr/bin/env python3
# coding: UTF-8

import numpy as np
import rospy
import cv2
from cv_bridge import CvBridge
import os
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
import math

shape = 0

def start_node():

    global shape
    rospy.init_node('opencv')
    rospy.loginfo('opencv node started')
   # rospy.Publisher("hand_gesture", Int32, queue_size=1)
   # rospy.Subscriber("camera/color/image_raw", Image, process_image)
    sub = Subscribers()
    pub = Publishsers()
    rospy.spin()
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        pub.send_msg()
        rate.sleep()

class Publishsers():
        def __init__(self):
            self.publisher = rospy.Publisher('hand_gesture', Int32, queue_size=1)
            self.message = Int32()
        def make_msg(self):
            pass
        def send_msg(self):
            self.make_msg()
            self.publisher.publish(self.message)

class Subscribers():
        def __init__(self):
            self.subscriber = rospy.Subscriber('camera/color/image_raw', Image, self.process_image)
            self.message = Image()
        def process_image(self,msg):

            try:
                bridge = CvBridge()
                frame = bridge.imgmsg_to_cv2(msg, "bgr8")
                size1 = (1080, 720)#画面サイズ
                count=0
                kernel = np.ones((3,3), np.uint8)
                frame=cv2.GaussianBlur(frame,(5,5),0)
                frame= cv2.medianBlur(frame,5)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                lower_skin = np.array([0,20,70], dtype=np.uint8)
                upper_skin = np.array([25,255,255], dtype=np.uint8)

                mask = cv2.inRange(hsv, lower_skin, upper_skin)

                mask = cv2.dilate(mask, kernel,iterations = 4)

        #        mask = cv2.GaussianBlur(mask,(5,5),100)
            #輪郭を検出
                contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            #最大の輪郭を見つける
                cnt = max(contours, key = lambda x: cv2.contourArea(x))

        #approx contour
                epsilon = 0.001*cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, epsilon, True)

            #輪郭の凸包（convex hull）を求める
                hull = cv2.convexHull(cnt)

        #area define
                areahull = cv2.contourArea(hull)
                areacnt = cv2.contourArea(cnt)
                #print(areacnt)

        #arearatio
                arearatio = ((areahull-areacnt)/areacnt)*100
                #print(arearatio)

            #物体検出
                n, img_label, data, center = cv2.connectedComponentsWithStats(mask)
                img_trans_marked = frame.copy()

            #最大の輪郭と凸包を描画
                img_trans_marked = cv2.drawContours(img_trans_marked, [cnt], -1, (255,0,0), 3)

            #凹状欠損（convexity defects）の検出
                #cnt = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
                hull = cv2.convexHull(cnt, returnPoints=False)

            #凹状欠損の点を描画
                defects = cv2.convexityDefects(cnt, hull)
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])

               #print(d)

                    a = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
                    b = math.sqrt((far[0]-start[0])**2 + (far[1]-start[1])**2)
                    c = math.sqrt((end[0]-far[0])**2 + (end[1]-far[1])**2)
                    s = (a+b+c)/2
                    ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
        #distance convex hull
                    d = (2*ar)/a
                    angle = math.acos((b**2+c**2-a**2)/(2*b*c))*57

                    if angle < 70 and d>90:
                        count+=1

                        cv2.circle(img_trans_marked, far, 5, [0, 255, 0], -1)

                cv2.line(img_trans_marked, start, end, [0, 255, 0], 2)


                count+=1
                font = cv2.FONT_HERSHEY_SIMPLEX
                if count == 0:
                    cv2.putText(img_trans_marked, 'gu', (0, 100), font, 4, (0, 0, 255), 5, cv2.LINE_AA)
                    shape=1

                if count == 1:
                    if areacnt<58000:
                        cv2.putText(img_trans_marked, 'gu', (0, 100), font, 4, (0, 0, 255), 5, cv2.LINE_AA)
                        shape=1
                   # elif arearatio<12:
                    #    cv2.putText(img_trans_marked, 'gu', (0, 100), font, 6, (0, 0, 255), 5, cv2.LINE_AA)
                    else:
                        cv2.putText(img_trans_marked, 'gu', (0, 100), font, 4, (0, 0, 255), 5, cv2.LINE_AA)
                        shape=1


                if count == 2:
                    cv2.putText(img_trans_marked, 'choki', (0, 100), font, 4, (0, 0, 255), 5, cv2.LINE_AA)
                    shape=2

                if count == 3:
                    cv2.putText(img_trans_marked, '3', (0, 100), font, 4, (0, 0, 255), 5, cv2.LINE_AA)
                    shape=3


                if count == 4:
                    cv2.putText(img_trans_marked, '4', (0, 100), font, 4, (0, 0, 255), 5, cv2.LINE_AA)
                    shape=4

                if count >= 5:
                    cv2.putText(img_trans_marked, 'pa', (0, 100), font, 4, (0, 0, 255), 5, cv2.LINE_AA)
                    shape=5


                cv2.rectangle(img_trans_marked, (100,100),(550,450),(0,255,0),0)
                cv2.imshow('trans',img_trans_marked)
                cv2.imshow('mask', mask)

           #     pub = rospy.Publisher('hand_gesture', Int32, queue_size=1)
                #pub.publish(shape)

                cv2.waitKey(10)
                

            except:
                pass

if __name__=='__main__':
    try:
        start_node()
    except rospy.ROSInterruptException: pass
