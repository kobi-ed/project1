# Implementation of the pwd command with Python
# Date June 5, 2021
# Author : kobi-ed

#!/usr/bin/env python3
import os

def getCurrentDirectory():
    '''Return the current directory'''
    return os.getcwd()

def showCurrentDirectory():
    '''Print out the current working
    directory'''
    workingDirectory = getCurrentDirectory()
    print(workingDirectory)

if __name__ == "__main__":
    showCurrentDirectory()
