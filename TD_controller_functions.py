nodes = [6001, 6002]
# dictionary to store file metadata
files = {}
directories = []


def list_files():
    if len(files) == 0:
        return "OK|"
    
    result = ",".join(files.keys())
    return f"OK|{result}"

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
    # choose first storage node
    node = nodes[0]
    
    # store file metadata
    files[filename] = node
    
    # return redirect response
    return "REDIRECT|127.0.0.1|" + str(node)

def read_file(filename):
    # check if file exists in metadata
    if filename in files:
        node = files[filename]
        return "REDIRECT|127.0.0.1|" + str(node)
    else:
        return "ERROR|File not found"
    
def delete_file(filename):
    # check if file exists
    if filename in files:
        node = files[filename]

        # remove file from metadata
        del files[filename]

        # return redirect to storage
        return "REDIRECT|127.0.0.1|" + str(node)
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
    if dirname in files and files[dirname] == "dir":
        del files[dirname]
        return "OK|removed"
    else:
        return "ERROR|Directory not found"
    

      