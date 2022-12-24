import matplotlib.pyplot as plt
import numpy as np


def arm_draw(point):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #draw line
    for i in range(len(point)-1):
        ax.plot([point[i][0], point[i+1][0]], [point[i][1],point[i+1][1]],zs=[point[i][2],point[i+1][2]],label='arm '+str(i), markerfacecolor="b",marker="o",linewidth=2)
    
    #draw
    plt.show()



#robot input
point_baseframe = [0,0,5]
arm_length_1 = 5
arm_length_2 = 5
angle_1 = 45
angle_2 = 45


x_point_2 = point_baseframe[0]+arm_length_1*np.sin(np.deg2rad(angle_2))*np.cos(np.deg2rad(angle_1))
y_point_2 = point_baseframe[1]+arm_length_1*np.sin(np.deg2rad(angle_2))*np.sin(np.deg2rad(angle_1))
z_point_2 = point_baseframe[2]+arm_length_1*np.sin(np.deg2rad(angle_2))

x_point_3 = x_point_2+arm_length_2*np.sin(np.deg2rad(angle_2))*np.cos(np.deg2rad(angle_1))
y_point_3 = y_point_2+arm_length_2*np.sin(np.deg2rad(angle_2))*np.sin(np.deg2rad(angle_1))
z_point_3 = z_point_2+arm_length_2*np.sin(np.deg2rad(angle_2))

#input
point=[point_baseframe, [x_point_2,y_point_2,z_point_2]]
arm_draw(point)
