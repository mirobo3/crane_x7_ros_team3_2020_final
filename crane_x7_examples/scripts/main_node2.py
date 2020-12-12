#!/usr/bin/env python
#coding: utf-8

import rospy
from std_msgs.msg import Int32
import choki
import gu
import par
import pose2


n = 0
#flag = 0
        
def process():
        pose2.main()
        rospy.sleep(2)
        n = rospy.wait_for_message('hand_gesture', Int32)
        n = n.data
        print(n)

        if n > 0:
            if n == 1:
                gu.main()
            elif n == 2:
                choki.main()
            elif n == 5:
                par.main()
            else: 
                print('not find gesture')
        print('done')

def callback(self, message):
    global n
    n = message.data



if __name__=='__main__':
        if not rospy.is_shutdown():
            rospy.init_node("master")
            rospy.loginfo('master node started')
            flag = 0
            process()

