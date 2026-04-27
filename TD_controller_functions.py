nodes = [6001, 6002]
# dictionary to store file metadata
files = {}


def list_files():
    if len(files) == 0:
        return "OK|"
    
    result = ",".join(files.keys())
    return f"OK|{result}"