import cv2
import utils
import lane_detect
def main():
    vid = cv2.VideoCapture('6.avi')
    ini = [158, 148, 71, 221]
    utils.create_trackbars(ini)
    while vid.isOpened():
        _, img = vid.read()

        if _:
            img = cv2.resize(img, (480, 240)) # or getting video from raspberry pi
            curve = lane_detect.get_lane(img) # processing
            # getting curve and sending to raspberrypi
        else:
            print('no video')
            vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
if __name__ == '__main__':
    main()
        