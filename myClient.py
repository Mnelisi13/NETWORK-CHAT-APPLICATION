import socket

options = eval(input("Select the number of the end-system you would like to communicate with and hit enter:\n1.Server\n2.Client\n>> "))

SIZE = 1024
FORMAT = 'utf-8'
DISCONNECT_MSG = "disconnect"


def main():
    """ TCP """
    if options == 1:
        HOST = input("Enter the IP Address of the server you wish to establish a connection with: ")  # Host IP address
        PORT = eval(input("Enter the PORT # of the server: "))
        ADDR = (HOST, PORT)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # client communication socket
        try:
            client.connect(ADDR)  # connecting the client to the server
            print(f"\n[CONNECTED] Client connected to server at {HOST}:{PORT}")
        except socket.gaierror:
            print(f"Server {ADDR} can't be reached!!!")
            return

        connected = True
        while connected:
            msg = input("Enter a message (type 'disconnect' to disconnect from server OR type \"connections\" to view active clients):\n")
            client.send(msg.encode(FORMAT))
            if msg.lower() == DISCONNECT_MSG:
                connected = False

            else:
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"Message from server {ADDR}: {msg} ")

    elif options == 2:
        """ UDP """
        CLIENT = input("Enter the IP Address of the client you wish to send a message to: ")  # Host IP address
        PORT = eval(input("Enter the PORT # of the client: "))
        ADDR = (CLIENT, PORT)

        client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_udp.bind(ADDR)

        active = True  # active to send and receive messages
        while active:
            data = input("Enter a message (Type \"deactivate\" to exit): ")
            if data.lower() == "deactivate":
                active = False
            else:
                '''Sending the data'''
                data = data.encode(FORMAT)
                client_udp.sendto(data, ADDR)

                '''Receiving the data'''
                print(client_udp.recvfrom(1024)[0].decode(FORMAT))

    else:
        print("You have entered an invalid number!!!")


if __name__ == "__main__":
    main()
