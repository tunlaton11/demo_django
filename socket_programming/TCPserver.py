from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive requests")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    modifiedSentence = sentence.upper()
    print("Client message: " + modifiedSentence)
    connectionSocket.send(modifiedSentence.encode())
    connectionSocket.close()
