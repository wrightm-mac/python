#!/usr/bin/env python

##################################################################################
#                                                                                #
# BSD 3-Clause License                                                           #
#                                                                                #
# Copyright (c) 2018, wrightm-mac                                                #
# All rights reserved.                                                           #
#                                                                                #
# Redistribution and use in source and binary forms, with or without             #
# modification, are permitted provided that the following conditions are met:    #
#                                                                                #
# * Redistributions of source code must retain the above copyright notice, this  #
#   list of conditions and the following disclaimer.                             #
#                                                                                #
# * Redistributions in binary form must reproduce the above copyright notice,    #
#   this list of conditions and the following disclaimer in the documentation    #
#   and/or other materials provided with the distribution.                       #
#                                                                                #
# * Neither the name of the copyright holder nor the names of its                #
#   contributors may be used to endorse or promote products derived from         #
#   this software without specific prior written permission.                     #
#                                                                                #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"    #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE      #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE   #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL     #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR     #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER     #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,  #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.           #
#                                                                                #
##################################################################################


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

        except Exception as ex:
            print(color.Fore.YELLOW + ' error: '
                    + color.Fore.RED + color.Style.BRIGHT + str(ex) + color.Style.NORMAL)


if len(sys.argv) > 1:
    directories = sys.argv[1:]
else:
    directories = ['.']

color.init(autoreset = True)

for directory in directories:
    loopDirectory(directory, fileCallback)
