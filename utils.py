import cv2
import numpy as np

def none(none):
    """Returns nothing.

    Args:
        none ([NONE]): none
    """
    pass

def warp(img, points, w, h):
    """Warped Image

    Args:
        img ([2D: Array]): [Original Image]
        points ([2D: Array]): [The points for warped image.]
        w ([int]): [width]
        h ([int]): [height]

    Returns:
        ([2D: Array]): [Binary Image]
    """
    pt1 = np.float32(points)
    pt2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    mat = cv2.getPerspectiveTransform(pt1, pt2)
    img = cv2.warpPerspective(img, mat, (w, h))
    return img

def threshold(img):
    """Giving the binary image from the original lane image

    Args:
        img ([2D: Array]): [Original Image]

    Returns:
        ([2D: Array]): [Binary Image]
    """
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_white = np.array([90, 0, 168])
    upper_white = np.array([160, 98, 255])
    img = cv2.inRange(imgHSV, lower_white, upper_white)
    return img

def create_trackbars(ini, wT = 480, hT = 240):  
    """[summary]

    Args:
        ini ([list]): [initial value of points]
        wT (int, optional): [width]. Defaults to 480.
        hT (int, optional): [height]. Defaults to 240.
    """
    cv2.namedWindow("Warp-Meter")
    cv2.resizeWindow("Warp-Meter", 480, 240)
    cv2.createTrackbar("Width TOP", "Warp-Meter", ini[0], wT//2, none)
    cv2.createTrackbar("Height TOP", "Warp-Meter", ini[1], hT, none)
    cv2.createTrackbar("Width BOTTM", "Warp-Meter", ini[2], wT//2, none)
    cv2.createTrackbar("Height BOTTM", "Warp-Meter", ini[3], hT, none)

def val_trackbars(wT = 480, hT = 240):  
    """Returns points for warped image. Trackbars is being used to set the points.

    Args:
        wT (int, optional): [width]. Defaults to 480.
        hT (int, optional): [height]. Defaults to 240.
        
    Returns:
        points ([2D: Array]): [The points for warped image.]
    """
    wt = cv2.getTrackbarPos("Width TOP", "Warp-Meter")
    ht = cv2.getTrackbarPos("Height TOP", "Warp-Meter")
    wb = cv2.getTrackbarPos("Width BOTTM", "Warp-Meter")
    hb = cv2.getTrackbarPos("Height BOTTM", "Warp-Meter")
    
    points = [[wt, ht], [wT-wt, ht], [wb, hb], [wT-wb, hb]]
    return points

def draw_points(img, points):
    """Draw points on image.

    Args:
        img ([2D: Array]): [Original Image]
        points ([2D: Array]): [The points for warped image.]

    """
    cv2.circle(img, (points[0][0], points[0][1]), 5, (255, 0, 171), cv2.FILLED)
    cv2.circle(img, (points[1][0], points[1][1]), 5, (255, 0, 171), cv2.FILLED)
    cv2.circle(img, (points[2][0], points[2][1]), 5, (255, 0, 171), cv2.FILLED)
    cv2.circle(img, (points[3][0], points[3][1]), 5, (255, 0, 171), cv2.FILLED)

def hist(img, disp = False, per = 0.1, region = 4):    
    if region == 1:
        hist_val = np.sum(img, axis = 0)
    else:
        hist_val = np.sum(img[img.shape[0]//region:, :], axis=0)
        
    max_val = np.max(hist_val)
    min_val = per * max_val 
    
    index = np.where(hist_val >= min_val)
    base = int(np.average(index))
    
    if disp:
        hist_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
        for x, intensity in enumerate(hist_val):
            color = (0, 0, 255)
            cv2.line(hist_img, (x, img.shape[0]), (x, int(img.shape[0] - intensity//255//region)), color, 1)
            cv2.circle(hist_img, (base, img.shape[0]), 20, (0, 255, 0), cv2.FILLED)   
        return base, hist_img
    return base
       