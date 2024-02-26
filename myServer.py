import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
ADDR = (HOST, PORT)
SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = "disconnect".lower()

connections = {}
client_addresses = {}

def handle_client(com_socket, addr):
    print(f"[NEW CONNECTION] Connected to {addr}")
    connections[addr] = com_socket
    client_addresses[addr] = com_socket.getpeername()

    connected = True
    while connected:
        msg = com_socket.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            print(f"[ACTIVE CONNECTIONS] {len(connections)}")
        elif msg.startswith("sendto "):
            parts = msg.split()
            if len(parts) >= 4:
                dest_ip = parts[1]
                dest_port = int(parts[2])
                dest_msg = " ".join(parts[3:])
                send_udp_message(dest_ip, dest_port, dest_msg)
        else:
            print(f"Message from client {addr}: {msg}")
            broadcast_message(msg, addr)

    com_socket.close()
    del connections[addr]
    del client_addresses[addr]

def broadcast_message(msg, sender_addr):
    for addr, com_socket in connections.items():
        if addr != sender_addr:
            try:
                com_socket.send(msg.encode(FORMAT))
            except socket.error:
                print(f"Error broadcasting message to {addr}")

def send_udp_message(ip, port, message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), (ip, port))
    udp_socket.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        com_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(com_socket, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {len(connections)}")

if __name__ == "__main__":
    main()
