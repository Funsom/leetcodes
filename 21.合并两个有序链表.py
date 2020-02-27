#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        if not l1: return l2
        if not l2: return l1
        
        if l1.val <= l2.val:
            dummyHead.next = l1
            l1 = l1.next
        else:
            dummyHead.next = l2
            l2 = l2.next
        p = dummyHead.next
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        if not l1:
            p.next = l2
        else:
            p.next = l1
        return dummyHead.next





# @lc code=end

