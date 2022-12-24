## RENARDI ADRYANTORO PRIAMBUDI

import serial
import time

## initialize serial
SerialObj = None
try:
    SerialObj = serial.Serial('COM11',9600) # open the Serial Port
except serial.SerialException as var : # var contains details of issue
    print('An Exception Occured')
    print('Exception Details-> ', var)

else:
    SerialObj.baudrate = 9600  # set Baud rate to 9600
    SerialObj.bytesize = 8     # Number of data bits = 8
    SerialObj.parity   ='N'    # No parity
    SerialObj.stopbits = 1     # Number of Stop bits = 1
    print('Serial Port Opened')

# time.sleep(3)


def send_arm_joint_angle(joint_angle=[]):
    #left arm
    # joint_angle[1]
    # joint_angle[2]
    # joint_angle[3]

    #right arm
    # joint_angle[4]
    # joint_angle[5]
    # joint_angle[6]

    pkg_stringify = "#"+str(joint_angle[1])+","+str(joint_angle[2])+","+str(joint_angle[3])+","+str(joint_angle[4])+","+str(joint_angle[5])+","+str(joint_angle[6])+"!"

    #send
    if SerialObj:
        SerialObj.write(pkg_stringify)      #transmit 'A' (8bit) to micro/Arduino












#close the port
if SerialObj:   
    SerialObj.close()          # Close the port