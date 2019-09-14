import os
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

groups = ['Programs', 'Documents', 'Images',
          'Videos', 'Compressed', 'Files', 'Audio']

folder_to_track = '/mnt/c/Users/KOMFUEKU METH. PRY/Downloads'


def categorize(directory):
    # Create a group
    for group in groups:
        try:
            os.mkdir(directory + "/" + group)
        except FileExistsError:
            print(f'{group} already exist')

    # Categorizing
    for file in os.listdir(directory):
        # Checking for filetype
        try:
            filename, separator, extension = file.partition('.')
        except IsADirectoryError:
            print(f'Failed to move {file}')
        else:
            print(extension)

        if file in groups:
            pass
        else:
            part = file.partition('.')
            if part[2] == 'txt':
                os.rename(directory+'/'+file, directory+'/Documents/'+file)
                print(file)
            if part[2] == 'mp3':
                os.rename(directory+'/'+file, directory+'/Audio/'+file)
                print(file)
            if part[2] == 'jpg':
                os.rename(directory+'/'+file, directory+'/Images/'+file)
                print(file)
            if part[2] == 'mp4':
                os.rename(directory+'/'+file, directory+'/Videos/'+file)
                print(file)
            else:
                print(file)


categorize(folder_to_track)
