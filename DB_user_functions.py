import socket  # Built-in Python library for creating network connections

def connect_to_controller():
    # This function creates a socket and connects to the Controller
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 5000))
        print("Connected to Controller.")
        return s
    except:
        print("ERROR: Could not connect to Controller.")
        return None
    
def send_command(s, message):
    # Sends a command to the Controller and returns the response
    try:
        s.send(message.encode())        # convert text to bytes and send
        response = s.recv(1024).decode() # receive bytes and convert back to text
        return response
    except:
        print("ERROR: Could not send command to Controller.")
        return None
    
def ls_command(s, path):
    # Sends the ls command to the Controller to list files/directories
    message = "ls|" + path
    response = send_command(s, message)
    return response

def mkdir_command(s, path):
    # Sends the mkdir command to the Controller to create a directory
    message = "mkdir|" + path
    response = send_command(s, message)
    return response

def rmdir_command(s, path):
    # Sends the rmdir command to the Controller to remove a directory
    message = "rmdir|" + path
    response = send_command(s, message)
    return response

def save_command(s, filename):
    # Sends the save command to the Controller, expects a REDIRECT back
    message = "save|" + filename
    response = send_command(s, message)
    return response

def read_command(s, filename):
    # Sends the read command to the Controller, expects a REDIRECT back
    message = "read|" + filename
    response = send_command(s, message)
    return response

def delete_command(s, filename):
    # Sends the delete command to the Controller, expects a REDIRECT back
    message = "delete|" + filename
    response = send_command(s, message)
    return response