import os
import logger
import win32api
import tkinter as tk
import merge_open

# Declared dictionary to get the various types of files
files_found = dict()


def is_folder(file):
    """
    Function returns whether the given file argument is folder or not.
    Input :
    file(string) - Name of the file
    Output :
    Boolean - Whether the file is folder or not.
    """
    return file.rfind('.') < 0


def search(file_name, drive_name, files_found):
    """
    Function searches the file recursively in all the directories and returns the found in dictionary format
    Input :
    file_name(string) - Name of file to be searched
    drive_name(string) - Name of the drive currently being searched
    files_found(dictionary) - Dictionary of files found

    Output :
    Dictionary - Dictionary of files found
    """
    print(file_name)
    for sub_dir, dirs, files in os.walk(drive_name):
        for file in files:
            if file.split('.')[0] == file_name and (file.endswith('.docx') or file.endswith('.txt') or file.endswith('.pdf')):
                print(file, sub_dir)
                extension = file.split('.')[1]
                if extension in files_found:
                    files_found[extension].append([file, sub_dir])
                else:
                    files_found[extension] = [[file, sub_dir]]
    
    return files_found    

def start_search(file_to_search, window):
    """
    Function responsible for calling search function. 
    Input : 
    file_to_search(Object) - Tkinter Entry Object
    window(Object) - Tkinter Root Object
    """
    
    files_found = {}
    file_name = file_to_search.get()

    # To check whether file name is valid
    if file_name == '' and file_name.rfind('.') > 0:
        tk.messagebox.showinfo(
            'Error', 'Please enter the valid file name')
        return

    # Finding the drives_list
    drives = win32api.GetLogicalDriveStrings()
    drives_name = drives.split('\000')[:-1]
    
    # Iterate over all the drives one by one
    for drive_name in drives_name:
        try:
            os.chdir(drive_name)
            files_found = search(file_name, drive_name, files_found)
        except Exception as e:
            logger.log.exception(e)

    if files_found.items():
        for key, value in files_found.items():
            print(key, value)

        return_val = merge_open.show_files(files_found, window)
        # Calling the merge_func for merging of the different files
        merge_open.merge_func(
            return_val[0], return_val[1], files_found, file_to_search)
    else:
        tk.messagebox.showinfo('Result not found',
                               'The entered file is not present in directories')


def makeEntryEmpty(file_to_search):
    """
    Function is responsible for adding event handler on entry object.
    Input : 
    file_to_search(Object) - Tkinter Entry Object
    """
    file_to_search.delete(0, 'end')
