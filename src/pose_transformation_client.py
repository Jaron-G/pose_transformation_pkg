#!/usr/bin/env python3
from __future__ import print_function 
import sys
import rospy
from pose_transformation.srv import PoseTransform,PoseTransformResponse#注意是功能包名.srv
import numpy as np

def pose_transformation_client(x, y):
    rospy.wait_for_service('pose_transformation')
    try:
        pose_transformation = rospy.ServiceProxy('pose_transformation', PoseTransform)
        resp1 = pose_transformation(x, y)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    rospy.init_node("pose_tranformation_client")
    final_pose = np.array([[7.07361985e-01, 7.06851485e-01,  4.21206373e-07,  240],
    [-7.06851485e-01,  7.07361985e-01,  2.34742508e-05, -700],
    [1.62948636e-05, -1.69025230e-05,  1,  1010],
    [0,  0,  0,  1]])
    rospy.loginfo("Start pose transform!")
    final_pose = final_pose.reshape(-1).tolist()
    matched_model = 'pipe'
    print("Requesting:",final_pose, matched_model)
    response = pose_transformation_client(final_pose, matched_model)
    print("rotation_matri is :",response.rotation_matrix)
    print("grasp_pose is :",type(response.grasp_pose))
    print("up_pose is :",response.up_pose)
    rospy.loginfo("Pose transform is OK !")
