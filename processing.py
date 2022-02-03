import cv2
import utils
import lane_detect
import server_data
import client_video

def main():
    client_socket = client_video.conn('192.168.1.5', 9999)
    server_socket = server_data.conn('192.168.1.5', 9999)
    ini = [158, 148, 71, 221]
    utils.create_trackbars(ini)
    while True:
        addr = server_data.address(server_socket)
        img = client_video.frame(client_socket)
        img = cv2.resize(img, (480, 240)) # or getting video from raspberry pi
        curve = lane_detect.get_lane(img) # processing
        message = str(curve)
        message = message.encode('utf-8')
        server_data.send(server_socket, message, addr)# getting curve and sending to raspberrypi
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
if __name__ == '__main__':
    main()
        