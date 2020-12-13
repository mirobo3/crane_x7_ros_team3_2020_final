#!/usr/bin/env python
# coding: UTF-8

#金曜日に起こっていた問題は解決しました
#インポートするのではなく、移植しました
#
import sys
import rospy
import moveit_commander
import time
import actionlib
import math
import rosnode
import geometry_msgs.msg
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from control_msgs.msg import (
    GripperCommandAction,
    GripperCommandGoal
)
import pose2

class GripperClient(object):
    def __init__(self):
        self._client = actionlib.SimpleActionClient("/crane_x7/gripper_controller/gripper_cmd",GripperCommandAction)
        self._goal = GripperCommandGoal()

        # Wait 10 Seconds for the gripper action server to start or exit
        self._client.wait_for_server(rospy.Duration(10.0))
        if not self._client.wait_for_server(rospy.Duration(10.0)):
            rospy.logerr("Exiting - Gripper Action Server Not Found.")
            rospy.signal_shutdown("Action Server not found.")
            sys.exit(1)
        self.clear()

    def command(self, position, effort):
        self._goal.command.position = position
        self._goal.command.max_effort = effort
        self._client.send_goal(self._goal,feedback_cb=self.feedback)

    def feedback(self,msg):
        print("feedback callback")
        print(msg)

    def stop(self):
        self._client.cancel_goal()

    def wait(self, timeout=0.1 ):
        self._client.wait_for_result(timeout=rospy.Duration(timeout))
        return self._client.get_result()

    def clear(self):
        self._goal = GripperCommandGoal()

def call(message):
	pose2.main()

	gc = GripperClient()
	arm = moveit_commander.MoveGroupCommander("arm")
	arm.set_max_velocity_scaling_factor(0.5)  
	arm.set_named_target("home")
	arm.go()

	print ("joint_value_target (radians):")
	print (arm.get_joint_value_target())
	print ("current_joint_values (radians):")
	print (arm.get_current_joint_values())

	if message.data == 1:
		target_joint_values = arm.get_current_joint_values()
		joint_angle = math.radians(90)
		target_joint_values[6] = joint_angle 
		arm.set_joint_value_target(target_joint_values)
		arm.go()
		# チョキの手
		print ("Close choki.")
		gripper = 15
		gc.command(math.radians(gripper),1.0)
		result = gc.wait(2.0)
		print (result)
		time.sleep(1)
	elif message.data == 2:
		target_joint_values = arm.get_current_joint_values()
		joint_angle = math.radians(0)
		target_joint_values[6] = joint_angle 
		arm.set_joint_value_target(target_joint_values)
		arm.go()
     	#グーの手
		print ("Close gu.")
		gripper = 0.0
		gc.command(math.radians(gripper),1.0)
		result = gc.wait(2.0)
		print (result)
		time.sleep(1)
	elif message.data==3:
		target_joint_values = arm.get_current_joint_values()
     	#手首回転
		joint_angle = math.radians(0)
		target_joint_values[6] = joint_angle 
		arm.set_joint_value_target(target_joint_values)
		arm.go()
		#パーの手
		print ("Change par.")
		gripper = 70
		gc.command(math.radians(gripper),1.0)
		result = gc.wait(2.0)
		print (result)
		time.sleep(1)
	else:
		print('Error Not correct number')

	# 悔しがる
	target_joint_values = arm.get_current_joint_values()
	joint_angle = math.radians(90)
	target_joint_values[6] = joint_angle 
	arm.set_joint_value_target(target_joint_values)
	arm.go()

	for i in range(3):
		target_joint_values = arm.get_current_joint_values()
		joint_angle = math.radians(-60)
		target_joint_values[3] = joint_angle 
		arm.set_joint_value_target(target_joint_values)
		arm.go()
		target_joint_values = arm.get_current_joint_values()
		joint_angle = math.radians(-160)
		target_joint_values[3] = joint_angle 
		arm.set_joint_value_target(target_joint_values)
		arm.go()

	gripper = 0.0
	gc.command(math.radians(gripper),1.0)
	result = gc.wait(2.0)
	print result
	time.sleep(1)

def main():
	rospy.init_node('main')
	rospy.Subscriber("gesture_gu", Int32, call)
	rospy.spin()

if __name__ == "__main__":
	try:
		if not rospy.is_shutdown():
			main()
	except rospy.ROSInterruptException:
		pass
