from naoqi import ALProxy

# 로봇의 IP 및 포트 (사용자의 Pepper 로봇 IP로 수정)
robot_ip = "192.168.1.100"  
robot_port = 9559

# ALMotion 프록시 생성
motion = ALProxy("ALMotion", robot_ip, robot_port)

# 목표 nose 좌표 (x, y, z)
target_position = [0.442791522, 0.155218989, -0.676236689]

# 프레임 선택 (0 = FRAME_TORSO, 1 = FRAME_WORLD, 2 = FRAME_ROBOT)
frame = 0  # TORSO 기준 좌표계

# 축 마스크 (XYZ 위치만 조정 -> 1 + 2 + 4 = 7)
axis_mask = 7  

# 속도 설정 (0.1: 천천히, 1.0: 최대 속도)
fraction_max_speed = 0.5  

# 머리 위치 조정 (chainName: "Head")
motion.setPositions("Head", frame, target_position, fraction_max_speed, axis_mask)

print("Pepper's head moved to the target position.")
