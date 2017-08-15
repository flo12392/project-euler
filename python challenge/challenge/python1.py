# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(['working directory: ' + os.getcwd()])

file = open("text.txt", "r") 
my_text = file.read()
print(my_text) 


strs = 'abcdefghijklmnopqrstuvwxyz'

def shifttext(inp,shift):
    data=[]
    for i in inp:                     #iterate over the text not some list
        if i.strip() and i in strs:                 # if the char is not a space ""  
            data.append(strs[(strs.index(i) + shift) % 26])    
        else:
            data.append(i)           #if space the simply append it to data
    output = ''.join(data)
    return output

result = shifttext(my_text,2)

print(result)