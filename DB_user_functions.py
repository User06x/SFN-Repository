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
    
