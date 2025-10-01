import socket
import threading
import random
import json

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    
    while True:
        data = client_socket.recv(1024).decode() # Forventet JSON data
        print(f"[DEBUG] Raw data received from client: {data}") # I kommandopromt kan jeg se hvilke data serveren får sendt fra klienten. Dette var blot så jeg kunne se, om JSON virkede som det skulle
        request = json.loads(data) 
        method = request["method"].lower()
        
        if method == "exit":
            break

        num1 = request["Tal1"] # Første tal
        num2 = request["Tal2"] # Andet tal

        if method == "random":
            low = min(num1, num2)
            high = max(num1, num2)
            result = random.randint(low, high)
        elif method == "add":
            result = num1 + num2
        else:
            result = num1 - num2

        client_socket.send(json.dumps({"result": result}).encode()) # Send resultat tilbage til klient i JSON format

    client_socket.close()
    print(f"[DISCONNECTED] {client_address} disconnected.")

def start_server(host="127.0.0.1", port=12000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port}")
    
    while True:
        client_socket, client_address = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    start_server()