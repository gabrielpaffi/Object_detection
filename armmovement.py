import rtde_control, rtde_receive
import numpy as np

#Check what the x y and z axis are on the arm  and where the origin is

def ArmMovement(XPosition, YPosition):

    # Setup robot with robot IP address
    rtde_c = rtde_control.RTDEControlInterface("192.168.1.22")
    rtde_r = rtde_receive.RTDEReceiveInterface("192.168.1.22")

    # Speeds and accelerations - Joint space
    speed_J_fast = 0.7
    acc_J_fast = 1
    # Speeds and accelerations - Cartesian space
    speed_L_fast = 0.5
    acc_L_fast = 1

    # Gripper size
    H = 0.15 # 15 cm
    L = 0.2

    # Coordinates of object

    xObject = XPosition
    yObject = YPosition

    rObject = np.sqrt(xObject^2+yObject^2)
    alpha = np.arctan(yObject/xObject)

    # Calculating arm coordinates

    xArm = (rObject-L)*np.cos(alpha)
    yArm = (rObject-L)*np.sin(alpha)

    #Move robot to object position (no margin taken into account here)

    position1 = [0, 0, 0]
    position1[0] = xArm # When calling the python script, input the x and y coordinates as inputs.
    position1[1] = yArm # python MovingToObjects.py XPos YPos ZPos
    position1[2] = H # This is the z axis position of the object

    rtde_c.moveL(position1, speed_J_fast, acc_L_fast, True)
    # Move robot along along Z axis for 50 mm, non-blocking movement
    # Default is False - blocking movement, True is non-blocking movement
    # Blocking movement means it'll move one axis after the other and not simultaneously.

    CurrentPosition = rtde_r.getActualTCPPose()

    if (CurrentPosition == position1):
        print("Arm has finished moving")

    # Stop the RTDE control script
    rtde_c.stopScript()