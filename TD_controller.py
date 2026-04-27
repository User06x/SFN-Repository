import socket
from TD_controller_functions import *

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to controller address
server_socket.bind(("127.0.0.1", 5000))

# listen for connections
server_socket.listen()
print("Controller is waiting for connection...")

# accept connection
client_socket, client_address = server_socket.accept()
print(f"Connected from {client_address}")

# Loop to receive and process commands from the user program
while True:
    data = client_socket.recv(1024)
    message = data.decode()
    print("Received:", message)

    parts = message.split("|")
    command = parts[0]

    if command == "ls":
        response = list_files()
        client_socket.send(response.encode())

    elif command == "save":
        filename = parts[1]
        response = save_file(filename)
        client_socket.send(response.encode())
        
    elif command == "read":
        filename = parts[1]
    response = read_file(filename)
    client_socket.send(response.encode())