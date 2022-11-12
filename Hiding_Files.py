import os
import time
import sys

if sys.platform.lower() == 'win32':

    def enclose(cf, hf):
        '''
        This function encloses the hidden file within the cover file and asks the user for permission to delete the hidden file
        '''

        cmd_enclose = 'type ' + hf + " > " + cf + ":" + hf
        os.system(cmd_enclose)

        permission_to_delete = input("Do you wish to delete the hidden file?(Y/n): ")
        if permission_to_delete.lower() == 'y':
            cmd_delete = 'del ' + hf
            os.system(cmd_delete)
            time.sleep(1)
            print("\nThe file has been deleted successfully")
        
        else:
            print("\nThe file has not been deleted")
    
    def hide_cover_file(cf):
        '''
        This function hides the cover file from plain sight
        '''

        query_hide_cf = input("Do you wish to hide the cover file?(Y/n): ")
        if query_hide_cf.lower() == 'y':
            cmd_hide_cf = 'attrib +h ' + cf
            os.system(cmd_hide_cf)
            time.sleep(1)
            print("\nThe Cover File has been hidden successfully")
        
        else:
            print("Cover File not hidden")
    

    print("\t\t\tMAIN MENU")
    print("\n\n1. Hide Files\n2. Show hidden files\n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        cover_file = input("Enter the name of the cover file: ")
        cover_file_with_extension = cover_file + '.txt'
        
        print()

        hidden_file = input("Enter the name of the file to be hidden: ")
        hidden_file_with_extension = hidden_file + '.txt'

        print()

        print("A notepad window will appear on your screen within 5 seconds. Enter the cover message\n")
        time.sleep(5)
        cmd_cover = 'notepad ' + cover_file_with_extension
        os.system(cmd_cover)

        print("A notepad window will appear on your screen within 5 seconds. Enter the message to be hidden\n")
        time.sleep(5)
        cmd_hide = 'notepad ' + hidden_file_with_extension
        os.system(cmd_hide)

        print("Beginning to enclose file")

        enclose(cover_file_with_extension, hidden_file_with_extension)
        hide_cover_file(cover_file_with_extension)

    elif choice == 2:
        pass
    
    else:
        print("Option entered does not exist")

else:
    print("This code is specifically meant to be run only in WINDOWS systems")