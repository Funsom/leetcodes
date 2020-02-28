# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:44:28 2019

@author: Illusion
"""

import json
import urllib
import math
import shapefile
import csv
import numpy as np
from asq.initiators import query
import matplotlib.pyplot as plt
from pyproj import Transformer, transform
from collections import Counter
from dxfwrite import DXFEngine as dxf


if __name__ == '__main__':
    flag = False
    
    pipePath = "D:/GASNET_Local/DOCUMENT/1128GEODATA/PIPE_N.shp" 
    elbowPath ="D:/GASNET_Local/DOCUMENT/1128GEODATA/TKBEND_N.shp"
    valvePath = "D:/GASNET_Local/DOCUMENT/1128GEODATA/VALVE_N.shp"
    teePath = "D:/GASNET_Local/DOCUMENT/1128GEODATA/TEE1_N.shp"
    pipe = shapefile.Reader(pipePath,encoding='gbk')
    elbow = shapefile.Reader(elbowPath,encoding='gbk')
    valve = shapefile.Reader(valvePath,encoding='gbk')
    tee = shapefile.Reader(teePath,encoding='gbk')
    #管线
    pipeShapes = pipe.shapes()
    pipeRecords = pipe.records()
    pipeFields = pipe.fields
    #弯头
    epoints = []
    elbowShapes = elbow.shapes()
    elbowRecords = elbow.records()
    elbowFields = elbow.fields
    #阀门
    vpoints = []
    valveShapes = valve.shapes()
    valveRecords = valve.records()
    valveFields = valve.fields
    
    #三通
    tpoints = []
    teeShapes = tee.shapes()
    teeRecords = tee.records()
    teeFields = tee.fields
    
    for s in elbowShapes:
        for i in s.points:
            
            epoints.append(tuple(i))
            
    for s in valveShapes:
        for i in s.points:
            
            vpoints.append(tuple(i))
            
    for s in teeShapes:
        for i in s.points:
            
            tpoints.append(tuple(i))
    
    ppoints = []
    for s,record in zip(pipeShapes,pipeRecords):
        #if  record[41] == '中压B' :
        #pipeType.append(record[41])
        for i in s.points: 
            ppoints.append(i)
    
    tempPipe = set(ppoints)
    tempElbow = set(epoints)
    tempValve = set(vpoints)
    tempTee = set(tpoints)
    
    unionPoints = tempPipe | tempValve | tempElbow | tempTee   
    
    #对节点进行编号
    lens = len(unionPoints) +1
    counts = list(range(1,lens))
    
    #声明节点编号查坐标与坐标查编号的字典
    nodeTable = {}
    nodeTableReverse = {}
    
    for c,r in zip(counts,unionPoints):
        
        nodeTable[r] = c 
        nodeTableReverse[c] = r
    
    #用节点编号构造管道
    pipeWithNodeID =[]
    elbowWithNodeID = []
    valveWithNodeID = []
    teeWithNodeID = []
    for s in pipeShapes:
        temp = []
        for i in s.points:
            temp.append(nodeTable[i])
        pipeWithNodeID.append(temp)
    
    for i in tpoints:
        teeWithNodeID.append(nodeTable[i])
    for i in vpoints:
        valveWithNodeID.append(nodeTable[i])    
        
    for i in epoints:
        elbowWithNodeID.append(nodeTable[i])    
        
    pipeLens = len(pipeWithNodeID)+1
    pipeID = list(range(1,pipeLens))
    pipeWithNumAndID = list(zip(pipeID,pipeWithNodeID))
    
    #构造字典，通过ID查管道上节点编号
    pipeDict = {}
    for ID,nodeID in pipeWithNumAndID:
        pipeDict[ID] = nodeID
    
    
    
    #根据管道SID属性筛选管道
    pipeInfoWithID = list(zip(pipeID,pipeRecords))
    wholePressure = pipeInfoWithID
    wholepressPipeWithNodeID = [ pipeDict[m[0]] for m in wholePressure]
    wholePressPipeInfoWithNodeID = list(zip(wholePressure,wholepressPipeWithNodeID))
    
    if flag:
        writecsv = open(r'C:\Users\Illusion\Desktop\wholePressPipeInfoWithNodeID.csv','w',newline = '')
        for ID in wholePressPipeInfoWithNodeID:
            writecsv.write(str(ID))
            writecsv.write("\n")
        writecsv.close()
    
    
    #根据中压管网中的节点ID，匹配节点类型与信息,先整出节点表 节点表必须拆分
    
    wholePressNodeList = counts
    #建立全局的特殊节点类型字典
    valveInfoWithID = list(zip(valveWithNodeID,valveRecords))
    teeInfoWithID = list(zip(teeWithNodeID,teeRecords))
    elbowInfoWithID = list(zip(elbowWithNodeID,elbowRecords))
    nodeTypeInfoDict ={}
    
    #初始化节点字典
    for c in counts:
        nodeTypeInfoDict[c] = ''
    for e in elbowInfoWithID:
        nodeTypeInfoDict[e[0]] = (e[1],"弯头")
    for t in teeInfoWithID:
        nodeTypeInfoDict[t[0]] = (t[1],"三通")
    for v in valveInfoWithID:
        nodeTypeInfoDict[v[0]] = (v[1],"阀门")
    # 节点编号   节点信息   节点地址 
    wholePressNodeTable = [(m,nodeTypeInfoDict[m],nodeTableReverse[m])  for m in wholePressNodeList]
    #记录 节点表基本完毕
    if flag:
        writecsv1 = open(r'C:\Users\Illusion\Desktop\midPressCommonNodeTable.csv','w',newline = '')
        for ID in wholePressNodeTable:
            if ID[1] == '':
                writecsv1.write(str(ID))
                writecsv1.write("\n")
    # =============================================================================
    #         if ID[1] != '':
    #              
    #             if ID[1][1] == '弯头':
    #                 writecsv1.write(str(ID[0]))
    #                 writecsv1.write(',')
    #                 for e in ID[1][0]:
    #                     writecsv1.write(str(e))
    #                     writecsv1.write(',')
    #                 writecsv1.write(str(ID[2]))
    #                 writecsv1.write("\n")
    # =============================================================================
        writecsv1.close()
    
    # 处理管道表的问题
    # 思路就是将多节点管道拆分成多段管道，编号是个问题，管道编号先保持不变
    rebulitWholePressPipeWithMoreNode = []
    wholePressPipeWithMoreNode = [p for p in wholePressPipeInfoWithNodeID if len(p[1])>2 ]
    wholePressPipeWithTwoNode = [p for p in wholePressPipeInfoWithNodeID if len(p[1])==2 ]
    for p in wholePressPipeWithMoreNode:
        start = p[1][0]
        index = 0
        for n in p[1]:
            if n == start:
                continue
            else:
                ID = str(p[0][0])+'-'+str(index)
                index += 1
                element = (ID,p[0][1],[start,n])
                rebulitWholePressPipeWithMoreNode.append(element)
                start = n
    rebulitmidPressPipeTable = wholePressPipeWithTwoNode + rebulitWholePressPipeWithMoreNode
    
    #记录
    if flag:
        writecsv2 = open(r'C:\Users\Illusion\Desktop\rebulitmidPressPipeTable.csv','w',newline = '')
        for ID in wholePressPipeWithTwoNode:
            writecsv2.write(str(ID[0][0]))
            writecsv2.write(',')
            for e in ID[0][1]:
                writecsv2.write(str(e))
                writecsv2.write(',')
            writecsv2.write(str(ID[1]))
            writecsv2.write("\n")
        for ID in rebulitWholePressPipeWithMoreNode:
            writecsv2.write(str(ID[0]))
            writecsv2.write(',')
            for e in ID[1]:
                writecsv2.write(str(e))
                writecsv2.write(',')
            writecsv2.write(str(ID[2]))
            writecsv2.write("\n")
        
        writecsv2.close()
        
        
        writecsv3 = open(r'C:\Users\Illusion\Desktop\fields.csv','w',newline = '')
        
        
        writecsv3.write(str(pipeFields))
        writecsv3.write("\n")
        writecsv3.write(str(elbowFields))
        writecsv3.write("\n")
        writecsv3.write(str(valveFields))
        writecsv3.write("\n")
        writecsv3.write(str(teeFields))
           
        writecsv3.write("\n")
        writecsv3.close()
    
    
    
    #测试中压管网是否连通
    # 测试结果，不完全连通，连通分量为187，最大连通图元素数为32017
    
    import networkx as nx
    G=nx.Graph()#创建空的简单图
    #G.add_node(1)#加1这个点
    #G.add_edge(1,2)
    #G.add_nodes_from(count)#加列表中的点
    edgesInMidPressPipe0 = [tuple([p[1][0],p[1][1],{'ID':p[0][0]}]) for p in wholePressPipeWithTwoNode]
    edgesInMidPressPipe1 = [tuple([p[2][0],p[2][1],{'ID':p[0]}]) for p in rebulitWholePressPipeWithMoreNode]
    edgesInMidPressPipe = edgesInMidPressPipe0 + edgesInMidPressPipe1
    G.add_nodes_from(counts)
    G.add_edges_from(edgesInMidPressPipe)
    

    #len(list(nx.connected_components(G)))
    result = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    subNetwork = [c for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    
    subG = [c for c in sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)]
    
    
    
    drawing = dxf.drawing(r'C:\Users\Illusion\Desktop\WholeNetworklayers.dxf')
    
    
    drawing.add_layer(
                'points',
                color = 2,
        )
    drawing.add_layer(
                'pipeLabel',
                color = 2,
        )
   
    indicator = 0
    for sub in subG:
        drawing.add_layer(
                'subG%s'% indicator,
                color = indicator % 255,
        )
    
        for s in sub.edges(data = True):
            startPoint = nodeTableReverse[s[0]]
            
            endPoint = nodeTableReverse[s[1]]
            xdiff = startPoint[0] - endPoint[0]
            ydiff = startPoint[1] - endPoint[1]
            angle = 0
            if np.abs(xdiff)> 1e-5:
                angle = np.arctan(ydiff/xdiff)*180/np.pi
            
            middlePoint = [( startPoint[0] + endPoint[0] ) /2.,( startPoint[1] + endPoint[1] ) /2.]
            line = dxf.line(startPoint, endPoint,layer ='subG%s'% indicator )
            text = dxf.text('pipe%s'%  str(s[2]['ID']), middlePoint, height=0.2, rotation=angle,layer ='pipeLabel'  )
            text['color'] = 0
            
            drawing.add(line)
            drawing.add(text)
        
    
        for i in sub.nodes:
            text = dxf.text(i, nodeTableReverse[i], height=0.05, rotation=0,layer ='subG%s'% indicator  )
            point = dxf.point(nodeTableReverse[i], layer ='points'  )
            point['color'] = 250
            drawing.add(text)
            drawing.add(point)
        indicator += 1
    drawing.save()
