
import cv2, imutils, socket
import numpy as np
import time
import base64
BUFF_SIZE = 65536

def conn(host_ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
    host_name = socket.gethostname()
    print(host_ip, host_name)
    message = b'Hello'
    client_socket.sendto(message, (host_ip, port))
    return client_socket

def frame(client_socket):
    """Loop."""
    packet, _ = client_socket.recvfrom(BUFF_SIZE)
    data = base64.b64decode(packet, ' /')
    npdata = np.fromstring(data, dtype = np.uint8)
    frame = cv2.imdecode(npdata, 1)
    return frame
        
