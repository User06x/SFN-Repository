nodes = [6001, 6002]
# dictionary to store file metadata
files = {}


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