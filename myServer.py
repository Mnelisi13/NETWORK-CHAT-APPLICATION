import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())  # Host IP address
PORT = 9090
ADDR = (HOST, PORT)
SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"


def handle_client(com_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = com_socket.recv(SIZE).decode('utf-8')
        # message received from the communication client socket
        if msg == DISCONNECT_MSG:
            connected = False
        print(f"[{addr}] {msg}")
        msg = f"Message received: {msg}"
        com_socket.send(msg.encode(FORMAT))
    com_socket.close()


def main():
    print("[STARTING] the server is starting..." )
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating server socket for accepting connections
    server.bind(ADDR)  # bind/associate the server socket with the ADDR for identification
    server.listen()   # listen for any client trying to connect to server
    print(f"[LISTENING] the server is listening on {HOST}:{PORT}")

    while True:
        com_socket, addr = server.accept()  # server accept connection from communication socket.

        # create a separate thread for the server to handle the accepted client.
        thread = threading.Thread(target=handle_client, args=(com_socket, addr))
        thread.start()
        # print the number of active connections/ number of threads
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # minus the main thread


if __name__ == "__main__":
    main()