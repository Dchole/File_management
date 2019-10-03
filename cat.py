import os
import time
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import file_extensions


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            new_name = filename
            extension = 'noname'
            try:
                extension = str(os.path.splitext(
                    folder_to_track + '/' + filename)[1])
                path = file_extensions.extensions[extension]
            # else:
                print(path)
            except Exception:
                extension = 'noname'


folder_to_track = '/Users/KOMFUEKU METH. PRY/Projects/demos/cat-test'

handler = MyHandler()
observer = Observer()

observer.schedule(handler, folder_to_track, recursive=True)
observer.start()
