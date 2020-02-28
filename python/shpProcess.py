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
#from dpfpy import dbfread


path = r'D:\GASNET_Local\DOCUMENT\1128GEODATA'
filenames = os.listdir(path)
fileList = []
for filename in filenames:
    if os.path.splitext(filename)[1] == '.shp':
        fileList.append(os.path.splitext(filename)[0])


def WriteData(filelist):
    shpName = "D:/GASNET_Local/DOCUMENT/1128GEODATA/%s.shp" % (filelist)
    
    sf = shapefile.Reader(shpName,encoding='gbk')

    shapes = sf.shapes()
    records = sf.records()
# =============================================================================
# =============================================================================
#     records = sf.records()
#     fileds = sf.fields
# =============================================================================
    if shapes:

        print(filelist+',    '+shapes[0].shapeTypeName + str(records[0]))
    #writer.writerow(fileds)
# =============================================================================
#     if shapes:
#         try:
#             #index = fileds.index(['SID', 'C', 254, 0])
#             
# # =============================================================================
# #             dirName = r'D:/'+records[0][index-1]+'.csv'
# # 
# #             csvFile = open(dirName,'w',newline = '')
# #         
# #             writer = csv.writer(csvFile)
# # =============================================================================
#         except:
#             print("error")
#         else:
#             print("right")
# 
# =============================================================================
    

    

    
            
# =============================================================================
# =============================================================================
#     fileds = sf.fields
#     li = list(zip(fileds[1:],record[1]))
# =============================================================================
# =============================================================================
#     a =[]
#     for r in records:
#         a.append(r[41])
# # =============================================================================
#     c = collections.Counter(a)
#     print(c.elements)
# =============================================================================
# =============================================================================
    
    # start =[]
    # end =[]

# =============================================================================
#     for shape,record in zip(shapes,records):
#         # start.append(shape.points[0][0])
#         # start.append(shape.points[1][0])
#         # end.append(shape.points[0][1])
#         # end.append(shape.points[1][1])
#         #strs = str([shape.points[0][0],shape.points[0][1]])+","+str([shape.points[1][0],shape.points[1][1]])+",,"+"\n"
#         #print(record[41])
#         #if(record[41] == '中压A'):
#         li = record+list(shape.points[0])
#         if(writer):
#             writer.writerow(li)
# =============================================================================
             
# =============================================================================
#             strs = str(shape.points[0][1])+','+str(shape.points[0][0])
#             f.write(strs)
#             for r in record:
#                 f.write(",")
#                 f.write(r)
#             
#             f.write("\n")
#     f.close()
# =============================================================================
        
        #plt.plot([shape.points[0][0],shape.points[1][0]],[shape.points[0][1],shape.points[1][1]],'r--')
        #temp = [str(num),str(shape.points[0]),str(shape.points[1]),None]

        #writer.writerow(temp)

    #plt.scatter(start,end)
    # maxX = np.max(start) 
    # minX = np.min(start)
    # maxY = np.max(end)
    # minY = np.min(end)
    # diffX= maxX-minX
    # diffY= maxY-minY
    #csvFile.close()

    #print(roadName+ ' is ' + str(lineth) + 'points\n'+ 'and ' + str(num) + ' roads\n')
#WriteData("BUILDINGNO_N")
    
# =============================================================================
for f in fileList:
    WriteData(f)
# =============================================================================
'''
读取DBF文件
'''
# =============================================================================
# def readDbfFile(filename):
#     table = dbfread.DBF(filename, encoding='GBK')
# 
#     for field in table.fields:
#         print(field)
# 
#     for record in table:
#         for field in record:
#             print(field, record[field])
# 
#     for delete_record in table.delete:
#        print(delete_record)
# 
# =============================================================================
#readDbfFile(r"D:\GASNET_Local\DOCUMENT\1128GEODATA\PIPE_N.dbf")



