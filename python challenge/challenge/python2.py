# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pdb

dir_path = os.path.dirname(os.path.realpath(__file__))
print(['working directory: ' + os.getcwd()])

file = open("text2.txt", "r") 
my_text = file.read()



strs = 'abcdefghijklmnopqrstuvwxyz'

def keeptext(inp):
    data =[]
    for i in inp:
        if i in strs:
            data.append(i)
            
    output = ''.join(data)
    return output
        
print(keeptext(my_text))