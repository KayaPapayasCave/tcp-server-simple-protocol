from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM) # Opret TCP klient socket
clientSocket.connect(('localhost', 12000))  # Forbind til serveren på port 12000

while True:
    command = input('Enter method "add", "subtract", "random" or "exit": ') # Få kommando fra bruger
    clientSocket.send(command.encode()) # Send kommando til server

    if command.lower() == 'exit': # Hvis brugeren vil afslutte
        print('Exiting client.')
        break

    prompt = clientSocket.recv(1024).decode() # Modtag prompt fra server
    print(f'Server: {prompt}')

    numbers = input('Enter two numbers separated by space: ') # Få to tal fra bruger
    clientSocket.send(numbers.encode()) # Send tallene til server

    result = clientSocket.recv(1024).decode() # Modtag resultat fra server
    print(f'Result from server: {result}')

clientSocket.close() # Luk klient socket