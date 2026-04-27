import socket

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