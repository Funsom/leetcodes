# -*- coding: utf-8 -*-
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

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方


class Geocoding:
    def __init__(self, api_key):
        self.api_key = api_key

    def geocode(self, address):
        """
        利用高德geocoding服务解析地址获取位置坐标
        :param address:需要解析的地址
        :return:
        """
        geocoding = {'s': 'rsv3',
                     'key': self.api_key,
                     'city': '全国',
                     'address': address}
        geocoding = urllib.urlencode(geocoding)
        ret = urllib.urlopen("%s?%s" % ("http://restapi.amap.com/v3/geocode/geo", geocoding))

        if ret.getcode() == 200:
            res = ret.read()
            json_obj = json.loads(res)
            if json_obj['status'] == '1' and int(json_obj['count']) >= 1:
                geocodes = json_obj['geocodes'][0]
                lng = float(geocodes.get('location').split(',')[0])
                lat = float(geocodes.get('location').split(',')[1])
                return [lng, lat]
            else:
                return None
        else:
            return None


def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]


def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)


def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


def findSubGByNodeID(subG,nodeID):
    index = 0
    for s in subG:
        if nodeID in s.nodes :
            return index
        index += 1
        
    return -1

if __name__ == '__main__':
    flag = False
    
    #新增四通、中低压、中中压、高中压调压站、变径\管末
    pipePath = "C:/Users/Illusion/Desktop/pipeWithLatLng.shp" 
    elbowPath ="C:/Users/Illusion/Desktop/XZTransShp/TKBEND_N.shp"
    valvePath = "C:/Users/Illusion/Desktop/VALVE_N.shp"
    teePath = "C:/Users/Illusion/Desktop/XZTransShp/TEE1_N.shp"
    crossPath = "C:/Users/Illusion/Desktop/XZTransShp/CROSS_N.shp"
    lowGovernorPath = "C:/Users/Illusion/Desktop/XZTransShp/GOVERNOR_N.shp"
    midGovernorPath = "C:/Users/Illusion/Desktop/XZTransShp/ZGOVERNOR_N.shp"
    higGovernorPath = "C:/Users/Illusion/Desktop/XZTransShp/OFFTAKE_N.shp"
    terminalPath = "C:/Users/Illusion/Desktop/XZTransShp/TERMINTR_N.shp"
    
    pipe = shapefile.Reader(pipePath,encoding='utf8')
    elbow = shapefile.Reader(elbowPath,encoding='utf8')
    valve = shapefile.Reader(valvePath,encoding='utf8')
    tee = shapefile.Reader(teePath,encoding='utf8')
    cross = shapefile.Reader(crossPath,encoding='utf8')
    lowGovernor = shapefile.Reader(lowGovernorPath,encoding='utf8')
    midGovernor = shapefile.Reader(midGovernorPath,encoding='utf8')
    higGovernor = shapefile.Reader(higGovernorPath,encoding='utf8')
    terminal = shapefile.Reader(terminalPath,encoding='utf8')
    
    #管线
    ppoints = []; pipeShapes = pipe.shapes()
    pipeRecords = pipe.records(); pipeFields = pipe.fields
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
    
    #四通
    cpoints = []
    crossShapes = cross.shapes()
    crossRecords = cross.records()
    crossFields = cross.fields
    
    #中低压调压站
    lpoints = []
    lowGovernorShapes = lowGovernor.shapes()
    lowGovernorRecords = lowGovernor.records()
    lowGovernorFields = lowGovernor.fields
    #中中压调压站
    mpoints = []
    midGovernorShapes = midGovernor.shapes()
    midGovernorRecords = midGovernor.records()
    midGovernorFields = midGovernor.fields
    #高中压调压站
    hpoints = []
    higGovernorShapes = higGovernor.shapes()
    higGovernorRecords = higGovernor.records()
    higGovernorFields = higGovernor.fields
    
    tepoints = []
    terminalShapes = terminal.shapes()
    terminalRecords = terminal.records()
    terminalFields = terminal.fields
    
    def getUniqPoint(shapes,points):
        for s in shapes:
            for i in s.points:
                points.append(tuple(i))
        return set(points)

         
    
    
    tempPipe = getUniqPoint(pipeShapes,ppoints)
    tempElbow = getUniqPoint(elbowShapes,epoints)     
    tempValve = getUniqPoint(valveShapes,vpoints)
    tempTee = getUniqPoint(teeShapes,tpoints)
    tempCross = getUniqPoint(crossShapes,cpoints)
    tempLowGovernor = getUniqPoint(lowGovernorShapes,lpoints)
    tempMidGovernor = getUniqPoint(midGovernorShapes,mpoints)
    tempHigGovernor = getUniqPoint(higGovernorShapes,hpoints)
    tempTeiminal = getUniqPoint(terminalShapes,tepoints)
    
    unionPoints = tempPipe | tempValve | tempElbow | tempTee | tempCross | tempLowGovernor | tempMidGovernor | tempHigGovernor | tempTeiminal
    #比单纯的管道上的点多了三个
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
     
    
    for s in pipeShapes:
        temp = [nodeTable[i] for i in s.points]       
        pipeWithNodeID.append(temp)
    
    def elementCoupleWithNodeID(points): 
        return [nodeTable[i] for i in points]
    
    elbowWithNodeID = elementCoupleWithNodeID(epoints)
    valveWithNodeID = elementCoupleWithNodeID(vpoints)
    teeWithNodeID = elementCoupleWithNodeID(tpoints)
    crossWithNodeID = elementCoupleWithNodeID(cpoints)
    lowGovernorWithNodeID = elementCoupleWithNodeID(lpoints)
    midGovernorWithNodeID = elementCoupleWithNodeID(mpoints)
    higGovernorWithNodeID = elementCoupleWithNodeID(hpoints)
    terminalWithNodeID = elementCoupleWithNodeID(tepoints)
    
    
    
    pipeLens = len(pipeWithNodeID)+1
    pipeID = list(range(1,pipeLens))
    pipeWithNumAndID = list(zip(pipeID,pipeWithNodeID))
    
    #构造字典，通过ID查管道上节点编号
    pipeDict = {}
    for ID,nodeID in pipeWithNumAndID:
        pipeDict[ID] = nodeID
    
    
    
    #根据管道SID属性筛选管道
    pipeInfoWithID = list(zip(pipeID,pipeRecords))
    # 全部中压A/B
    #middlePressure = [p for p in pipeInfoWithID if p[1][41] == "中压A" or p[1][41] == "中压B"]
    # 中压A
    #middlePressure = [p for p in pipeInfoWithID if p[1][41] == "中压A" ]
    # 中压B
    middlePressure = [p for p in pipeInfoWithID if p[1][41] == "中压B" ]
    
    midpressPipeWithNodeID = [ pipeDict[m[0]] for m in middlePressure]
    
    midPressPipeInfoWithNodeID = list(zip(middlePressure,midpressPipeWithNodeID))
    
    if flag:
        writecsv = open(r'C:\Users\Illusion\Desktop\midPressPipeInfoWithNodeID.csv','w',newline = '')
        for ID in midPressPipeInfoWithNodeID:
            writecsv.write(str(ID))
            writecsv.write("\n")
        writecsv.close()
    
    
    #根据中压管网中的节点ID，匹配节点类型与信息,先整出节点表 节点表必须拆分
    midPressNodeList_ = [ n for m in midpressPipeWithNodeID   for n in m  ]
    midPressNodeList = list(set(midPressNodeList_))
    #建立全局的特殊节点类型字典
    valveInfoWithID = list(zip(valveWithNodeID,valveRecords))
    teeInfoWithID = list(zip(teeWithNodeID,teeRecords))
    elbowInfoWithID = list(zip(elbowWithNodeID,elbowRecords))
    crossInfoWithID = list(zip(crossWithNodeID,crossRecords))
    lowGovernorInfoWithID = list(zip(lowGovernorWithNodeID,lowGovernorRecords))
    midGovernorInfoWithID = list(zip(midGovernorWithNodeID,midGovernorRecords))
    higGovernorInfoWithID = list(zip(higGovernorWithNodeID,higGovernorRecords))
    terminalInfoWithID = list(zip(terminalWithNodeID,terminalRecords))
    
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
    for c in crossInfoWithID:
        nodeTypeInfoDict[c[0]] = (c[1],"四通")
    for l in lowGovernorInfoWithID:
        nodeTypeInfoDict[l[0]] = (l[1],"中低压调压站")
    for m in midGovernorInfoWithID:
        nodeTypeInfoDict[m[0]] = (m[1],"中中压调压站")
    for h in higGovernorInfoWithID:
        nodeTypeInfoDict[h[0]] = (h[1],"高中压调压站")
    for t in terminalInfoWithID:
        nodeTypeInfoDict[t[0]] = (t[1],"管末")
    # 节点编号   节点信息   节点地址 
    midPressNodeTable = [(m,nodeTypeInfoDict[m],nodeTableReverse[m])  for m in midPressNodeList]
    #记录 节点表基本完毕
    if flag:
        writecsvCommonNode = open(r'C:\Users\Illusion\Desktop\midPressCommonNodeTable.csv','w',newline = '')
        writecsvElbow = open(r'C:\Users\Illusion\Desktop\midPressElbowTable.csv','w',newline = '')
        writecsvValve = open(r'C:\Users\Illusion\Desktop\midPressValveTable.csv','w',newline = '')
        writecsvTee = open(r'C:\Users\Illusion\Desktop\midPressTeeTable.csv','w',newline = '')
        writecsvCross = open(r'C:\Users\Illusion\Desktop\midPressCrossTable.csv','w',newline = '')
        writecsvLowGovernor = open(r'C:\Users\Illusion\Desktop\midPressLowGovernorTable.csv','w',newline = '')
        writecsvMidGovernor = open(r'C:\Users\Illusion\Desktop\midPressMidGovernorTable.csv','w',newline = '')
        writecsvHigGovernor = open(r'C:\Users\Illusion\Desktop\midPressHigGovernorTable.csv','w',newline = '')
        writecsvTerminal = open(r'C:\Users\Illusion\Desktop\midPressTerminalTable.csv','w',newline = '')
        for ID in midPressNodeTable:
            if ID[1] == '':
                writecsvCommonNode.write(str(ID))
                writecsvCommonNode.write("\n")
            elif ID[1][1] == '弯头':
                writecsvElbow.write(str(ID[0]))
                writecsvElbow.write(',')
            
                for e in ID[1][0]:
                    writecsvElbow.write(str(e))
                    writecsvElbow.write(',')
                writecsvElbow.write(str(ID[2]))
                writecsvElbow.write("\n")
            elif ID[1][1] == '阀门':
                
                writecsvValve.write(str(ID[0]))
                writecsvValve.write(',')
            
                for e in ID[1][0]:
                    writecsvValve.write(str(e))
                    writecsvValve.write(',')
                writecsvValve.write(str(ID[2]))
                writecsvValve.write("\n")
            elif ID[1][1] == '三通':
                
                writecsvTee.write(str(ID[0]))
                writecsvTee.write(',')
            
                for e in ID[1][0]:
                    writecsvTee.write(str(e))
                    writecsvTee.write(',')
                writecsvTee.write(str(ID[2]))
                writecsvTee.write("\n")
            elif ID[1][1] == '四通':
                
                writecsvCross.write(str(ID[0]))
                writecsvCross.write(',')
            
                for e in ID[1][0]:
                    writecsvCross.write(str(e))
                    writecsvCross.write(',')
                writecsvCross.write(str(ID[2]))
                writecsvCross.write("\n")
            elif ID[1][1] == '中低压调压站':
                
                writecsvLowGovernor.write(str(ID[0]))
                writecsvLowGovernor.write(',')
            
                for e in ID[1][0]:
                    writecsvLowGovernor.write(str(e))
                    writecsvLowGovernor.write(',')
                writecsvLowGovernor.write(str(ID[2]))
                writecsvLowGovernor.write("\n")
            elif ID[1][1] == '中中压调压站':
                
                writecsvMidGovernor.write(str(ID[0]))
                writecsvMidGovernor.write(',')
            
                for e in ID[1][0]:
                    writecsvMidGovernor.write(str(e))
                    writecsvMidGovernor.write(',')
                writecsvMidGovernor.write(str(ID[2]))
                writecsvMidGovernor.write("\n")
            elif ID[1][1] == '高中压调压站':
               
                writecsvHigGovernor.write(str(ID[0]))
                writecsvHigGovernor.write(',')
            
                for e in ID[1][0]:
                    writecsvHigGovernor.write(str(e))
                    writecsvHigGovernor.write(',')
                writecsvHigGovernor.write(str(ID[2]))
                writecsvHigGovernor.write("\n")
            elif ID[1][1] == '管末':
                
                writecsvTerminal.write(str(ID[0]))
                writecsvTerminal.write(',')
            
                for e in ID[1][0]:
                    writecsvTerminal.write(str(e))
                    writecsvTerminal.write(',')
                writecsvTerminal.write(str(ID[2]))
                writecsvTerminal.write("\n")
  
        writecsvCommonNode.close()
        writecsvElbow.close()
        writecsvValve.close()
        writecsvTee.close()
        writecsvCross.close()
        writecsvLowGovernor.close()
        writecsvMidGovernor.close()
        writecsvHigGovernor.close()
        writecsvTerminal.close()
    
    # 处理管道表的问题
    # 思路就是将多节点管道拆分成多段管道，编号是个问题，管道编号先保持不变
    rebulitmidPressPipeWithMoreNode = []
    midPressPipeWithMoreNode = [p for p in midPressPipeInfoWithNodeID if len(p[1])>2 ]
    midPressPipeWithTwoNode = [p for p in midPressPipeInfoWithNodeID if len(p[1])==2 ]
    for p in midPressPipeWithMoreNode:
        start = p[1][0]
        index = 0
        for n in p[1]:
            if n == start:
                continue
            else:
                ID = str(p[0][0])+'-'+str(index)
                index += 1
                element = (ID,p[0][1],[start,n])
                rebulitmidPressPipeWithMoreNode.append(element)
                start = n
    rebulitmidPressPipeTable = midPressPipeWithTwoNode + rebulitmidPressPipeWithMoreNode
    
    #记录
    if flag:
        writecsv2 = open(r'C:\Users\Illusion\Desktop\rebulitmidPressPipeTable.csv','w',newline = '')
        for ID in midPressPipeWithTwoNode:
            writecsv2.write(str(ID[0][0]))
            writecsv2.write(',')
            for e in ID[0][1]:
                writecsv2.write(str(e))
                writecsv2.write(',')
            writecsv2.write(str(ID[1]))
            writecsv2.write(',')
            if ID[0][1][41] == '中压A':
                writecsv2.write(str(0))
            else:
                writecsv2.write(str(1))
            writecsv2.write("\n")
        for ID in rebulitmidPressPipeWithMoreNode:
            writecsv2.write(str(ID[0]))
            writecsv2.write(',')
            for e in ID[1]:
                writecsv2.write(str(e))
                writecsv2.write(',')
            writecsv2.write(str(ID[2]))
            writecsv2.write(',')
            if ID[1][41] == '中压A':
                writecsv2.write(str(0))
            else:
                writecsv2.write(str(1))
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
    edgesInMidPressPipe0 = [tuple([p[1][0],p[1][1],{'ID':p[0][0]}]) for p in midPressPipeWithTwoNode]
    edgesInMidPressPipe1 = [tuple([p[2][0],p[2][1],{'ID':p[0]}]) for p in rebulitmidPressPipeWithMoreNode]
    edgesInMidPressPipe = edgesInMidPressPipe0 + edgesInMidPressPipe1
    G.add_nodes_from(midPressNodeList)
    G.add_edges_from(edgesInMidPressPipe)
    

    #len(list(nx.connected_components(G)))
    result = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    
    
    subG = [c for c in sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)]
    
# =============================================================================
#    计算不同集合内点的距离
#    找到不同集合内距离最近的点 然后建立边 时间上不允许
# =============================================================================
    def distanceBetweenNodes(i,j):
        x,y = nodeTableReverse[i]
        x1,y1 = nodeTableReverse[j]
        return np.sqrt((x-x1)**2. + (y-y1)**2.)
    import copy
    
    #distanceBetweenNodesInDiffSubGs = {}
    def findMinDistInDiffSubGs(G):
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
                        dis = distanceBetweenNodes(e,el)
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
            minDistanceBetweenNodeInDiffSubGs[pointer] = (idt[0],idt[1],mint)
            pointer += 1
        return  minDistanceBetweenNodeInDiffSubGs
        #distanceBetweenNodesInDiffSubGs[pointer] = temp
        
        
    
    pointer = 0
    fixedLines = []
    fixedLinesWithDisValue = []
    while nx.number_connected_components(G) > 1:
       minDistanceBetweenNodeInDiffSubGs =  findMinDistInDiffSubGs(G)
       fixedLine = [(m[0],m[1],{'ID':"fixedLine"})  for m in findMinDistInDiffSubGs(G).values()]
       fixedLinesWithDisValue += [(m[0],m[1],{'ID':"fixedLine",'Dis':m[2]})  for m in findMinDistInDiffSubGs(G).values()]
       G.add_edges_from(fixedLine)
       print(pointer)
       pointer +=1
       fixedLines += fixedLine
    
    
    if flag:
        writecsv4 = open(r'C:\Users\Illusion\Desktop\fixedLinesWithDisValue.csv','w',newline = '')
        
        
        for d in fixedLinesWithDisValue:
            
            writecsv4.write(str(d))
            writecsv4.write("\n")
       
        writecsv4.close()
    
# =============================================================================
#     时间上允许
# =============================================================================
    
    # 绘制CAD图
    drawing = dxf.drawing(r'C:\Users\Illusion\Desktop\中压B经纬度.dxf')
    
    
    drawing.add_layer(
                'points',
                color = 2,
        )
    drawing.add_layer(
                'pipeLabel',
                color = 2,
        )
    drawing.add_layer(
                'fixedConnection',
                color = 2,
        )
    drawing.add_layer(
                'commonNode',
                color = 2,
        )
    drawing.add_layer(
                'elbow',
                color = 2,
        )
    indicator = 0
    
    for sub in subG:
        drawing.add_layer(
                'subG%s'% indicator,
                color = indicator,
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
            #text = dxf.text('pipe%s'%  str(s[2]['ID']), middlePoint, height=0.08, rotation=angle,layer ='pipeLabel'  )
            text['color'] = 0
            
            drawing.add(line)
            drawing.add(text)
        
    
        for i in sub.nodes:
            
            text = dxf.text(i, nodeTableReverse[i], height=0.05, rotation=0,layer ='subG%s'% indicator  )
            if nodeTypeInfoDict[i] == "":
                
                circle = dxf.circle(0.02, nodeTableReverse[i])
                circle['layer'] = 'commonNode'
                circle['color'] = 1
                drawing.add(circle)
            elif nodeTypeInfoDict[i][1] == "弯头":
                x,y = nodeTableReverse[i]
                r = 0.05
                elbowPloyline = dxf.polyline(
                                    points=[
                                        (x - r/2.,y - r*np.sqrt(3)/6.),
                                        (x , y + np.sqrt(3)/3.*r),
                                        (x + r/2., y - r*np.sqrt(3)/6.),
                                        (x - r/2., y - r*np.sqrt(3)/6.),
                                    ],
                                    layer='elbow',
                                    color = 1,
                                    
                                ) 
                drawing.add(elbowPloyline)
            elif nodeTypeInfoDict[i][1] == "三通":
                x,y = nodeTableReverse[i]
                
            elif nodeTypeInfoDict[i][1] == "四通":
                x,y = nodeTableReverse[i]
                
            elif nodeTypeInfoDict[i][1] == "中低压调压站":
                x,y = nodeTableReverse[i]
            elif nodeTypeInfoDict[i][1] == "中中压调压站":
                x,y = nodeTableReverse[i]
            elif nodeTypeInfoDict[i][1] == "高中压调压站":
                x,y = nodeTableReverse[i]
                
            drawing.add(text)
                
                
        indicator += 1
    
  

    
    
    for fixedLine in fixedLines:
        startPoint = nodeTableReverse[fixedLine[0]]
            
        endPoint = nodeTableReverse[fixedLine[1]]
        xdiff = startPoint[0] - endPoint[0]
        ydiff = startPoint[1] - endPoint[1]
        angle = 0
        if np.abs(xdiff)> 1e-5:
            angle = np.arctan(ydiff/xdiff)*180/np.pi
        
        middlePoint = [( startPoint[0] + endPoint[0] ) /2.,( startPoint[1] + endPoint[1] ) /2.]
        line = dxf.line(startPoint, endPoint,layer ="fixedConnection")
        line['color'] = 2
        text = dxf.text("fixedLine", middlePoint, height=0.08, rotation=angle,layer ='pipeLabel'  )
        text['color'] = 0
        
        drawing.add(line)
        drawing.add(text)
    drawing.save()
    
    
    
    






























