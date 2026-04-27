#This is the my storage client python file for the distributed file system
#This file will be in charge of accepting connections from the User Program system and handle the file operations.

import socket  #This is used to create the server and handle connections
from LI_storage_functions import save_file, read_file, delete_file, append_file  #This imports functions from my storage functions module

#This will set up the server socket and will begin to start listening on port number 6001
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 6001))
ss.listen()

print("Storage Client is running and waiting for connection...")

try:
    ns, addr = ss.accept()  #This will wait for User Program to connect to the Storage Client
    print("User Program connected from", addr)

    while True:  #This will keep looping and waiting for commands from the User Program module
        try:
            message = ns.recv(1024)
            message = message.decode()
            message = message.strip()   #This will remove the '\n' at the end of the message

            parts = message.split("|")  #This will split the message by a pipe separator
            command = parts[0]          #The first part is always the command

            if command == "save":        #This will handle saving a file to the disk
                filename = parts[1]
                filedata = parts[2]
                save_file(ns, filename, filedata)

            elif command == "read":      #This will handle reading a file and sending it back to the user
                filename = parts[1]
                read_file(ns, filename)

            elif command == "delete":    #This will handle the deletion of a file from the disk
                filename = parts[1]
                delete_file(ns, filename)

            elif command == "append":    #This will handle appending data to an already existing file
                filename = parts[1]
                filedata = parts[2]
                append_file(ns, filename, filedata)

            elif command == "quit":      #This will handle disconnections, to stops the loop
                response = "OK|bye\n"
                ns.send(response.encode())
                print("User Program disconnected.")
                break

            else:                        #This will handle any command which is not recognised
                response = "ERROR|unknown command\n"
                ns.send(response.encode())

        except:
            print("Error receiving message from User Program.")
            break

except:
    print("Error accepting connection.")

