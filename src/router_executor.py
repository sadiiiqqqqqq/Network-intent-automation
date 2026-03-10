import socket 
import time 
import serial 
def apply_gns3(commands, port):

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    sock.connect("127.0.0.1",port)
    time.sleep(0.5)
    sock.sendall(b"\r\n")
    time.sleep(1)

    for cmd in commands:
        sock.sendall(cmd + "\r \n")
        time.sleep(0.4) 

    socket.close()


