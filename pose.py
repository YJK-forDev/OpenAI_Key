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

    # Left arm angles
    left_shoulder_pitch = 1.5  # Approximation for "up"
    left_shoulder_roll = 0.5  # Away from the torso
    left_elbow_yaw = -1.0  # Rotation
    left_elbow_roll = -0.5  # Slightly bent

    # Right arm angles
    right_shoulder_pitch = 1.0  # Slightly down
    right_shoulder_roll = -0.3  # Closer to torso
    right_elbow_yaw = 1.0  # Rotation
    right_elbow_roll = 0.5  # Slightly bent

    motion_proxy.setAngles([
        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
        "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll"
    ], [
        left_shoulder_pitch, left_shoulder_roll, left_elbow_yaw, left_elbow_roll,
        right_shoulder_pitch, right_shoulder_roll, right_elbow_yaw, right_elbow_roll
    ], 0.2)

    # Optionally wait to hold the pose
    time.sleep(3)

    # Disable stiffness after execution
    motion_proxy.setStiffnesses("Body", 0.0)

if __name__ == "__main__":
    set_pepper_pose()
