import socket
#Client
#UDP messaging
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message, address = client.recvfrom(1024)[0]
print(message.decode('utf-8'))
client2IP = input("Enter the client you want to send a message to's IP address\n")
client2Port =eval(input("Enter the port number of the client:\n"))
messageTo =input("Enter the message: ")
client.sendto(messageTo.encode(), (client2IP, client2Port))
 
#Add connection to server using TCP!
