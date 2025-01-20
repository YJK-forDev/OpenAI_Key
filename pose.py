from naoqi import ALProxy
import time

def set_pepper_pose():
    # Connect to Pepper's motion service
    robot_ip = "<ROBOT_IP>"  # Replace with Pepper's IP address
    robot_port = 9559
    motion_proxy = ALProxy("ALMotion", robot_ip, robot_port)

    # Enable stiffness
    motion_proxy.setStiffnesses("Body", 1.0)

    # Head angles
    head_yaw = 0.44279  # Right/left rotation
    head_pitch = 0.15521  # Up/down rotation
    motion_proxy.setAngles(["HeadYaw", "HeadPitch"], [head_yaw, head_pitch], 0.2)

    # Arm angles
    left_shoulder_pitch = 0.25131
    left_shoulder_roll = 0.53421
    left_elbow_yaw = 0.36757
    left_elbow_roll = 0.60147

    right_shoulder_pitch = 0.27621
    right_shoulder_roll = 0.29358
    right_elbow_yaw = 0.40686
    right_elbow_roll = 0.23589

    motion_proxy.setAngles([
        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
        "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"
    ], [
        left_shoulder_pitch, left_shoulder_roll, left_elbow_yaw, left_elbow_roll,
        right_shoulder_pitch, right_shoulder_roll, right_elbow_yaw, right_elbow_roll
    ], 0.2)

    # Hip angles
    left_hip_pitch = 0.48977
    left_hip_roll = 0.51471
    right_hip_pitch = 0.50066
    right_hip_roll = 0.38069

    motion_proxy.setAngles([
        "LHipPitch", "LHipRoll", "RHipPitch", "RHipRoll"
    ], [
        left_hip_pitch, left_hip_roll, right_hip_pitch, right_hip_roll
    ], 0.2)

    # Optionally wait to hold the pose
    time.sleep(3)

    # Disable stiffness after execution
    motion_proxy.setStiffnesses("Body", 0.0)

if __name__ == "__main__":
    set_pepper_pose()
