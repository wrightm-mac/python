#!/usr/bin/env python3.7

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


import httplib2


gifts = [ 
    ('first', 'a partidge in a pear tree'),
    ('second', 'two turtle doves'),
    ('third', 'three french hens'),
    ('fourth', 'four calling birds'),
    ('fifth', 'five gold rings'),
    ('sixth', 'six geese a laying'),
    ('seventh', 'seven swans a swimming'),
    ('eighth', 'eight maids a milking'),
    ('ninth', 'nine ladies dancing'),
    ('tenth', 'ten lords a leaping'),
    ('eleventh', 'eleven pipers piping'),
    ('twelfth', 'twelve drummers drumming')
]


def doGet(url, useragent):
    headers = {'User-Agent': useragent}
    _, content = httplib2.Http().request(url, 'GET', headers=headers)
    return content

def writeLine(line):
    doGet('http://localhost:2108', line)
    print(line)


for verseindex in range(0, len(gifts)):
    number, gift = gifts[verseindex]
    writeLine('on the ' + number + ' day of christmas, my true love gave to me ' + gift)

    if verseindex > 0:
        for previndex in range(verseindex - 1, -1, -1):
            if previndex == 0:
                prevline = 'and '
            else:
                prevline = ''
            _, prevgift = gifts[previndex]
            prevline += prevgift
            writeLine(prevline)
