## RENARDI ADRYANTORO PRIAMBUDI

import serial
import time
# from vision import *
## initialize serial
SerialObj = None
try:
    SerialObj = serial.Serial('COM7',9600) # open the Serial Port
    SerialObj.timeout = 1
    time.sleep(3)

except serial.SerialException as var : # var contains details of issue
    print('An Exception Occured')
    print('Exception Details-> ', var)

def send_arm_joint_angle(torque=[],joint_angle=[]):
    #left arm
    # joint_angle[1]
    # joint_angle[2]
    # joint_angle[3]

    #right arm
    # joint_angle[4]
    # joint_angle[5]
    # joint_angle[6]

    pkg_stringify = "#"+"$"+str(torque[0])+","+str(joint_angle[0])+"$"+str(torque[1])+","+str(joint_angle[1])+"$"+str(torque[2])+","+str(joint_angle[2])+"$"+str(torque[3])+","+str(joint_angle[3])+"$"+str(torque[4])+","+str(joint_angle[4])+"$"+str(torque[5])+","+str(joint_angle[5])+"$"+str(torque[6])+","+str(joint_angle[6])+"$"+str(torque[7])+","+str(joint_angle[7])+"$"+str(torque[8])+","+str(joint_angle[8])+"$"+str(torque[9])+","+str(joint_angle[9])+"$"+str(torque[10])+","+str(joint_angle[10])+"$"+str(torque[11])+","+str(joint_angle[11])+"$"+str(torque[12])+","+str(joint_angle[12])+"$"+str(torque[13])+","+str(joint_angle[13])+"$"+str(torque[14])+","+str(joint_angle[14])+"$"+str(torque[15])+","+str(joint_angle[15])+"$"+str(torque[16])+","+str(joint_angle[16])+"$"+str(torque[17])+","+str(joint_angle[17])+"$"+"!"
    print(pkg_stringify)
    
    for char in pkg_stringify:
        if SerialObj:
            SerialObj.write(char.encode())      #transmit 'A' (8bit) to micro/Arduino
            SerialObj.flush()
            # time.sleep(0.0005)


torque=[0] * 18
torque[0]=1
torque[1]=1

joint_angle=[0] * 18
joint_angle[0]=500
joint_angle[1]=500
send_arm_joint_angle(torque,joint_angle)

# while 1:
#     pass
    #read vision
    # flag_break,distance = update_vision()
    # print(distance)
    # if flag_break == 1:
    #     break


# time.sleep(3)
#close the port
if SerialObj:   
    SerialObj.close()          # Close the port