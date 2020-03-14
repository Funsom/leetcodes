# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:04:02 2020

@author: Illusion
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import tensorflow as tf
import datetime

matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] ='sans-serif'


def func(filename,picstr,batchSize,dataList,deviceID,isPrint=True):
    excel = pd.read_excel(filename,header=[4],dtype={'对象':np.datetime64},index_col=[1])#
    excel = excel.sort_values(by=['对象'],na_position='first')
    excel.loc[excel[excel['进口压力(kPa)']==  0.0].index,'进口压力(kPa)'] = np.nan
    excel.loc[excel[excel['出口压力(kPa)']==  0.0].index,'出口压力(kPa)'] = np.nan
    excel.index = excel.index.astype('datetime64[ns]')
    
    x = []
    
    data1 = {
            '进口压力(kPa)':np.array([np.nan]*1440),
            '出口压力(kPa)':np.array([np.nan]*1440)
            }
    for data in range(1,batchSize+1):
        if data <10:
            
            a = excel[picstr+'0'+str(data):picstr+'0'+str(data)][['进口压力(kPa)','出口压力(kPa)']]
            print(len(a))
            if len(a) != 1440:
                rng = pd.date_range(picstr+'0'+str(data), periods=1440, freq='T')
                test = pd.DataFrame(data=data1,index=rng)
                for i in range(len(a)):
                    s = a.index[i]
                    test.loc[test[test.index == s].index,['进口压力(kPa)','出口压力(kPa)']] = \
                        list(a[['进口压力(kPa)','出口压力(kPa)']].iloc[i])
        
                x.append(test)
            else:
                x.append(a)
            
        else:
            
            a = excel[picstr +str(data):picstr +str(data)][['进口压力(kPa)','出口压力(kPa)']]
            print(len(a))
            if len(a) != 1440:
                rng = pd.date_range(picstr+str(data), periods=1440, freq='T')
                test = pd.DataFrame(data=data1,index=rng)
                for i in range(len(a)):
                    s = a.index[i]
                    test.loc[test[test.index == s].index,['进口压力(kPa)','出口压力(kPa)']] = \
                        list(a[['进口压力(kPa)','出口压力(kPa)']].iloc[i])
                x.append(test)
            else:
                x.append(a)
        print(data)
    if isPrint:
        
        for ind,i in enumerate(x):
            ax = i.plot(title= picstr + str(ind+1), kind='line', subplots=True)
# =============================================================================
#             ax[0].set_ylim([170,200])
#             ax[1].set_ylim([1,5])
# =============================================================================
            #ylim
            fig = ax[0].get_figure()
            fig.savefig(r'D:\Users\Illusion\Desktop\压力曲线分析\figure\\'+ deviceID + '\\' + picstr + str(ind+1)+'.png')
            plt.close()
    
    dataList.extend(x)

if __name__ == "__main__":
    filenameList = [
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-05-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-06-01-30.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-07-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-08-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-09-01-30.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-10-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-11-01-30.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\19-12-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\20-01-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\久保田农业机械2路艾创_设备序号_00050676\20-02-01-29.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\维苏威铸造_设备序号_00050737\19-11-01-30.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\维苏威铸造_设备序号_00050737\19-12-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\维苏威铸造_设备序号_00050737\20-01-01-31.xls',
        r'D:\Users\Illusion\Desktop\压力曲线分析\维苏威铸造_设备序号_00050737\20-02-01-29.xls',
        
        
    ]
    picstrList = [
        '2019-05-',
        '2019-06-',
        '2019-07-',
        '2019-08-',
        '2019-09-',
        '2019-10-',
        '2019-11-',
        '2019-12-',
        '2020-01-',
        '2020-02-',
        '2019-11-',
        '2019-12-',
        '2020-01-',
        '2020-02-',
    ]
    batchSizeList = [
        31,30,31,31,30,31,30,31,31,29,
        30,31,
        31,29
    ]
    deviceIDList = [
        r'久保田农业机械2路艾创_设备序号_00050676',r'久保田农业机械2路艾创_设备序号_00050676',
        r'久保田农业机械2路艾创_设备序号_00050676',r'久保田农业机械2路艾创_设备序号_00050676',
        r'久保田农业机械2路艾创_设备序号_00050676',r'久保田农业机械2路艾创_设备序号_00050676',
        r'久保田农业机械2路艾创_设备序号_00050676',r'久保田农业机械2路艾创_设备序号_00050676',
        r'久保田农业机械2路艾创_设备序号_00050676',r'久保田农业机械2路艾创_设备序号_00050676',
        r'维苏威铸造_设备序号_00050737',r'维苏威铸造_设备序号_00050737',
        r'维苏威铸造_设备序号_00050737',r'维苏威铸造_设备序号_00050737',
        
    ]
    n = len(filenameList)
    # 不想全部重新生成就改range范围
    dataList = []
    for i in range(n):
        func(filenameList[i],picstrList[i],batchSizeList[i],dataList,deviceIDList[i],isPrint = False)
    LabelList = []
    # 下面开始处理训练的问题
    x_input = [np.array(i) for i in dataList if not i.isnull().values.any()]
    x_input = np.array(x_input)
    
    for i in x_input:
        max1 = max(i[:,0])
        max2 = max(i[:,1])
        i[:,0] /= max1
        i[:,1] /= max2
    y_input = np.random.randint(0,1,241) # mock data
    y_input[np.random.randint(0,241,120)] = 1
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(1440, 2)),
        tf.keras.layers.Dense(128, activation='relu'),
        
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(2, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(x_input, y_input, epochs=50)
    
    #model.evaluate(x_test,  y_test, verbose=2)
    #model.save('all_model.h5')
    #model = tf.keras.models.load_model('all_model.h5')
    model.summary()
    current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = 'logs/' + current_time
    summary_writer = tf.summary.create_file_writer(log_dir)
    
    
    



