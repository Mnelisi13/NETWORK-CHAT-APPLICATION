import socket


def main():
    client_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_1_ip = input("Enter the IP address of client 1: ")
    client_1_port = eval(input("Enter the port # of client 1: "))
    client_1_addr = (client_1_ip, client_1_port)
    print(f"[LISTENING] Client 1 is listening on {client_1_ip}:{client_1_port}")

    client_2_ip = input("Enter the IP address of client 2: ")
    client_2_port = eval(input("Enter the port # of client 2: "))
    client_2_addr = (client_2_ip, client_2_port)

    while True:
        msg = input("Enter a message (type 'disconnect' to exit): ")
        if msg.lower() == "disconnect":
            break
        client_1.sendto(msg.encode('utf-8'), client_2_addr)
        msg, client_addr = client_1.recvfrom(1024)
        print(f"Message from client 2: {msg.decode('utf-8')}")


if __name__ == "__main__":
    main()

