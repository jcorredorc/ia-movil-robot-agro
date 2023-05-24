#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Estoy leyendo el mensaje %s", data.data)

def suscriptor():
    rospy.init_node('suscriptor', anonymous=True)

    rospy.Subscriber("saludo", String, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    suscriptor()