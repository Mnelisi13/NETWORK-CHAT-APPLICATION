import socket

HOST = "196.47.247.212"  #  server IP
PORT = 9090
msg = input("msg: ")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))
print(f"connected to server {HOST}")
socket.send(msg.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))