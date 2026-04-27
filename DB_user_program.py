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

def main():
    print("Starting User Program...")

    # Connect to Controller
    controller = connect_to_controller()
    if controller is None:
        print("Could not connect to Controller. Exiting.")
        return

    while True:
        show_menu()
        choice = input("Choose an option: ")
        try:
            if choice == "1":
                # LS - list files
                path = input("Enter path (press Enter for root '/'): ")
                if path == "":
                    path = "/"
                response = ls_command(controller, path)
                print("Response:", response)

            elif choice == "2":
                # MKDIR - make directory
                path = input("Enter directory name to create: ")
                response = mkdir_command(controller, path)
                print("Response:", response)

            elif choice == "3":
                # RMDIR - remove directory
                path = input("Enter directory name to remove: ")
                response = rmdir_command(controller, path)
                print("Response:", response)
            
            elif choice == "4":
                # SAVE - controller redirects to storage client
                filename = input("Enter filename to save: ")
                response = save_command(controller, filename)
                print("Controller response:", response)
                redirect = parse_redirect(response)
                if redirect:
                    host, port = redirect
                    sc = connect_to_storage(host, port)
                    if sc:
                        content = input("Enter content to save: ")
                        result = storage_save(sc, filename, content)
                        print("Response:", result)
                        
            elif choice == "5":
                # READ
                filename = input("Enter filename to read: ")
                response = read_command(controller, filename)
                print("Controller response:", response)
                redirect = parse_redirect(response)
                if redirect:
                    host, port = redirect
                    sc = connect_to_storage(host, port)
                    if sc:
                        result = storage_read(sc, filename)
                        print("File content:", result)
                        quit_storage(sc)

            elif choice == "6":
                # DELETE
                filename = input("Enter filename to delete: ")
                response = delete_command(controller, filename)
                print("Controller response:", response)
                redirect = parse_redirect(response)
                if redirect:
                    host, port = redirect
                    sc = connect_to_storage(host, port)
                    if sc:
                        result = storage_delete(sc, filename)
                        print("Response:", result)
                        quit_storage(sc)

            elif choice == "7":
                # QUIT
                quit_controller(controller)
                print("Goodbye!")
                break

            else:
                print("Unknown option. Please choose 1-7.")

        except:
            print("ERROR: Something went wrong. Please try again.")
                        
main()
    
        
