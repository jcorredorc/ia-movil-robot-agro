#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

def publicador():
    pub = rospy.Publisher('saludo', String, queue_size=10)
    rospy.init_node('publicador', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        hello_str = "Hola amigos %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
  
if __name__ == '__main__':
    try:
        publicador()
    except rospy.ROSInterruptException:
        pass