#This is the my storage client python file for the distributed file system
#This file will be in charge of accepting connections from the User Program system and handle the file operations.

import socket  #This is used to create the server and to the handle connections
from LI_storage_functions import save_file, read_file, delete_file, rename_file  #This imports the functions from our storage functions module

#This will set up the server socket and will begin to start listening on port number 12347
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 12347))
ss.listen()

print("The storage client is running and waiting for a connection...")

try:
    ns, addr = ss.accept()  #This will wait for User Program to connect to the Storage Client
    print("User Program connected from", addr)

    while True:  #This will keep receiving and handling commands until the EXIT option is chosen 
        try:
            message = ns.recv(1024)
            message = message.decode()

            if message.startswith("SAVE"):    #This handles the file saving to disk section
                parts = message.split(" ", 2)
                filename = parts[1]
                filedata = parts[2]
                save_file(ns, filename, filedata)

            elif message.startswith("READ"):    #This will handle the file reading and sending it back 
                parts = message.split(" ", 1)
                filename = parts[1]
                read_file(ns, filename)

            elif message.startswith("DELETE"):     #This handles the deletion of a file from the disk
                parts = message.split(" ", 1)
                filename = parts[1]
                delete_file(ns, filename)

            elif message.startswith("RENAME"):     #This handles the renaming of a file inside the disk
                parts = message.split(" ", 2)
                oldname = parts[1]
                newname = parts[2]
                rename_file(ns, oldname, newname)

            elif message == "EXIT":     #This handles the disconnection and stops the loops
                print("User Program disconnected.")
                break

            else:    #This will handle any unrecognised commands
                response = "UNKNOWN_COMMAND"
                ns.send(response.encode())

        except:
            print("Error receiving message from User Program.")
            break

except:
    print("Error accepting connection.")

#TBC
