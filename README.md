# SFN-Repository
Repository for home assignment commits
-----------------------------------------------------------------------------------------------------------------------------------------
#Distributed File system - Controller Functionalities (Tasnim)
## Distributed File System - Controller (Stage 1)

This project is part of the SFN1 unit and focuses on developing the Controller component of a Distributed File System.

At this stage, the basic structure of the controller has been created. The controller is designed to act as the central component of the system, responsible for managing metadata and coordinating communication between the User Program and the Storage Clients.

## Current Progress

- Basic socket setup implemented
- Controller can start and wait for a connection
- Connection from a client can be accepted
- Initial structure of the program is defined

## Planned Features

The controller will support the following commands in later stages:

- LS – List files and directories
- MKDIR – Create a directory
- RMDIR – Remove a directory
- SAVE – Assign a file to a storage client
- READ – Locate a file and redirect the user
- DELETE – Remove file metadata

## Data Structures (Planned)

- A list to store file metadata
- A list to store storage client details (IP and port)

## Communication

The controller will use socket programming to:
- Receive commands from the User Program
- Process requests
- Send responses based on a defined protocol

## Notes

This is the initial stage of development. The core logic for handling commands and managing metadata will be implemented in the next stages.
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

- Protocol design completed ✅
- Controller structure in progress ⚙️
- Storage Client implementation in progress ⚙️
- User Program implementation starting soon ⏳

---
