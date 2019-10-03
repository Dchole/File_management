import os
import time


target_directory = '/mnt/c/Users/KOMFUEKU METH. PRY/Projects/demos/cat-test'


def categorize(target_directory):
    for file in os.listdir(target_directory):
        print(file)


categorize(target_directory)
