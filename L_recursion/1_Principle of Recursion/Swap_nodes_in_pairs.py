"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-19 16:07:27
 * @modify date 2019-11-19 16:07:27
 * @desc [
Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

LeetCode Diagnostics:
Runtime: 24 ms, faster than 98.52% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
    ]
 */
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        returns linked list with every two adjacent nodes switched.
        """
        # Base case
        if head == None or head.next == None:
            return head

        # Switch two nodes
        n3 = head.next.next
        head, head.next = head.next, head
        head.next.next = n3

        # Recursive call
        head.next.next = self.swapPairs(head.next.next)

        return head
            
            
            