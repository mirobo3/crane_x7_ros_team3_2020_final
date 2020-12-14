#!/usr/bin/env python
# -*- coding: utf-8 -*-

# このサンプルは実機動作のみに対応しています
# fake_execution:=trueにすると、GripperCommandActionのサーバが立ち上がりません

import sys
import rospy
import moveit_commander
import time
import actionlib
import math
from std_msgs.msg import Float64
from control_msgs.msg import (
    GripperCommandAction,
    GripperCommandGoal
)

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

def main():
   # rospy.init_node("gipper_action_client")
    gc = GripperClient()

    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(0.5)  

    arm.set_named_target("home")
    arm.go()

    print "joint_value_target (radians):"
    print arm.get_joint_value_target()
    print "current_joint_values (radians):"
    print arm.get_current_joint_values()

     #手首回転
    target_joint_values = arm.get_current_joint_values()
    joint_angle = math.radians(90)
    target_joint_values[6] = joint_angle 
    arm.set_joint_value_target(target_joint_values)
    arm.go()
    
     #チョキの手
    print "Change choki."
    gripper = 15
    gc.command(math.radians(gripper),1.0)
    result = gc.wait(2.0)
    print result
    time.sleep(1)

if __name__ == "__main__":
    main()
