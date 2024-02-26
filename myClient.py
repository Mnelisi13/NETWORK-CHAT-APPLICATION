import socket

HOST = "196.42.73.170"  # Host IP address
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
        msg = input("Enter a message (type 'disconnect' to disconnect from server OR type 'connections' to view active clients):\n")
        client.send(msg.encode(FORMAT))
        if msg == DISCONNECT_MSG:
            connected = False
        elif msg == "connections":
            connections_msg = client.recv(SIZE).decode(FORMAT)
            print(f"Active connections:\n{connections_msg}")
        else:
            recipient = input("Enter the recipient's IP address and port number (e.g., '192.168.1.1:9090'):\n")
            udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            recipient_ip, recipient_port = recipient.split(":")
            udp_client.sendto(msg.encode(FORMAT), (recipient_ip, int(recipient_port)))
            udp_client.close()

    client.close()


if __name__ == "__main__":
    main()
