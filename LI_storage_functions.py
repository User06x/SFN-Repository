#This is my storage functions python file for the distributed file system
#This module will contain all the file system functions that will be used for the Storage Client file

import os  #This will be used for the file operations like deleting and renaming 

#This saves the received data into a file on the disk, then sends back 'OK' or 'ERROR' depending on the outcome.
def save_file(conn, filename, filedata):
    try:
        f = open(filename, "w")
        f.write(filedata)
        f.close()
        response = "SAVE_OK"
        conn.send(response.encode())
    except:
        response = "SAVE_ERROR"
        conn.send(response.encode())

def read_file(conn, filename):
    #This will read a file from the disk and then it will send the content back
    try:
        f = open(filename, "r")
        filedata = f.read()
        f.close()
        conn.send(filedata.encode())
    except:
        response = "READ_ERROR"
        conn.send(response.encode())

def delete_file(conn, filename):
    #This will delete a file from disk, returning back an 'OK' or 'ERROR' text
    try:
        os.remove(filename)
        response = "DELETE_OK"
        conn.send(response.encode())
    except:
        response = "DELETE_ERROR"
        conn.send(response.encode())

def rename_file(conn, oldname, newname):
    #This will rename a file on the disk, return it back with 'OK' or 'ERROR' text
    try:
        os.rename(oldname, newname)
        response = "RENAME_OK"
        conn.send(response.encode())
    except:
        response = "RENAME_ERROR"
        conn.send(response.encode())
