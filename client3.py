import socket
client = socket.gethostbyname(socket.gethostname())
port = 7070
addr = (client, port)
FORMAT = 'utf-8'
prompt = "hi"

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # communication socket
socket.bind(addr)

msg, address = socket.recvfrom(1024)
print(f"message received: {msg.decode(FORMAT)}")
socket.sendto(f"{prompt}".encode(FORMAT), address)



