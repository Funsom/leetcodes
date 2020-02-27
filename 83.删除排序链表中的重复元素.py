#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = head
        post = head.next
        while post:
            if pre.val == post.val:
                post = post.next
            else:
                pre.next = post
                pre = post
                post = post.next
        pre.next = None
        return dummyHead.next



# @lc code=end

