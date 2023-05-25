#!/usr/bin/env python3
from time import sleep
import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('vel_robot_script', anonymous=False)
    velocity_publisher = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed=0.5
    angle=0.979
    
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    a = 0
    while a < 5:
        velocity_publisher.publish(vel_msg)
        sleep(1)
        a = a + 1

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = angle

    a = 0
    while a < 2:
        velocity_publisher.publish(vel_msg)
        sleep(1)
        a = a + 1

    vel_msg.linear.x = speed
    vel_msg.angular.z = 0.0
    a = 0
    while a < 5:
        velocity_publisher.publish(vel_msg)
        sleep(1)
        a = a + 1       

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)
    sleep(0.1)

if __name__ == '__main__':
    try:
        #Testing our function
        move()  
    except rospy.ROSInterruptException: pass    
