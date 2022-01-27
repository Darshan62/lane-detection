import utils
import cv2

vid = cv2.VideoCapture('5.avi')
utils.create_trackbars([100, 100, 100, 100])

while vid.isOpened():
    _, img = vid.read()
    points = utils.val_trackbars()
    print(points)
    # utils.draw_points(img, points)
    if _:
        cv2.imshow("Image", img)
        print(img.shape)
    else:
       print('no video')
       vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
    cv2.waitKey(1)