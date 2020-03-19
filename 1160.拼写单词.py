#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        from collections import Counter
        import copy
        dic = Counter(chars) 
        flag = False
        res = []
        for i in words:
            copys = copy.deepcopy(dic)
            for c in i:
                if c not in copys:
                    flag = True
                    break
                else:
                    if copys[c] != 0:
                        copys[c] -= 1
                    else:
                        flag = True
                        break
            if not flag:
                res.append(i)
            flag = False
        return len(''.join(res))

# if __name__ == "__main__":
#     s = Solution()
#     word = ["hello","world","leetcode"]
#     chars = "welldonehoneyr"
#     res = s.countCharacters(word,chars)
#     print(res)

# @lc code=end

