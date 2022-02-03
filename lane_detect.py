import cv2
import numpy as np
import utils

curve_list = [] 
avg_val = 10

def get_lane(img):
    """Videos from raspberry pi gets processed in main PC using this function and returns curve value."""
    # Thresholding and Warping 
    h, w, c = img.shape
    points = utils.val_trackbars()
    imgThres = utils.threshold(img)
    imgWarp = utils.warp(imgThres, points, w, h)
    utils.draw_points(img, points) 
    # print(points)
    
    #  Histogram
    mid, hist_img = utils.hist(imgWarp, disp=True, per=0.5, region=1)
    curve_avg, hist_img = utils.hist(imgWarp, disp=True, per=0.9)
    
    curve_raw = curve_avg - mid
    
    curve_list.append(curve_raw)
    if len(curve_list) > avg_val:
        curve_list.pop(0)
    curve = int(sum(curve_list)/len(curve_list))/100
    if curve>1: curve ==1
    if curve<-1:curve == -1

    
    cv2.putText(hist_img, str(curve), (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))
    
    # Stack
    hstack1 = np.hstack((imgThres, imgWarp))
    hstack2 = np.hstack((hist_img, img))
    
    cv2.imshow('Capture1', hstack1)
    cv2.imshow('Capture2', hstack2)
    
    return curve


