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

    # check if client disconnected
    if not data:
       client_socket.close()
       break

    message = data.decode()
    # handle quit command
    if message == "quit":
        response = "OK|bye"
        client_socket.send(response.encode())
        client_socket.close()
        break
    print("Received:", message)

    # split message
    parts = message.split("|")
    command = parts[0]

    if command == "ls":
        response = list_files()
        client_socket.send(response.encode())

    elif command == "save":
        if len(parts) > 1:
            filename = parts[1]
            response = save_file(filename)
        else:
            response = "ERROR|Missing filename"
        client_socket.send(response.encode())

    elif command == "read":
        if len(parts) > 1:
            filename = parts[1]
            response = read_file(filename)
        else:
            response = "ERROR|Missing filename"
        client_socket.send(response.encode())

    elif command == "delete":
        if len(parts) > 1:
            filename = parts[1]
            response = delete_file(filename)
        else:
            response = "ERROR|Missing filename"
        client_socket.send(response.encode())

    elif command == "mkdir":
        if len(parts) > 1:
            dirname = parts[1]
            response = make_directory(dirname)
        else:
            response = "ERROR|Missing directory name"
        client_socket.send(response.encode())

    elif command == "rmdir":
        if len(parts) > 1:
            dirname = parts[1]
            response = rmdir_command(dirname)
        else:
            response = "ERROR|Missing directory name"
        client_socket.send(response.encode())

    else:
        response = "ERROR|Unknown command"
        client_socket.send(response.encode())



