# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pdb
import requests
import re
import pickle

dir_path = os.path.dirname(os.path.realpath(__file__))
print(['working directory: ' + os.getcwd()])


 
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
r = requests.get(url)
text = str.encode(r.text)
x=pickle.loads(text)

for line in x:
    toprint=[]
    for v in line:
        toprint.append(v[0]*v[1])
    print(''.join(toprint))
 
    
for line in x:
    print("".join([k * v for k, v in line]))

    
    
