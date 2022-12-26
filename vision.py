from __future__ import print_function
import cv2 as cv
import argparse
import imutils

max_value = 255
max_value_H = 360//2
low_H = 24
low_S = 108
low_V = 144
high_H = max_value_H
high_S = max_value
high_V = max_value
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
window_detection_binary_name = 'Object Detection Binary'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

iteration_erode_L = 2
iteration_erode_H = 255
iteration_erode_name = 'it_erode'

iteration_dilate_L = 2
iteration_dilate_H = 50
iteration_dilate_name = 'it_dilate'

def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)
def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)
def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)
def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)
def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)

def on_iteration_erode_trackbar(val):
    pass

def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth


parser = argparse.ArgumentParser(description='Human Robot Tracking.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)

cv.namedWindow(window_capture_name,cv.WINDOW_NORMAL)
cv.namedWindow(window_detection_name,cv.WINDOW_NORMAL)
cv.namedWindow(window_detection_binary_name,cv.WINDOW_NORMAL)
cv.resizeWindow(window_detection_binary_name,640,480)


cv.createTrackbar(low_H_name, window_detection_name , low_H, max_value_H, on_low_H_thresh_trackbar)
cv.createTrackbar(high_H_name, window_detection_name , high_H, max_value_H, on_high_H_thresh_trackbar)
cv.createTrackbar(low_S_name, window_detection_name , low_S, max_value, on_low_S_thresh_trackbar)
cv.createTrackbar(high_S_name, window_detection_name , high_S, max_value, on_high_S_thresh_trackbar)
cv.createTrackbar(low_V_name, window_detection_name , low_V, max_value, on_low_V_thresh_trackbar)
cv.createTrackbar(high_V_name, window_detection_name , high_V, max_value, on_high_V_thresh_trackbar)

cv.createTrackbar(iteration_erode_name, window_detection_name , iteration_erode_L, iteration_erode_H,on_iteration_erode_trackbar)
cv.createTrackbar(iteration_dilate_name, window_detection_name , iteration_dilate_L, iteration_dilate_H,on_iteration_erode_trackbar)


# Set default value for Max HSV trackbars for green color
cv.setTrackbarPos(low_H_name, window_detection_name, 24)
cv.setTrackbarPos(low_S_name, window_detection_name, 108)
cv.setTrackbarPos(low_V_name, window_detection_name, 144)

cv.setTrackbarPos(high_H_name, window_detection_name, 64)
cv.setTrackbarPos(high_S_name, window_detection_name, 255)
cv.setTrackbarPos(high_V_name, window_detection_name, 255)

cv.setTrackbarPos(iteration_erode_name, window_detection_name, 2)
cv.setTrackbarPos(iteration_dilate_name, window_detection_name, 2)
distance=0
flag_break=0
# def update_vision():
# global distance
#     global flag_break
threshValue_erode = cv.getTrackbarPos(iteration_erode_name, window_detection_name)
threshValue_dilation = cv.getTrackbarPos(iteration_dilate_name, window_detection_name)
while(1):
    ret, frame = cap.read()
    width  = cap.get(cv.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)  # float `height`
    print(width,height)
    # new_h = height / 2
    # new_w = width / 2
    # frame = cv.resize(frame, (new_w, new_h))
    if frame is None:
        break
        # return None

    frame = cv.flip(frame, 1)
    frame_blurred = cv.GaussianBlur(frame, (11, 11), 0)
    frame_HSV = cv.cvtColor(frame_blurred, cv.COLOR_BGR2HSV)
    frame_threshold_mask = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    frame_threshold_mask = cv.erode(frame_threshold_mask, None, iterations=threshValue_erode)
    frame_threshold_mask = cv.dilate(frame_threshold_mask, None, iterations=threshValue_dilation)
    
    cnts = cv.findContours(frame_threshold_mask.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
	# only proceed if at least one contour was found
    if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
        c = max(cnts, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        marker = cv.minAreaRect(c)
        dimension = marker[1]
        M = cv.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		# only proceed if the radius meets a minimum size
        if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
            cv.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv.circle(frame, center, 5, (0, 0, 255), -1)
            cv.putText(frame, str(center), center, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)

    #Distance Calculation
    if center:
        #Uncomment for Calibrations
        # KNOWN_DISTANCE = 30 #cm
        # KNOWN_WIDTH = 10 #cm
        # focalLength = (dimension[0] * KNOWN_DISTANCE) / KNOWN_WIDTH
        # print(focalLength)

        #Distance Running
        FOCALLENGTH = 10
        KNOWN_WIDTH = 10 #cm
        
        distance = distance_to_camera(KNOWN_WIDTH, FOCALLENGTH, dimension[0])
        print(center,dimension)
    else:
        distance = 0


    cv.imshow(window_detection_binary_name, frame_threshold_mask)
    cv.imshow(window_capture_name, frame)
    
    
    
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        # flag_break = 1
        break

    # return flag_break,distance