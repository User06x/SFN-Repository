# SFN-Repository
Repository for home assignment commits
-----------------------------------------------------------------------------------------------------------------------------------------
## Distributed File System - Controller (Tasnim)
## Distributed File System - Controller

This project implements the Controller component of a distributed file system. The controller manages metadata and handles communication between the User Program and Storage Clients.

## Features
- LS – List files  
- MKDIR – Create directory  
- RMDIR – Remove directory  
- SAVE – Assign file to storage node  
- READ – Locate file and redirect  
- DELETE – Remove file metadata  

## Structure
- Main controller handles socket communication  
- Functions are implemented in a separate module for better organization  

## Protocol
Request: COMMAND|ARG  
Response: STATUS|DATA  

Status Codes:
- OK – Success  
- ERROR – Failure  
- REDIRECT – Connect to storage node  

## Notes
Basic error handling is implemented for missing arguments, invalid commands, and file/directory checks. The controller uses IP and port to redirect clients to storage nodes.
-----------------------------------------------------------------------------------------------------------------------------------------
#Distributed File System - Storage Clients (Luka) 
What is my part for? 
The storage client/data node will be part of the distributed file system.
It will act as a form of warehouse that will physically store and gather files, it also checks
for a connection from the user program and handles file operations (FO).

#Files involved for this section of the storage client:
LI_storage_client.py - This will be the main server script that will check for any connections
LI_storage_functions.py - This will be the module that contains all the FO functions

#The type of commands that will be supported from the storage client:
-SAVE filename content - This will save a file to the disk
-READ filename - This will read a file and send it back
-DELETE filename - This will delete a file
-RENAME oldname newname - This will rename a file

#How to run my storage client code:
Run the LI_storage_client.py file and wait for the User Program to connect on port 12347
-----------------------------------------------------------------------------------------------------------------------------------------
#Distributed File system - User Program (Darren)
The User Program acts as the client interface for interacting with the system.

**Responsibilities:**
- Connects to the Controller
- Sends file system commands
- Handles redirects to Storage Clients
- Executes operations on the correct node

**Supported Flow:**
1. Connect to Controller
2. Send command
3. Receive response or redirect
4. If redirected → connect to Storage Client
5. Execute operation

---

## Communication Protocol

The system uses a custom text-based protocol.

**Format:**
- Request: `COMMAND|ARG1|ARG2`
- Response: `STATUS|DATA`

**Status Codes:**
- `OK` – Success
- `ERROR` – Failure
- `REDIRECT` – Connect to Storage Client

See `PROTOCOL.md` for full details.

---

## Development Progress

Protocol design completed ✅
Functions module created (DB_user_functions.py) ✅
Main User Program script created (DB_user_program.py) ✅
Controller commands implemented (ls, mkdir, rmdir, save, read, delete) ✅
Storage Client commands implemented (save, read, delete, append) ✅
Exception handling implemented ✅
Ready for integration testing ⚙️

---
