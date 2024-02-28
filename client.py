import socket

HOST = "196.47.247.212"  # server IP
PORT = 9090

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Connected to the server {HOST}")

    while True:
        msg = input("Enter a message (type 'exit' to quit): ")

        if msg == "exit":
            client_socket.send(msg.encode('utf-8'))
            break

        client_socket.send(msg.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

except ConnectionRefusedError:
    print("Connection to the server was refused. Please make sure the server is running and the correct IP and port are used.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    client_socket.close()
