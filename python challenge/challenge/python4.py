# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pdb
import requests
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
print(['working directory: ' + os.getcwd()])

#number = '12345'
#
#while(number):
#
#    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(number))
#    print(r.text)
#    number = ''.join(re.findall(r'\d+', r.text))
#
#and the next nothing is 16044
#Yes. Divide by two and keep going.
    
number = 16044/2

while(number):

    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(number))
    print(r.text)
    number = ''.join(re.findall('nothing is (\d+)', r.text))
    print(number)
    
    
