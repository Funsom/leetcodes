#-*- coding:utf8 -*-
'''
算法第四版代码实现
'''
from timeit import Timer
from random import shuffle
class SortAlgorithm(object):
    def __init__(self):
        pass
    def SelectionSort(self,lists):
        if not lists: return []
        lens = len(lists)
        for i in range(lens):
            minIndex = i
            for j in range(i+1,lens):
                if lists[j] < lists[minIndex]:
                    minIndex = j
            lists[i],lists[minIndex] = lists[minIndex],lists[i]
        return lists
    def InsertionSort(self,lists):
        if not lists: return []
        lens = len(lists)
        for i in range(1,lens):
            j = i - 1
            while j >= 0:
                if lists[j] > lists[i]:
                    lists[i],lists[j] = lists[j],lists[i]
                    j -= 1
                    i -= 1
                else:
                    break
        return lists

    def QuickSort(self,lists):
        shuffle(lists)
        self.__QuickSort__(lists,0,len(lists)-1)
        return lists
    def __QuickSort__(self,lists,lo,hi):
        if hi <= lo: return
        j = self.__partition__(lists,lo,hi)
        self.__QuickSort__(lists,lo,j-1)
        self.__QuickSort__(lists,j+1,hi) 
        
    def __partition__(self,lists,lo,hi):
        i,j = lo+1,hi-1
        v = lists[lo]
        while True:
            while lists[i] < v:
                i += 1
                if i == hi:
                    break 
            while lists[j] > v:
                j -= 1
                if j == lo:
                    break
            if i >= j:
                break

        lists[lo],lists[j] = lists[j],lists[lo]
        return j
if __name__ == "__main__":
    lists = [100,2,0,80,78]
    sortAlgorithm = SortAlgorithm()
    #res = sortAlgorithm.SelectionSort(lists)
    #res = sortAlgorithm.InsertionSort(lists)
    res = sortAlgorithm.QuickSort(lists)
    
    print(res)