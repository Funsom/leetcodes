import numpy as np
'''
Created on 2017年7月17日

@author: fujianfei
'''

class KDNode(object):
    '''
    定义KD节点：
    point:节点里面的样本点，指的就是一个样本点
    split:分割纬度（即用哪个纬度的数据进行切分，比如4维数据，split=3，则表示按照第4列的数据进行切分空间）
    left:节点的左子节点
    right:节点的右子节点
    '''


    def __init__(self, point=None, split=None, left=None, right=None):
        '''
        Constructor
        '''
        self.point = point
        self.split = split
        self.left = left
        self.right = right
        
        
class KDTree(object):
    '''
    定义：
    KDNode:kd-tree的节点
    dimensions:数据的纬度
    right:节点的右子节点
    left:节点的左子节点
    curr_axis:当前需要切分的纬度
    next_axis:下一次需要切分的纬度
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        """        
        def createNode(split=None, data_set=None):
            '''
            创建KD节点
            输入值：split:分割纬度 data_set:需要分割的样本点集合
            返回值：KDNode:KD节点
            '''
            if len(data_set) == 0:    # 数据集为空，作为递归的停止条件
                return None
            #找到split维的中位数median,先对数据进行排序，按照split维的数据大小排序
            data_set = list(data_set)
            data_set.sort(key=lambda x: x[split])#对data_set进行排序，lambda是隐函数，具体用法请百度。排序方式为按照split维的数据大小排序
            data_set = np.array(data_set)
            median = len(data_set) // 2#//为python的整数除法，找到中间点的位置median，按照这个位置进行空间切分
            #返回KD节点
            #输入的变量分别是：
            #data_set[median]，中间点位置的样本点，传入KDNode即节点里面包含的数据
            #split，该节点的纬度分度位置
            #createNode(maxVar(data_set[:median]),data_set[:median])，该节点的左节点，maxVar(data_set[:median])为左节点的纬度分度位置，data_set[:median]为左节点包含的空间里的所有数据
            #同理，createNode(maxVar(data_set[median+1:]),data_set[median+1:])，为右节点。
            #用的是函数的递归创建树，因为要不断的调用函数，这个方法速度不快，用基本语句（判断、循环）去构建树的方法会更快
            
            
            return KDNode(data_set[median], split, createNode(maxVar(data_set[:median]),data_set[:median]), createNode(maxVar(data_set[median+1:]),data_set[median+1:]))
            return KDNode(data_set[median], split, createNode(maxVar(data_set[:median]),data_set[:median]), createNode(maxVar(data_set[median+1:]),data_set[median+1:]))
        """
        """
        def maxVar(data_set=None):
            '''
            按纬度计算样本集的最大方差纬度
            输入值:data_set:样本集
            输出值:split:最大方差的纬度，作为createNode的输入值
            '''
            if  len(data_set) == 0:    # 数据集为空，作为递归的停止条件
                return 0
            data_mean = np.mean(data_set,axis=0)#axis=0表示按列求均值
            mean_differ = data_set - data_mean#均值差
            data_var = np.sum(mean_differ ** 2,axis=0)/len(data_set)#按列求均值差平方之和，再除以样本数，便是方差
            re = np.where(data_var == np.max(data_var))#寻找方差最大的位置，也就是第几纬方差最大，返回它
            return re[0][0]
        """
        self.root = KDNode() #定义根节点，分割纬度是使得样本点方差最大的纬度，需要分割的样本点为全数据
        
        k = len(data[0])
        self.k = k
        head = self.root
        split = 0
        queue = [(head,data)]
        while queue:
            root,data_set = queue.pop(0)
            n = len(data_set)
            
            if n == 0:
                continue

            #print(split)
            data_set = list(data_set)
            data_set.sort(key=lambda x: x[split])#对data_set进行排序，lambda是隐函数，具体用法请百度。排序方式为按照split维的数据大小排序
            data_set = np.array(data_set)
            median = n // 2
            root.point = data_set[median]
            root.split = split
            if median > 0: # if len(data_set[:median]) > 0:
                root.left = KDNode()
                queue.append((root.left,data_set[:median]))
            if median+1 < n:
                root.right = KDNode()
                queue.append((root.right,data_set[median+1:n]))
            split = (split + 1) % k
    def add(self,point):
        root = self.root
        while root:
            split = root.split
            if point[split] < root.point[split] and not root.left :
                root.left = KDNode(point,(split + 1) % self.k)
                break
            elif point[split] > root.point[split] and not root.right :
                root.right = KDNode(point,(split + 1) % self.k)
                break
            elif point[split] < root.point[split]:
                root = root.left
            elif point[split] > root.point[split]:
                root = root.right
        return self.root
    def levelOrder(self):
        cur_layer = [self.root]
        res = []
        while cur_layer:
            temp = []
            next_layer = []
            for i in cur_layer:
                temp.append(i.point)
                if i.left: next_layer.append(i.left)
                if i.right: next_layer.append(i.right)
            cur_layer = next_layer
            res.append(temp)
        return res
    
    
def computeDist(pt1, pt2):
    """
    计算两个数据点的距离
    return:pt1和pt2之间的距离
    """
    sums = 0.0
    for i in range(len(pt1)):
        sums = sums + (pt1[i] - pt2[i])**2.
    return np.math.sqrt(sums)
        
def preOrder(root):
    '''
    KD树的前序遍历
    '''
    print(root.point)
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

def updateNN(min_dist_array=None, tmp_dist=0.0, NN=None, tmp_point=None, k=1):
    '''
    /更新近邻点和对应的最小距离集合
    min_dist_array为最小距离的集合
    NN为近邻点的集合
    tmp_dist和tmp_point分别是需要更新到min_dist_array，NN里的近邻点和距离
    '''
    
    if tmp_dist <= np.min(min_dist_array) : 
            for i in range(k-1,0,-1) :
                min_dist_array[i] = min_dist_array[i-1]
                NN[i] = NN[i-1]    
            min_dist_array[0] = tmp_dist
            NN[0] = tmp_point                
            return NN,min_dist_array
    for i in range(k) :
        if (min_dist_array[i] <= tmp_dist) and (min_dist_array[i+1] >= tmp_dist) :
            #tmp_dist在min_dist_array的第i位和第i+1位之间，则插入到i和i+1之间，并把最后一位给剔除掉
            for j in range(k-1,i,-1) : #range反向取值
                min_dist_array[j] = min_dist_array[j-1]
                NN[j] = NN[j-1]
            min_dist_array[i+1] = tmp_dist
            NN[i+1] = tmp_point
            break
    return NN,min_dist_array

def searchKDTree(KDTree=None, target_point=None, k=1):  
    '''
    /搜索kd树
    /输入值:KDTree,kd树;target_point,目标点；k,距离目标点最近的k个点的k值
    /输出值:k_arrayList,距离目标点最近的k个点的集合数组
    '''      
    if k == 0 : return None
    #从根节点出发，递归地向下访问kd树。若目标点当前维的坐标小于切分点的坐标，则移动到左子节点，否则移动到右子节点
    tempNode = KDTree.root#定义临时节点，先从根节点出发
    NN = [tempNode.point] * k#定义最邻近点集合,k个元素，按照距离远近，由近到远。初始化为k个根节点
    min_dist_array = [float("inf")] * k#定义近邻点与目标点距离的集合.初始化为无穷大
    nodeList = []#我们是用二分查找建立路径，定义依次查找节点的list

    def buildSearchPath(tempNode=None, nodeList=None, min_dist_array=None, NN=None, target_point=None):
        '''
        P:此方法是用来建立以tempNode为根节点，以下所有节点的查找路径，并将它们存放到nodeList中
        nodeList为一系列节点的顺序组合，按此先后顺序搜索最邻近点
        tempNode为"根节点",即以它为根节点，查找它以下所有的节点（空间）
        '''
        while tempNode :
            nodeList.append(tempNode)
            split = tempNode.split#节点的分割纬度
            point = tempNode.point#节点包含的数据,当前实例点
            tmp_dist = computeDist(point,target_point)
            if tmp_dist < np.max(min_dist_array) : #小于min_dist_array中最大的距离
                NN,min_dist_array = updateNN(min_dist_array, tmp_dist, NN, point, k)#更新最小距离和最邻近点
            if  target_point[split] <= point[split] : #如果目标点当前维的值小于等于切分点的当前维坐标值，移动到左节点
                tempNode = tempNode.left
            else : #如果目标点当前维的值大于切分点的当前维坐标值，移动到右节点
                tempNode = tempNode.right
        return NN,min_dist_array
    #建立查找路径
    NN,min_dist_array = buildSearchPath(tempNode,nodeList,min_dist_array, NN, target_point)
    #回溯查找
    while nodeList :
        back_node = nodeList.pop()#将nodeList里的元素从后往前一个个推出来
        split = back_node.split
        point = back_node.point
        #判断是否需要进入父节点搜素
        #如果当前纬度，目标点减实例点大于最小距离，就没必要进入父节点搜素了
        #因为目标点到切割超平面的距离很大，那邻近点肯定不在那个切割的空间里，即没必要进入那个空间搜素了
        if not abs(target_point[split] - point[split]) >= np.max(min_dist_array) :
            #判断是搜索左子节点，还是搜索右子节点
            if (target_point[split] <= point[split]) :
                #如果目标点在左子节点的空间，则搜索右子节点，查看右节点是否有更邻近点
                tempNode = back_node.right
            else :
                #如果目标点在右子节点的空间，则搜索左子节点，查看左节点是否有更邻近点
                tempNode = back_node.left
            
            if tempNode :
                #把tempNode（此时它为另一个全新的未搜素的空间，需要将它放入nodeList，进行最近邻搜索）放入nodeList
                #nodeList.append(tempNode)
                #不能单纯地将tempNode存放到nodeList，这样下次只会搜索这一个节点
                #因为tempNode可做为一个全新的空间，故而需重新以它为根节点，构建查找路径，搜索它名下所有的节点
                NN,min_dist_array = buildSearchPath(tempNode,nodeList,min_dist_array, NN, target_point)

    return NN,min_dist_array 

def classify0(inX, dataSet, labels, k):
    '''
    k近邻算法的分类器
    \输入：
    inX:目标点
    dataSet:训练点集合
    labels:训练点对应的标签
    k:k值
    \这个方法的目的：已知训练点dataSet和对应的标签labels，确定目标点inX对应的labels
    ''' 
    kd = KDTree(dataSet)#构建dataSet的kd树
    NN,min_dist_array = searchKDTree(kd, inX, k)#搜索kd树，返回最近的k个点的集合NN，和对应的距离min_dist_array
    dataSet = dataSet.tolist()
    voteIlabels = []
    #多数投票法则确定inX的标签，为防止边界处分类不准的情况，以距离的倒数为权重，即距离越近，权重越大，越该认为inX是属于该类
    for i in range(k) :
        #找到每个近邻点对应的标签
        nni = list(NN[i])
        voteIlabels.append(labels[dataSet.index(nni)])
        
#     #开始记数,加权重的方法
#     uniques = np.unique(voteIlabels)
#     counts = [0.0] * len(uniques)
#     for i in range(len(voteIlabels)) :
#         for j in range(len(uniques)) :
#             if voteIlabels[i] == uniques[j] :
#                 counts[j] = counts[j] + uniques[j] / min_dist_array[i] #权重为距离的倒数
#                 break
    #开始记数,不加权重的方法
    uniques, counts = np.unique(voteIlabels, return_counts=True)
    return uniques[np.argmax(counts)]


            



if __name__ == "__main__":
    f = open(r'D:\Users\Illusion\Desktop\Desktop.csv','r')
    data = f.readlines()
    data = [tuple([float(a) for a in i.split(',')])  for i in data]
    
    kdtree = KDTree(data)
    kdtree.add([117.2445,34.26261])
    #preOrder(kdtree.root)
    for ind,i in enumerate(data):
        knn = searchKDTree(kdtree, i, k=1)
        #print(ind,knn[1])
    
    #knn = searchKDTree(kdtree, [117.2445,34.26261], k=1)
    #print(knn[1])
    for ind,i in enumerate(kdtree.levelOrder()):
        print(ind,i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    