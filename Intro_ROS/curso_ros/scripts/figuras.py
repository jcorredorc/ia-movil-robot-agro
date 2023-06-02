#!/usr/bin/env python
from time import sleep
import rospy
from geometry_msgs.msg import Twist

# def move():
# Starts a new node
rospy.init_node('vel_robot_script', anonymous=True)
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

#Receiveing the user's input
vel_x=1
vel_msg.linear.y = 0
vel_msg.linear.z = 0
vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0

def lineal_move(num_times_dist):
    a=0
    print("inicio mov lineal")
    while(a<num_times_dist):
        vel_msg.linear.x = vel_x
        # vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        a+=1
        print("wait 1seg")
        sleep(1)        
    print("fin mov lineal")
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)


def rotate(num_times_rotate):
    print("inicio rotar")
    vel=2.09439
    a=0
    while(a < num_times_rotate):
        vel_msg.linear.x = 0
        vel_msg.angular.z=vel
        velocity_publisher.publish(vel_msg)
        print("wait 1 seg")
        sleep(1) 
        a+=1
    print("fin rotar")
    vel_msg.linear.x = 0
    vel_msg.angular.z=0
    velocity_publisher.publish(vel_msg)
    
def triangle(dist,ang):
    for arista in range(3):
        lineal_move(dist)
        sleep(2)
        rotate(ang)
        sleep(2)
        print("end triangle")
    
def square(dist,ang):
    for arista in range(4):
        lineal_move(dist)
        sleep(2)
        rotate(ang)
        sleep(2)
        print("end square")
     

    #Checking if the movement is forward or backwards
#     if(isForward == "True"):
#         a=0
#         while(a<4):
#             vel_msg.linear.x = vel_x
#             vel_msg.angular.z = 0
#             velocity_publisher.publish(vel_msg)
#             a=a+1
#             sleep(1)        
#         print("fin mov lineal")
#         vel_msg.linear.x = 0
#         vel_msg.angular.z=2.094
#         velocity_publisher.publish(vel_msg)
#         sleep(3) 
#         a=0
#         while(a<4):
#             vel_msg.linear.x = vel_x
#             vel_msg.angular.z = 0
#             velocity_publisher.publish(vel_msg)
#             a=a+1
#             sleep(1)  
#         vel_msg.linear.x = 0  
#         vel_msg.angular.z=2.094
#         velocity_publisher.publish(vel_msg)
#         sleep(1) 
#         a=0
#         while(a<4):
#             vel_msg.linear.x = vel_x
#             vel_msg.angular.z = 0
#             velocity_publisher.publish(vel_msg)
#             a=a+1
#             sleep(1)
     
#         vel_msg.linear.x = 0  
#         vel_msg.angular.z=2.094
#         velocity_publisher.publish(vel_msg)
#         sleep(1) 

#  #Dibujar Cuadrado
#         z=0
#         for z in range (4):
#             a=0
#             while(a<4):
#                 vel_msg.linear.x = vel_x
#                 vel_msg.angular.z = 0
#                 velocity_publisher.publish(vel_msg)
#                 a=a+1
#                 sleep(1)
     
#             vel_msg.linear.x = 0  
#             vel_msg.angular.z=1.5707
#             velocity_publisher.publish(vel_msg)
#             sleep(1) 
    
            
#     else:
#         print("MDigite ctrl C")
#     #Since we are moving just in x-axis

if __name__ == '__main__':
    # try:
    print("Moveremos el robot...")
    isForward = input("1 - Triangulo, 2 - Cuadrado: ") #True or False
        #Testing our function
    if isForward == "1":
        triangle(4,1)
    elif isForward == "2":   
        square(4,5)
    else:
        print("fin ")
    
        # lineal_move(4)
    # except rospy.ROSInterruptException: pass