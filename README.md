# SFN-Repository
Repository for home assignment commits
-----------------------------------------------------------------------------------------------------------------------------------------
#Distributed File system - Controller Functionalities (Tasnim)

The controller is the main part of the system. It keeps track of files and storage clients. It does not store files, but decides where files should go and where they can be found.

It receives commands from the user program and sends back the correct response or storage client details.

#Commands:
- LS – list files
- SAVE filename – add file
- READ filename – find file location
- DELETE filename – remove file
- INFO filename – show file details

#Data used:
- storage clients (IP and port)
- file metadata (filename and location)

#How it works:
1. waits for connection
2. receives command
3. processes command
4. sends response
5. closes connection

#Development Progress

This is the first stage of the controller.

At this point, the structure of the program is being set up. The basic idea of how the controller will work has been planned.

The code is still in progress and not all features are implemented yet.
-----------------------------------------------------------------------------------------------------------------------------------------
#Distributed File System - Storage Clients (Luka) 
What is my part for? The storage client/data node will be part of the distributed file system.
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

#How to run my storage client code: (WIP! I'll update this file and send a message on teams once i fully implement the storage client).

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
