#This is my storage functions python file for the distributed file system
#This module will contain all the file system functions that will be used for the Storage Client file

import os  #This will be used for the file operations like deleting and renaming 

#This saves the received data into a file on the disk, then sends back 'OK' or 'ERROR' depending on the outcome.
def save_file(conn, filename, filedata):
    try:
        f = open(filename, "w")
        f.write(filedata)
        f.close()
        response = "OK|saved\n"
        conn.send(response.encode())
    except:
        response = "ERROR|could not save file\n"
        conn.send(response.encode())

def read_file(conn, filename):
    #This will read a file from disk and send its content back to the user
    try:
        f = open(filename, "r")
        filedata = f.read()
        f.close()
        conn.send(filedata.encode())
    except:
        response = "ERROR|could not read file\n"
        conn.send(response.encode())

def delete_file(conn, filename):
    #This will delete a file from the disk, and send back 'OK' or 'ERROR' depending on the outcome
    try:
        os.remove(filename)
        response = "OK|deleted\n"
        conn.send(response.encode())
    except:
        response = "ERROR|could not delete file\n"
        conn.send(response.encode())

def append_file(conn, filename, filedata):
    #This will append the data to an already existing file, then send back 'OK' or 'ERROR' depending on the outcome
    try:
        f = open(filename, "a")
        f.write(filedata)
        f.close()
        response = "OK|appended\n"
        conn.send(response.encode())
    except:
        response = "ERROR|could not append to file\n"
        conn.send(response.encode())
