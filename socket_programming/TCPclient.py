from socket import *
serverName = "192.168.1.4"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence =input("Input lower case sentence: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server: " + modifiedSentence.decode())
clientSocket.close()