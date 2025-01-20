from naoqi import ALProxy
import time


ROBOT_IP = "192.168.1.100"  
PORT = 9559


motion_proxy = ALProxy("ALMotion", ROBOT_IP, PORT)
posture_proxy = ALProxy("ALRobotPosture", ROBOT_IP, PORT)


posture_proxy.goToPosture("StandInit", 0.8)
time.sleep(1)


names = [
    "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
    "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"
]


target_angles = [
    0.0,  # LShoulderPitch 
    0.3,  # LShoulderRoll 
    -1.5, # LElbowYaw 
    -0.05,  # LElbowRoll
    
    0.0,  # RShoulderPitch 
    -0.3, # RShoulderRoll 
    1.5,  # RElbowYaw 
    0.05   # RElbowRoll 
]


fraction_max_speed = 0.2


motion_proxy.setAngles(names, target_angles, fraction_max_speed)


time.sleep(5)


posture_proxy.goToPosture("StandInit", 0.8)
