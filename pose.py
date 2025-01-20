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

    # Left arm angles (more bent, closer to torso, rotated inward)
    left_shoulder_pitch = 1.4  # Slightly lower
    left_shoulder_roll = 0.2  # Closer to the torso
    left_elbow_yaw = -1.2  # Rotation
    left_elbow_roll = -1.5  # More bent inward
    left_wrist_yaw = -0.5  # Adjusted wrist orientation

    # Right arm angles (fully bent, closer to torso)
    right_shoulder_pitch = 0.8  # Lower position
    right_shoulder_roll = 0.0  # Neutral, close to torso
    right_elbow_yaw = 1.8  # Rotation
    right_elbow_roll = 1.5  # Fully bent
    right_wrist_yaw = 0.5  # Adjusted wrist orientation

    motion_proxy.setAngles([
        "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
        "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"
    ], [
        left_shoulder_pitch, left_shoulder_roll, left_elbow_yaw, left_elbow_roll, left_wrist_yaw,
        right_shoulder_pitch, right_shoulder_roll, right_elbow_yaw, right_elbow_roll, right_wrist_yaw
    ], 0.2)

    # Optionally wait to hold the pose
    time.sleep(3)

    # Disable stiffness after execution
    motion_proxy.setStiffnesses("Body", 0.0)

if __name__ == "__main__":
    set_pepper_pose()
