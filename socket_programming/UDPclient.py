from socket import *
server_name = 'Tunwongchai'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lower case sentence : ')
clientSocket.sendto(message.encode(), (server_name, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Server message: " + modifiedMessage.decode())
clientSocket.close()