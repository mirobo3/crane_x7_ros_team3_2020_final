#!/usr/bin/python
import rospy
from std_msgs.msg import Int32

rospy.init_node('count', anonymous=True)
pub = rospy.Publisher('pub_node', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
  pub.publish(2)
  rate.sleep()
