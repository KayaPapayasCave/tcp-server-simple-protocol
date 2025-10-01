import socket
import threading
import random

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.") # Printer når en ny klient forbinder
    
    while True:
        command = client_socket.recv(1024).decode().strip() # Modtag kommando fra klienten
        if command.lower() == "exit": # Hvis klient vil lukke forbindelsen
            print(f"[DISCONNECTED] {client_address} requested exit.")
            break

        client_socket.send("Input numbers".encode()) # Send prompt til klienten, der beder om to tal
        numbers = client_socket.recv(1024).decode().strip() # Modtag to tal fra klienten
        num1, num2 = map(int, numbers.split()) # Split og konverter til int
        
        if command.lower() == "random": # Generer tilfældigt tal mellem num1 og num2, inklusiv begge. Den fejler hvis num2 > num1
            result = str(random.randint(num1, num2))
        elif command.lower() == "add": # Plus
            result = str(num1 + num2)
        else:  # Minus
            result = str(num1 - num2)
        
        client_socket.send(result.encode()) # Send resultat tilbage til klienten
    
    client_socket.close() # Luk forbindelsen til klienten
    print(f"[DISCONNECTED] {client_address} disconnected.") # Printer når en klient afbryder forbindelsen

def start_server(host="127.0.0.1", port=12000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Opret TCP socket
    server.bind((host, port)) # Bind til host og port
    server.listen() # Lyt efter forbindelser
    print(f"[LISTENING] Server is listening on {host}:{port}")
    
    while True:
        client_socket, client_address = server.accept() # Accepter en ny klientforbindelse
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start() # Håndter klienten i en ny tråd, så flere klienter kan forbindes samtidigt

if __name__ == "__main__":
    start_server() # Start serveren
