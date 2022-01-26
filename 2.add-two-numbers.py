#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        n1 = self.getNum(l1)
        n2 = self.getNum(l2)

        sum    = str(n1 + n2)[::-1]
        sum_ln = None
        last   = None

        for n in sum:
            if not sum_ln:
                sum_ln = ListNode(int(n))  # type: ignore
                last   = sum_ln

            else:
                next      = ListNode(int(n))  # type: ignore
                last.next = next
                last      = next

        return sum_ln

    def getNum(self, node):
        n = 0
        i = 1

        while node:
            n    += node.val * i
            node  = node.next
            i    *= 10

        return n
# @lc code=end

