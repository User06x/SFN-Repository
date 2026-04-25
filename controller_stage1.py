import socket  # Library for socket programming

# Creating a new socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to IP and Port
server_socket.bind(('127.0.0.1', 5000))

# Set the socket to listening mode
server_socket.listen()
print("Controller waiting for client...")

# Accept connection
client_socket, client_address = server_socket.accept()
print(f"A client connected from: {client_address}")

# =========================
# COMMAND FUNCTIONS
# =========================

def ls_command(parts):
    return "OK|"

def mkdir_command(parts):
    return "OK|"

def rmdir_command(parts):
    return "OK|"

def save_command(parts):
    return "REDIRECT|"

def read_command(parts):
    return "REDIRECT|"

def delete_command(parts):
    return "REDIRECT|"

# =========================
# MAIN LOOP
# =========================

while (True):

    message_received_bytes = client_socket.recv(1024)
    message_received_string = message_received_bytes.decode()

    print(f"Received from Client: {message_received_string}")

    if message_received_string == "quit":
        response = "OK|bye"
        client_socket.send(response.encode())
        client_socket.close()
        break

    # Split command
    parts = message_received_string.split("|")
    command = parts[0]

    # Process command
    if command == "ls":
        response = ls_command(parts)

    elif command == "mkdir":
        response = mkdir_command(parts)

    elif command == "rmdir":
        response = rmdir_command(parts)

    elif command == "save":
        response = save_command(parts)

    elif command == "read":
        response = read_command(parts)

    elif command == "delete":
        response = delete_command(parts)

    else:
        response = "ERROR|Unknown command"

    # Send response
    client_socket.send(response.encode())