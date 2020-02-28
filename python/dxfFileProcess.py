# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:06:52 2019

@author: Illusion
"""
import json
import urllib
import math
import shapefile
import csv
from asq.initiators import query
import matplotlib.pyplot as plt
from pyproj import Transformer, transform
from collections import Counter
from dxfwrite import DXFEngine as dxf
pipePath = "D:/GASNET_Local/DOCUMENT/1128GEODATA/PIPE_N.shp" 
pipe = shapefile.Reader(pipePath,encoding='gbk')
pipeShapes = pipe.shapes()
pipeRecords = pipe.records()
pipeFields = pipe.fields
ppolylines = []
ppoints = []
for s,record in zip(pipeShapes,pipeRecords):
    if  record[41] == '中压B' or  record[41] == '中压A':
        ppolylines.append(s.points)
        for i in s.points:
            ppoints.append(i)

drawing = dxf.drawing(r'C:\Users\Illusion\Desktop\layers.dxf')
drawing.add_layer(
            'midPressB',
            color = 5,
    )
drawing.add_layer(
            'points',
            color = 2,
    )
drawing.add_layer(
            'text',
            color = 2,
    )





for i in ppolylines:
    polyline= dxf.polyline(linetype='DOT',color = 256,layer='midPressB')
    polyline.add_vertices( i )
    drawing.add(polyline)
# =============================================================================
#     drawing.save()
#     drawing.add(
#         dxf.polylines(
#             ppoints[i],
#             ppoints[i+1],
#             layer='midPressB',
#             color = 256
#         )
#     )
# =============================================================================
for i in ppoints:
    text = dxf.text('Text', i, height=3, rotation=45,layer ='text' ,color =200 )
    point = dxf.point(i)
    point['layer'] = 'points'
    point['color'] = 100
    point['thickness'] = 3.2
    drawing.add(point)
    drawing.add(text)
drawing.save()


