import matplotlib.pyplot as plt
import numpy as np
import math




def geometric_invers_kinematic(xref,yref,zref,A1,A2,A3):

    if xref > 0:
        theta1 = math.degrees(math.atan(yref/xref))
    else:
        theta1 = 180 - math.degrees(math.atan(yref/xref))
    
    r_1 = math.sqrt(xref*xref + yref*yref)
    r_2 = zref - A1
    r_3 = math.sqrt(r_2*r_2 + r_1*r_1)

    psi_1 = math.degrees(math.atan(r_2/r_1))
    print((A2*A2 + r_3*r_3 + - A3*A3)/( 2 *A2 * r_3 ))
    psi_2 = math.degrees(math.acos((A2*A2 + r_3*r_3 + - A3*A3)/( 2 *A2 * r_3 )))
    theta2 = psi_1+psi_2

    psi_3 = math.degrees(math.acos((A2*A2 + A3*A3 - r_3 * r_3)/( 2 * A2 * A3 )))
    theta3 = -(180-psi_3)
    
    return theta1,theta2,theta3



def arm_draw(point):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #draw line
    for i in range(len(point)-1):
        ax.plot([point[i][0], point[i+1][0]], [point[i][1],point[i+1][1]],zs=[point[i][2],point[i+1][2]],label='arm '+str(i), markerfacecolor="b",marker="o",linewidth=2)
    
    #draw
    plt.show()



#robot input
point_baseframe = [0,0,0]
point_eof = [5,5,0]

arm_length_1 = 1
arm_length_2 = 5
arm_length_3 = 5

angle_1,angle_2,angle_3 = geometric_invers_kinematic(point_eof[0],point_eof[1],point_eof[2],arm_length_1,arm_length_2,arm_length_3)
print(angle_1,angle_2,angle_3)

x_point_1 = point_baseframe[0]
y_point_1 = point_baseframe[1]
z_point_1 = point_baseframe[2]+arm_length_1

x_point_2 = point_baseframe[0]+arm_length_2*np.sin(np.deg2rad(angle_2))*np.cos(np.deg2rad(angle_1))
y_point_2 = point_baseframe[1]+arm_length_2*np.sin(np.deg2rad(angle_2))*np.sin(np.deg2rad(angle_1))
z_point_2 = point_baseframe[2]+arm_length_2*np.sin(np.deg2rad(angle_2))

#input
point=[point_baseframe,[x_point_1,y_point_1,z_point_1],[x_point_2,y_point_2,z_point_2], point_eof]
arm_draw(point)
