#!/usr/bin/env python3

import rospy
from rosgraph_msgs.msg import Log

class ROSOUTSubscriber:
    def __init__(self):
        self.dwa_failure_count = 0
        self.global_failure_count = 0
        rospy.loginfo("rosout_subscriber_node is started.")
        self.sub = rospy.Subscriber('/rosout', Log, self.rosout_callback)

    def rosout_callback(self, msg):
        if msg.msg == "DWA planner failed to produce path.":
            self.dwa_failure_count += 1
            rospy.loginfo("DWA planner failure count: %d", self.dwa_failure_count)
        if msg.msg == "Failed to get a plan.":
            self.global_failure_count += 1
            rospy.loginfo("Global planner failure count: %d", self.global_failure_count)

if __name__ == "__main__":
    rospy.init_node('rosout_subscriber_node')
    counter = ROSOUTSubscriber()
    rospy.spin()