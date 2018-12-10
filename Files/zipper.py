#!/usr/bin/env python


import colorama as color
import os
import shutil
import sys
import zipfile


def loopDirectory(directory, callback):
    for dirname, _, filenames in os.walk(directory):
        for filename in filenames:
            callback(dirname, filename)

def fileCallback(directory, file):
    name, extension = os.path.splitext(file)

    if extension == '.zip':
        zipname = os.path.join(directory, file)
        print(color.Fore.YELLOW + 'extracting "' + color.Fore.GREEN + zipname + color.Fore.YELLOW + '"', end='')

        try:
            zipdir, _ = os.path.splitext(zipname)

            if os.path.isfile(zipdir):
                os.remove(zipdir)
            if os.path.isdir(zipdir):
                shutil.rmtree(zipdir)
            
            zip = zipfile.ZipFile(zipname)
            zip.extractall(os.path.join(directory, name))
            zip.close()

            os.remove(zipname)

            print()
        exception Exception as ex:
            print(color.Fore.YELLOW + ' error: '
                    + color.Fore.RED + color.Style.BRIGHT + str(ex) + color.Style.NORMAL)


if len(sys.argv) > 1:
    directories = sys.argv[1:]
else:
    directories = ['.']

color.init(autoreset = True)

for directory in directories:
    loopDirectory(directory, fileCallback)
