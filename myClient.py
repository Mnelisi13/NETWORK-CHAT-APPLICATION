import socket

HOST = socket.gethostbyname(socket.gethostname())  # Host IP address
PORT = 9090
ADDR = (HOST, PORT)
SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = "Disconnect".lower()



def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {HOST}:{PORT}")

    connected = True
    while connected:
        msg = input("Enter a message (type 'disconnect' to disconnect from server OR type \"connections\" to view active clients):\n")
        client.send(msg.encode(FORMAT))
        if msg == DISCONNECT_MSG:
            connected = False

        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"Message from server {ADDR}: {msg} ")


if __name__ == "__main__":
    main()
