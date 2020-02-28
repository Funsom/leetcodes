# -*- coding: utf-8 -*-
'''
用于MET-flow的管网数据生成
从Excel文件中读取数据，生成对应的
MET-flow Data数据

'''

import xlrd
import numpy as np
import networkx as nx
#import matplotlib.pyplot as plt

# 引入图论工具
# Creating a Graph

G = nx.Graph() # Right now G is empty

'''
文件输入
'''
path = r"C:\Users\Administrator\Desktop\简单环网.xlsx"
#path = r"D:\管道仿真软件\云龙工业园\云龙工业园\CE地块云龙工业园基础管线.xlsx"
data = xlrd.open_workbook(path)

sheet_1_by_name = data.sheet_by_name(r'CE地块基础管线数据')
sheet_2_by_name = data.sheet_by_name(r'节点流量')


node_list_1 = sheet_1_by_name.col_values(1)[2:-1]
node_list_2 = sheet_1_by_name.col_values(2)[2:-1]

demand_list_name = sheet_2_by_name.col_values(1)[2:-1]
demand_list_value = sheet_2_by_name.col_values(3)[2:-1]

pipe_len_list = sheet_1_by_name.col_values(3)[2:-1]
pipe_diam_list = sheet_1_by_name.col_values(4)[2:-1]
diff = np.array(pipe_diam_list) - np.array([np.floor(i) for i in pipe_diam_list ])
pdl = np.array(pipe_diam_list)
pdl[diff < 0.02] += 0.01
pipe_diam_list= pdl.tolist()






'''
交叉合并的收尾节点列表
'''
node_list = [rv for r in zip(node_list_1,node_list_2) for rv in r] 

'''
获取有序的节点名称列表
'''
formatted_node_list = list(set(node_list))
formatted_node_list.sort(key=node_list.index)


node_list_len = len(formatted_node_list)
node_index_list = [ i+1 for i in range(node_list_len)]


'''
图添加节点和边
'''

G.add_nodes_from(node_list)
G.add_edges_from(list(zip(node_list_1,node_list_2)))
cycle_basis = nx.cycle_basis(G)
cycle_num = len(cycle_basis)
#nx.draw(G, with_labels=True, font_weight='bold')





'''
管网信息中节点的序号
'''
node_index_1 = [formatted_node_list.index(i)+1 for i in node_list_1]
node_index_2 = [formatted_node_list.index(i)+1 for i in node_list_2]

'''
管网中有供气需求信息的节点的序号
'''
demand_index  = [formatted_node_list.index(i) for i in demand_list_name]

'''
管网中管道的序号
'''
pipe_list_len = len(node_list_1)
pipe_index_list = [ i+1 for i in range(pipe_list_len)]

zero = [0 for i in range(pipe_list_len)]
'''
关联需求与节点
'''
demand_list = [0 for i in range(node_list_len)]
for i in range(len(demand_list_name)):
    demand_list[demand_index[i]] = demand_list_value[i]


'''
按指定格式生成data文件
'''

str1 = 'CE,2019/08/23, 0 , 0 , 0 '
str2 = ' %s  %s  %s  1  0  0  0' % (cycle_num,G.number_of_edges(), G.number_of_nodes())
str3 = ' 0  0  1  0  1  0  0 '
str4 = 'Project'
head = [str1,str2,str3,str4]

table = list(zip(pipe_index_list,node_index_1,node_index_2,pipe_diam_list,pipe_len_list,zero))
node_table = list(zip(node_index_list,formatted_node_list,demand_list,zero))
file = open("CE.BAK",'w')
for row in head:
    file.write(row)
    file.write('\n')
file.write('\n')
for row in table:
    string = " " + str(row).replace(',',' ').replace('(','').replace(')','') + " "
    file.write(string)
    file.write('\n')
for row in node_table:
    string = " " + str(row[0]) + " " + str(row[1])+", "+str(row[2]) + "  "+str(row[3])+" "
    file.write(string)
    file.write('\n')
file.close()
    

