import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())  # Host IP address
PORT = 9090
ADDR = (HOST, PORT)
SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = "disconnect"
VIEW_CONNECTIONS_MSG = "connections"

# Array list to store the connections
connections = []


def handle_client(com_socket, addr):
    print(f"[NEW CONNECTION] The server is connected to {addr} ")
    connections.append(addr)  # Add new connection ADDR to the list

    connected = True
    while connected:
        msg = com_socket.recv(SIZE).decode(FORMAT).lower()  # Convert received message to lowercase
        # message received from the communication client socket
        if msg.lower() == DISCONNECT_MSG:
            connected = False
            print(f"[DISCONNECTION] The server is disconnected from {addr}")

        elif msg.lower() == VIEW_CONNECTIONS_MSG:
            response = f"Current connections: {connections}"
            com_socket.send(response.encode(FORMAT))

        else:
            print(f"Message from client {addr}: {msg}")
            msg = f"Message received is \"{msg}\""
            com_socket.send(msg.encode(FORMAT))

    com_socket.close()
    connections.remove(addr)  # Remove the connection ADDR from the list after disconnection


def main():
    print("[STARTING] the server is starting...")
    '''starting a TCP socket'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating server socket for accepting connections
    server.bind(ADDR)  # bind/associate the server socket with the ADDR for identification
    server.listen()   # listen for any client trying to connect to server
    print(f"[LISTENING] the server is listening on {HOST}:{PORT} \n")

    while True:
        com_socket, addr = server.accept()  # server accept connection from communication socket.

        # create a separate thread for the server to handle the accepted client.
        thread = threading.Thread(target=handle_client, args=(com_socket, addr))
        thread.start()
        # print the number of active connections/ number of threads
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # minus the main thread
        print(f"Current connections: {connections}")


if __name__ == "__main__":
    main()
