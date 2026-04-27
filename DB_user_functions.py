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
    
