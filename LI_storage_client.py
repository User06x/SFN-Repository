#This is the my storage client python file for the distributed file system
#This file will be in charge of accepting connections from the User Program system and handle the file operations.

import socket  #This is used to create the server and to the handle connections
from LI_storage_functions import save_file, read_file, delete_file, rename_file  #This imports the functions from our storage functions module

#This will set up the server socket and will begin to start listening on port number 12347
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 12347))
ss.listen()

print("The storage client is running and waiting for a connection...")

#TBC