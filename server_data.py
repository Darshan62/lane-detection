import socket

def conn(host_ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65535)
    print('Socket Created ')
    server_socket.bind((host_ip, port))
    print('Waiting for conn: ')
    return server_socket


def address(server_socket):
    """Loop."""
    msg, addr = server_socket.recvfrom(65535)
    print('GOT: ', addr)
    return addr

def send(server_socket, message, addr):
    server_socket.sendto(message, addr)   