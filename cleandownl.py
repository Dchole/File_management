import os
import time
import file_extensions

target_directory = '/mnt/c/Users/KOMFUEKU METH. PRY/Downloads'

files = [file for file in os.listdir(
    target_directory) if os.path.isfile(os.path.join(target_directory, file))]

for f in files:
    extension = os.path.splitext(f)[1]

    try:
        extension = file_extensions.extensions[extension]
    except KeyError:
        pass

    if os.path.exists(target_directory + "/" + extension):
        print(extension, "Folder exists")
        pass
    else:
        os.mkdir(target_directory + "/" + extension)
        print(extension, "Folder created")

    os.rename(target_directory + "/" + f,
              target_directory + "/" + extension + "/" + f)
