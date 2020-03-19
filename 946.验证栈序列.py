#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        #if  pushed == popped: return True
        # 至多有一个逆序
        dic = {}
        n = len(popped)
        nin = len(pushed)
        if n != nin: return False
        for ind,ele in enumerate(pushed):
            dic[ele] = ind
        if popped[0] not in dic: return False
        count = 0
        for i in range(1,n):
            if popped[i] not in dic: return False
            if dic[popped[i]] - dic[popped[i-1]] > 1:
                return False
            elif dic[popped[i]] - dic[popped[i-1]] == 1:
                count += 1
                if count > 1:
                    return False
            
        # if count == 1 and pushed[:2] == popped[-2:]:
        #     return False 
        return True
if __name__ == "__main__":
    s = Solution()
    pushed = [2,1,0]
    poped = [1,2,0]
    print(s.validateStackSequences(pushed,poped))
# @lc code=end

