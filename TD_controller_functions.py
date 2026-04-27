# storage nodes with IP and port
nodes = [
    {"ip": "127.0.0.1", "port": 6001},
    {"ip": "127.0.0.1", "port": 6002}
]
# dictionary to store file metadata
files = {}
directories = []



def list_files():
    # return empty response if no files exist
    if len(files) == 0:
        return "OK|"
    
    result = ""
    
    for name in files:
        result = result + name + ","
    
    # remove trailing comma and format response
    result = result[:-1]
    
    return "OK|" + result

def save_file(filename):
    node = nodes[0]
    files[filename] = node["port"]
    return "REDIRECT|" + node["ip"] + "|" + str(node["port"])
   
   
def read_file(filename):
    if filename in files:
        port = files[filename]
        ip = "127.0.0.1"
        return "REDIRECT|" + ip + "|" + str(port)
    else:
        return "ERROR|File not found"
    
def delete_file(filename):
    # check if file exists
    if filename in files:
        del files[filename]
        return "OK|deleted"
    else:
        return "ERROR|File not found"
    
def make_directory(name):
    # check if directory already exists
    if name not in directories:
        directories.append(name)
        return "OK|Directory created"
    else:
        return "ERROR|Directory already exists"

def rmdir_command(dirname):
    # check if directory exists
    if dirname in directories:
        directories.remove(dirname)
        return "OK|removed"
    else:
        return "ERROR|Directory not found"

      