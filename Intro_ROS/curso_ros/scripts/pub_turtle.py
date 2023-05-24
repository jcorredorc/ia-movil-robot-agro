#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('vel_robot_script', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Moveremos el robot...")
    speed = int(input("Ingrese la velocidad"))
    isForward = input("Adelante?: ")#True or False

    #Checking if the movement is forward or backwards
    if(isForward == "True"):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = abs(speed)*(-1)

    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass