#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import math
import geometry_msgs.msg
from control_msgs.msg import GripperCommandAction, GripperCommandGoal
from tf.transformations import quaternion_from_euler
import rosnode
import actionlib
import time
import sys

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

    APPROACH_Z = 0.2 #移動するときの高さ
    LEAVE_Z = 0.20   #持ち上げる高さ
    PICK_Z = 0.14    #掴むときのアームの高さ
    card0 = 0.0      #カード3のy座標
    card2 = -0.07    #カード2のy座標
    card1 = 0.07     #カード1のy座標
    cardx = 0.195    #3つのカードのx座標

    rospy.init_node("gripper_action_client")
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    #アームの動きの速さを示している
    arm.set_max_velocity_scaling_factor(0.3)

    gripper = moveit_commander.MoveGroupCommander("gripper")
    

    while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
        rospy.sleep(1.0)
    rospy.sleep(1.0)

    print("Group names:")
    print(robot.get_group_names())

    print("Current state:")
    print(robot.get_current_state())

    # アーム初期ポーズを表示
    arm_initial_pose = arm.get_current_pose().pose
    print("Arm initial pose:")
    print(arm_initial_pose)

    # SRDFに定義されている"home"の姿勢にする
    arm.set_named_target("home")
    arm.go()
    gripper.set_joint_value_target([0.7, 0.7])
    gripper.go()
    
    #繰り返し呼び出すのでmove関数を定義する
    def move(x,y,z):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = x
        target_pose.position.y = y
        target_pose.position.z = z
        q = quaternion_from_euler(-3.14, 0.0, 3.14)  
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)  
        arm.go()  

    #掴むカードを迷う動作
    move(cardx, card0, APPROACH_Z)   
    rospy.sleep(1.0)
    move(cardx, card2, APPROACH_Z)
    rospy.sleep(1.2) 
    move(cardx, card1, APPROACH_Z)
    rospy.sleep(1.5)

    move(cardx, card0, APPROACH_Z)
    rospy.sleep(2.0)
    move(cardx, card0, 0.16)
    rospy.sleep(1.0)
    move(cardx, card0, APPROACH_Z)
    rospy.sleep(1.0)

    move(cardx, card1, APPROACH_Z)
    rospy.sleep(1.0)

    # 掴みにいく
    move(cardx, card1, PICK_Z)
    rospy.sleep(1.0)

    gc = GripperClient()
    rospy.sleep(1.0)

    #gripperの角度を変える
    gripper = 0.275
    gc.command(math.radians(gripper), 1.0)
    result=gc.wait(2.0)
    time.sleep(1)
    
    # 持ち上げる
    move(cardx,card1,LEAVE_Z)

    # 移動する
    move(cardx,0.3,0.2)

    # SRDFに定義されている"home"の姿勢にする
    # srdfファイルがある場所 (mirobo3_3_2020_crane_x7_ros/crane_x7_moveit_config/config/crane_x7.srdf)
    arm.set_named_target("home")
    arm.go()

    move(cardx, card0, 0.3)

    def move1(x,y,z):
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = x
        target_pose.position.y = y
        target_pose.position.z = z
        q = quaternion_from_euler(-3.14, 0.0, 0.0)
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)
        arm.go()
    
        rospy.sleep(1.0)

    move1(cardx, card0, 0.25)

    move1(0.02, -0.3, APPROACH_Z)

    gripper = 45
    gc.command(math.radians(gripper), 1.0)
    result=gc.wait(2.0)
    time.sleep(1)

    arm.set_named_target("vertical")
    arm.go() 

    print("done")


if __name__ == '__main__':

    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
