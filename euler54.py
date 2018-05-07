#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:11:02 2017

@author: florian
"""

import numpy as np
import pandas as pd


a = list(open("data/euler54.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [x.split(',') for x in mat]
mat = [x[0].split(' ') for x in mat]

df = pd.DataFrame(mat)

x = df.ix[0,0:4]
print(x)
