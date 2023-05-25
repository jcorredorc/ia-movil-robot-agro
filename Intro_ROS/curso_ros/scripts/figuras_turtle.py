import rospy 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose 
import math 
import time 
from std_srvs.srv import Empty 
from math import pi 

x=0 
y=0 
z=0 
yaw=0 

def poseCallback(pose_message): 
    global x 
    global y, z, yaw 
    x= pose_message.x 
    y= pose_message.y 
    yaw = pose_message.theta 

 
 



def rotate(speed, angle):
    #declare a Twist message to send velocity commands 
    velocity_message = Twist() 
    #get current location from the global variable before entering the loop  
    # x0=x 
    # y0=y 
    #z0=z; 
    print("ACTUAL ORIENTATION: ", yaw)
    # yaw0=0; 

    #task 1. assign the x coordinate of linear velocity to the speed.  
    # velocity_message.angular.z = speed
 
    # distance_moved = 0.0 
    # loop_rate = rospy.Rate(100) # we publish the velocity at 10 Hz (10 times a second)     

    #task 2. create a publisher for the velocity message on the appropriate topic.   
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # while True : 
    #     rospy.loginfo("Turtlesim rotates") 

    #     #task 3. publish the velocity message 
    #     velocity_publisher.publish(velocity_message)            

    #     loop_rate.sleep() 
                    
    #     #rospy.Duration(1.0) 

 
    #     #measure the angle moved
    #     print("yaw: " , yaw) 
    #     print("yaw0: " , yaw0) 
    #     distance_moved = ((pi + abs(yaw/3)  if yaw < 0 else yaw) - yaw0)
    #     print("angulo absoluto: "   ,distance_moved)
    #     # distance_moved = distance_moved+(yaw-yaw0)#abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2))) 
    #     print(str(distance_moved))                
    #     if  not (distance_moved<angle): 
    #         rospy.loginfo("reached angle") 
    #         break 
             
    #     #task 4. publish a velocity message zero to make the robot stop after the distance is reached 
    # velocity_message.angular.z =0
    # velocity_publisher.publish(velocity_message)

    #### ------------------
    #Converting from angles to radians
    angular_speed = speed*2*pi/360
    relative_angle = angle*2*pi/360

    #We wont use linear components
    velocity_message.linear.y=0
    velocity_message.linear.x=0
    velocity_message.linear.z=0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0

    clockwise = False
    # Checking if our movement is CW or CCW
    if clockwise:
        velocity_message.angular.z = -abs(angular_speed)
    else:
        velocity_message.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        # print("control vel ...")
        velocity_publisher.publish(velocity_message)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)


    #Forcing our robot to stop
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message )
    # rospy.spin()
## --------------------------------


def move(speed, distance):
    #declare a Twist message to send velocity commands 
    velocity_message = Twist() 

    #get current location from the global variable before entering the loop  
    x0=x 
    y0=y 
    #z0=z; 
    #yaw0=yaw; 

    #task 1. assign the x coordinate of linear velocity to the speed.  
    velocity_message.linear.x = speed
 
    distance_moved = 0.0 
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)     

    #task 2. create a publisher for the velocity message on the appropriate topic.   
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while True : 
        rospy.loginfo("Turtlesim moves forwards") 

        #task 3. publish the velocity message 
        velocity_publisher.publish(velocity_message)            

        loop_rate.sleep() 
                    
        #rospy.Duration(1.0) 

 
        #measure the distance moved 
        distance_moved = distance_moved+abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2))) 
        print(str(distance_moved))                
        if  not (distance_moved<distance): 
            rospy.loginfo("reached") 
            break 
             
        #task 4. publish a velocity message zero to make the robot stop after the distance is reached 
    velocity_message.linear.x =0
    velocity_publisher.publish(velocity_message)
     

def triangle():
    print("draw triangle")
    angulo=2*pi/3
    for i in range(3):
        print(angulo)
        rotate(0.15,angulo*i)
        time.sleep(2) 
        print('move: ') 
        move (1.0, 10.0) 
        time.sleep(2)
        print(angulo)
        # rotate(0.15,angulo)
        # time.sleep(2) 


    # time.sleep(2) 

if __name__ == '__main__': 
    try: 
         
        rospy.init_node('turtlesim_motion_pose', anonymous=True) 

        #task 5. declare velocity publisher 
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
         
        position_topic = "/turtle1/pose" 
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback) 

        
        # time.sleep(2) 
        # print('move: ') 
        # move (1.0, 5.0) 
        # time.sleep(2) 
        print('start reset: ') 
        rospy.wait_for_service('reset') 
        reset_turtle = rospy.ServiceProxy('reset', Empty) 
        reset_turtle() 
        print('end reset: ')
        move(1,10)
        time.sleep(2)
        rotate(20,120)
        time.sleep(2)
        move(1,10)
        time.sleep(2)
        rotate(20,120)
        time.sleep(2)
        move(1,10)
        time.sleep(2)
        rotate(20,120)
        print("-----------")
        print("angulo grados : ", yaw )
        print("-----------")

        time.sleep(2)
        move(1,10)
        # triangle()
        rospy.spin() 
        
    except rospy.ROSInterruptException: 
        rospy.loginfo("node terminated.")