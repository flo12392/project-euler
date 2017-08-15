# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pdb

dir_path = os.path.dirname(os.path.realpath(__file__))
print(['working directory: ' + os.getcwd()])

file = open("text3.txt", "r") 
my_text = file.read()

data = []

for i in range(3,len(my_text)-4):
    if( my_text[(i-3):(i+4)].isalpha() and my_text[i].islower() and my_text[(i-3):i].isupper() and my_text[(i+1):(i+4)].isupper()):
            if(i != 3 and i != len(my_text)-4):
                if(my_text[(i-4)].islower() and my_text[(i+4)].islower()):
                    data.append(my_text[i])
                    print(my_text[(i-4):(i+5)])
            else:
                data.append(my_text[i])

print(''.join(data))
