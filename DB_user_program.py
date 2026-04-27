# This is the main User Program script for the Distributed File System
from DB_user_functions import *

def show_menu():
    print("\n=============================")
    print("   Distributed File System   ")
    print("=============================")
    print("1. List files (ls)")
    print("2. Make directory (mkdir)")
    print("3. Remove directory (rmdir)")
    print("4. Save a file")
    print("5. Read a file")
    print("6. Delete a file")
    print("7. Quit")
    print("=============================")
