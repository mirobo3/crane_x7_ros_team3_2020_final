#!/usr/bin/env python
#coding: utf-8

import rospy
from std_msgs.msg import Int32
import choki
import gu
import par
import pose4
import hand_action
import par_new

n = 0
        
def process():
        pose4.main()
        rospy.sleep(1)
        n = rospy.wait_for_message('hand_gesture', Int32, 0.1)
        n = n.data
        print(n)

        if n > 0:
            if n == 1:
                choki.main()
            elif n == 2:
                par.main()
            elif n == 3:
                par_new.main()
            elif n == 5:
                gu.main()
            else: 
                print('not find gesture')
            if not n==3:
                hand_action.main()
        print('done')

if __name__=='__main__':
        if not rospy.is_shutdown():
            rospy.init_node("master")
            rospy.loginfo('master node started')
            process()

