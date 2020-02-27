import numpy as np
class KDNode(object):
    '''
    定义KD节点：
    point:节点里面的样本点，指的就是一个样本点
    split:分割纬度（即用哪个纬度的数据进行切分，比如4维数据，split=3，则表示按照第4列的数据进行切分空间）
    left:节点的左子节点
    right:节点的右子节点
    '''
    def __init__(self, point=None, split=None, left=None, right=None):
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


    def __init__(self, data=None):
          
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
            '''
            #返回KD节点
            #输入的变量分别是：
            #data_set[median]，中间点位置的样本点，传入KDNode即节点里面包含的数据
            #split，该节点的纬度分度位置
            #createNode(maxVar(data_set[:median]),data_set[:median])，该节点的左节点，maxVar(data_set[:median])为左节点的纬度分度位置，data_set[:median]为左节点包含的空间里的所有数据
            #同理，createNode(maxVar(data_set[median+1:]),data_set[median+1:])，为右节点。
            #用的是函数的递归创建树，因为要不断的调用函数，这个方法速度不快，用基本语句（判断、循环）去构建树的方法会更快
            '''
            
            return KDNode(data_set[median], split)
            #return KDNode(data_set[median], split, createNode(maxVar(data_set[:median]),data_set[:median]), createNode(maxVar(data_set[median+1:]),data_set[median+1:]))
            
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
        
        self.root = KDNode() #createNode(maxVar(data),data)#定义根节点，分割纬度是使得样本点方差最大的纬度，需要分割的样本点为全数据
        head = self.root
        queue = [(head,data)]
        while queue:
            root,data_set = queue.pop(0)
            n = len(data)
            if n == 0:
                continue
            split = maxVar(data_set)
            print(split)
            data_set = list(data_set)
            data_set.sort(key=lambda x: x[split])#对data_set进行排序，lambda是隐函数，具体用法请百度。排序方式为按照split维的数据大小排序
            data_set = np.array(data_set)
            median = len(data_set) // 2
            root.point = data_set[median]
            root.split = split
            if len(data_set[:median]) > 0:
                root.left = KDNode()
                queue.append((root.left,data_set[:median]))
            if len(data_set[median+1:]) >0:
                root.right = KDNode()
                queue.append((root.right,data_set[median+1:]))
    def inOrderKD(self):
        '''
        KD树的前序遍历
        '''
        def inOrder(root):
            if not root: return
            if root.left:
                inOrder(root.left)
            print(root.point,root.split)
            if root.right:
                inOrder(root.right)
        inOrder(self.root)
    def preOrderKD(self):
        '''
        KD树的前序遍历
        '''
        def preOrder(root):
            if not root: return
            print(root.point,root.split)
            if root.left:
                preOrder(root.left)
            if root.right:
                preOrder(root.right)
        preOrder(self.root)

if __name__ == "__main__":
    kdtree = KDTree([(1,2,3),(2,8,4),(8,19,1)])
    kdtree.preOrderKD()