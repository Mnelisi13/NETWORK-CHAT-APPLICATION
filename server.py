import socket
HOST = '196.47.247.212' # server IP
PORT = 8800
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # server socket for accepting connections
server.bind((HOST,PORT))

server.listen(5)  # 5 unaccepted connections allowed before rejecting new ones
print("The server is listening ...")

while True:   # endless loop for accepting connections
    communication_socket, address = server.accept()  # return the IP adress of the connecting client and a socket we can use to communicate with that client.
    print(f"connected to {address}") # indicating success connection
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Message received! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")