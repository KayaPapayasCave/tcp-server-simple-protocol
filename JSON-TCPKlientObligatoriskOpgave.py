from socket import *
import json

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 12000))

while True:
    method = input('Enter method "add", "subtract", "random" or "exit": ')
    if method.lower() == "exit":
        clientSocket.send(json.dumps({"method": "exit"}).encode()) # Send exit kommando til server i JSON format
        break

    Tal1 = int(input("Enter first number: "))
    Tal2 = int(input("Enter second number: "))

    request = {"method": method, "Tal1": Tal1, "Tal2": Tal2} # Opret JSON request
    clientSocket.send(json.dumps(request).encode()) # Send request til server i JSON format

    response = json.loads(clientSocket.recv(1024).decode()) # Modtag response fra server i JSON format
    print(f"Result from server: {response['result']}")

clientSocket.close()