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

#TBC