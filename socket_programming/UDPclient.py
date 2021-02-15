from socket import *
server_name = '192.168.1.4'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 5432))
message = input('Input lower case sentence : ')
clientSocket.sendto(message.encode(), (server_name, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Server message: " + modifiedMessage.decode())
clientSocket.close()