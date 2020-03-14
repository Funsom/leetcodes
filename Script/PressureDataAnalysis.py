# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:01:41 2020

@author: Illusion
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def divide(filename):
    excel = pd.read_excel(filename,header=[0,1],index_col=0)
    print(type(excel))
    





if __name__ == "__main__":
    filename = r"D:\Users\Illusion\Desktop\20-02-1-15.xlsx"
    file = open('D:\\test.txt','w')
    oldstdout = sys.stdout
    sys.stdout = file
    print(help(pd.DataFrame))
    file.close()
    sys.stdout = oldstdout
    divide(filename)