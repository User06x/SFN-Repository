# SFN1 Distributed File System — Communication Protocol

This document is the shared agreement between the three scripts:
Controller (Tasnim), Storage Client (Luke), and User Program (Darren).

Any change to this file should be agreed by all three team members.

---

## 1. Network Configuration

| Role             | Host        | Port  |
|------------------|-------------|-------|
| Controller       | 127.0.0.1   | 5000  |
| Storage Client 1 | 127.0.0.1   | 6001  |
| Storage Client 2 | 127.0.0.1   | 6002  |

For the demo everything runs on `localhost`. Storage Client ports can
be extended if we add more nodes.

---

## 2. Message Format

All messages are plain-text strings encoded in UTF-8 and terminated with
a newline character (`\n`). Fields within a message are separated by
the pipe character (`|`).

- **Request**:  `COMMAND|ARG1|ARG2|...`
- **Response**: `STATUS|DATA`

### Response status values

| STATUS    | Meaning                                                     |
|-----------|-------------------------------------------------------------|
| `OK`      | Success. `DATA` contains the result (may be empty).         |
| `ERROR`   | Failure. `DATA` contains a human-readable error message.    |
| `REDIRECT`| Controller only. `DATA` = `host|port` of a Storage Client.  |

---

## 3. Controller Commands (User Program → Controller)

The Controller must accept at least these six commands:

| # | Request                    | Typical Response                 | Notes                                    |
|---|----------------------------|----------------------------------|------------------------------------------|
| 1 | `ls|<path>`                | `OK|file1,file2,dir1/`           | Controller answers from metadata.        |
| 2 | `mkdir|<path>`             | `OK|created` or `ERROR|...`      | Controller updates metadata only.        |
| 3 | `rmdir|<path>`             | `OK|removed` or `ERROR|...`      | Must be empty dir.                       |
| 4 | `save|<filename>`          | `REDIRECT|host|port`             | Controller picks a Storage Client.       |
| 5 | `read|<filename>`          | `REDIRECT|host|port`             | Controller looks up which node has it.   |
| 6 | `delete|<filename>`        | `REDIRECT|host|port`             | Same lookup as `read`.                   |

After a `REDIRECT`, the User Program **disconnects from the Controller**
and connects to the returned Storage Client.

---

## 4. Storage Client Commands (User Program → Storage Client)

The Storage Client must accept at least these four commands:

| # | Request                         | Typical Response            |
|---|---------------------------------|-----------------------------|
| 1 | `save|<filename>|<content>`     | `OK|saved` or `ERROR|...`   |
| 2 | `read|<filename>`               | `OK|<content>` or `ERROR|...` |
| 3 | `delete|<filename>`             | `OK|deleted` or `ERROR|...` |
| 4 | `append|<filename>|<content>`   | `OK|appended` or `ERROR|...`|

The Storage Client does **not** handle `ls` — that stays on the Controller.

---

## 5. Disconnect

Either side may send `quit` to request a clean close. The receiver
responds `OK|bye` and closes the socket.

---

## 6. Example Session

```
User -> Controller : save|notes.txt
Controller -> User : REDIRECT|127.0.0.1|6001
(User disconnects from Controller, connects to 127.0.0.1:6001)
User -> Storage   : save|notes.txt|Hello world
Storage -> User   : OK|saved
```
