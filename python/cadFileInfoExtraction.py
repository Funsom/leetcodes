# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:11:38 2019

@author: Illusion
"""
 #coding: utf-8

import ezdxf  
import re
import os
import csv
import numpy as np
import shapefile
from collections import Counter
import matplotlib.pyplot as plt 
#from dpfpy import dbfread


doc = ezdxf.readfile(r"C:\Users\Illusion\Desktop\徐州市中压A管道2019水力计算基础图dwg (1).dxf")
# iterate over all entities in modelspace
msp = doc.modelspace()
layer = [i for i in msp if i.dxf.layer == '地名' and i.dxftype() == 'MTEXT']
node = [i for i in layer if re.match(r'^A\d+$',i.text) ]
loc = [ i.dxf.insert for i in node]
text = [i.text for i in node]
union = [i for i in zip(text,loc)]
writecsv3 = open(r'C:\Users\Illusion\Desktop\PA.csv','w',newline = '')

for i in union:
    writecsv3.write(str(i))    
        

    writecsv3.write("\n")

writecsv3.close()