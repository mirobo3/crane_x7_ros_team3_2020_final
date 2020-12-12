#!/usr/bin/python
import rospy
from std_msgs.msg import Int32

def callback(message):
     if message.data == 2:
       print('7')
     else:
       print('5')


if __name__ == '__main__':
  rospy.init_node('sub_node')
  rospy.Subscriber('pub_node', Int32, callback)
  rospy.spin()
