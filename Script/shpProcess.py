# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:39:47 2019

@author: Illusion
"""

import os
import csv
import numpy as np
import shapefile
import collections
import matplotlib.pyplot as plt
import networkx as nx
import copy
from pyproj import Transformer, transform
from geopy.distance import geodesic
from coordTransform_utils import wgs84_to_bd09
#from dpfpy import dbfread

def getUniqPoint(shapes,points):
    for s in shapes:
        for i in s.points:
            points.append(tuple(i))
    return set(points)

def distanceBetweenNodes(dic,i,j):
        x,y = dic[i]
        x1,y1 = dic[j]
        return np.sqrt((x-x1)**2. + (y-y1)**2.)

    
def saveFile(filename,data):
    file = open(filename,"w")
    for d in data:
        file.write(str(d))
        file.write('\n')
    file.close()
    
    
#distanceBetweenNodesInDiffSubGs = {}
def findMinDistInDiffSubGs(dic,G):
    pointer = 1
    subNetwork = [c for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    minDistanceBetweenNodeInDiffSubGs = {}
    for s in subNetwork[1:]:
        connectedComponents = copy.deepcopy(subNetwork)
        connectedComponents.remove(s)
        #print(len(s))
        temp = []
        for e in s:
            minx = 1000000
            currentIndex = 0
            #print(pointer)
            for c in connectedComponents:
                for el in c:
                    dis = distanceBetweenNodes(dic,e,el)
                    if dis < minx :
                        minx = dis
                        currentIndex = el
                    
            temp.append((e,currentIndex,minx))
        idt = (0,0)
        mint = 100000
        for t in temp:
            if mint > t[2]:
                mint = t[2]
                idt = (t[0],t[1])
        minDistanceBetweenNodeInDiffSubGs[pointer] = (idt[0],idt[1])#,mint
        pointer += 1
    return  minDistanceBetweenNodeInDiffSubGs


if __name__ == "__main__":
    
    tempPath = r"D:\GWFZ\DOCUMENT\JinTanGIS\PIPESECTIONHP.shp"
    temp = shapefile.Reader(tempPath,encoding='gbk')
    tempShapes = temp.shapes()
    tempRecords = temp.records()
    tempFields =  temp.fields
    uniqPoints = getUniqPoint(tempShapes,[])
    pointDicts = {ele:ind+1 for ind,ele in enumerate(uniqPoints)}
    reversePointDicts = {ind+1:ele for ind,ele in enumerate(uniqPoints)}
    
    multiPipes = []
    simplePipes = []
    simplePipeInfo = []
    multiPipeInfo = []
    for s,info in zip(tempShapes,tempRecords):
        temps = []
        for i in s.points:
            temps.append(pointDicts[i])
        if len(temps) == 2:
            simplePipes.append(tuple(temps))
            simplePipeInfo.append(info[16])
        else:
            multiPipes.append(tuple(temps))
            multiPipeInfo.append(info[16])
            
    for p,info in zip(multiPipes,multiPipeInfo):
        n = len(p)
        for i in range(n-1):
            simplePipes.append((p[i],p[i+1]))
            simplePipeInfo.append(info)

    G=nx.Graph()#创建空的简单图
    G.add_nodes_from(list(pointDicts.values()))
    G.add_edges_from(simplePipes)
    
    result = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    
    
    subG = [G.subgraph(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
# =============================================================================
#     G.remove_edges_from(subG[-1].edges)
#     G.remove_edges_from(subG[-2].edges)
#     G.remove_nodes_from(subG[-1].nodes)
#     G.remove_nodes_from(subG[-2].nodes)
#     nu = nx.number_connected_components(G)
# =============================================================================
    
    fixedLine = []
    while nx.number_connected_components(G) > 1:
    
        minDistanceBetweenNodeInDiffSubGs = findMinDistInDiffSubGs(reversePointDicts,G)
        fixed = minDistanceBetweenNodeInDiffSubGs.values()
        G.add_edges_from(fixed)
        fixedLine.extend(fixed)
    
    
    
    
    for i in fixedLine:

        simplePipes.append(i)
        simplePipeInfo.append(219)
    
    # 文件处理
    data = []
    for k,v in pointDicts.items():
        x,y = k
        lat,lng = transform(2437, 4326, y,x)
        lng,lat = wgs84_to_bd09(float(lng), float(lat))
        data.append((v,lng,lat))
    pointsSavePath = r"D:\Users\Illusion\Desktop\points_.csv"
    saveFile(pointsSavePath,data)
    
    pipeSavePath = r"D:\Users\Illusion\Desktop\pipes_.csv"
    
    
    pipeInfo = []
    for p,info in zip(simplePipes,simplePipeInfo):
        s,e = p
        sx,sy = reversePointDicts[s]
        slat,slng = transform(2437, 4326, sy,sx)
        ex,ey = reversePointDicts[e]
        elat,elng = transform(2437, 4326, ey,ex)
        lens = geodesic((slat,slng), (elat,elng)).m
        pipeInfo.append((s,e,lens,info))
        #plt.plot([sx,ex],[sy,ey])
    
    
    saveFile(pipeSavePath,pipeInfo)
    
    
    
    minDist = float('inf')
    minDist1 = float('inf')
    target = (119.436071,31.831451)
    target1 = (119.437183,31.831137)
    res = None
    res1 = None
    for i,x,y in data:
        dist = (x - target[0])**2 + (y-target[1])**2
        dist1 = (x - target1[0])**2 + (y -target1[1])**2
        
        if dist < minDist:
            minDist = dist
            res = i
        if dist1 < minDist1:
            minDist1 = dist1
            res1 = i
    ind = res
    ind1 = res1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            