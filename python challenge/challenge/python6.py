# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pdb
import requests
import re
#import pickle
import io
import zipfile
import pandas

dir_path = os.path.dirname(os.path.realpath(__file__))
print(['working directory: ' + os.getcwd()])

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("python6")

number = "90052"
comments = []

while(number):
    file = open("python6/"+number+".txt", "r") 
    comments.append(z.getinfo(number + '.txt').comment)

    my_text = file.read()
    print(my_text) 
    number = ''.join(re.findall('nothing is (\d+)', my_text))
    print(number)
    file.close()
#    
#all_files = os.listdir("python6")
#all_files = [re.sub('.txt','',x) for x in all_files]
#
#[x for x in all_files if x not in all_numbers]

#for i in all_files:
#    file = open("python6/"+str(i), "r") 
#    my_text = file.read()
#    print(my_text) 
#    file.close

