"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-26 12:21:51
 * @modify date 2019-11-26 13:20:23
 * @desc [
Solutions to leetCode's [#21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Initial consideration indicates two different approaches to the problem:
1. Recursive
2. Iterative

Both of these solutions will compare the min of the lists nodes, and select the nose with the min(val)

## Recursive

### Basecase: 
if l1 == None: return l2
elif l2 == None: return l1

### Recursive relation
    node = min(l1, l2)
    node.next = self.mergeTwoLists(node.next, not_node)

### Complexity Analysis
#### Time complexity
O(N) - must cycle through all nodes in the lists

#### Space complexity
O(N) - Stack overhead contains N recursion calls, and constant O(1) space for l1, l2, node, and not_node.

### LeetCode Diagnostics:
Runtime: 28 ms, faster than 98.93% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

## Iterative solution
This follows the same approach as the recursive solution: Test for list node's min val and assign that ListNode 
as node.next.  

This uses a l1 != None and l2 != None while loop. Thus, after the while loop, the remaining listNode is assigned to
node.next

### Complexity Analysis
#### Time Complexity
O(N) - In worstcase, all elements of the lists are cycled through. Best case, only one list is cycled through and 
the other ListNode is appended to the end. Also note: for each listNode there is a comparison operator and variable assignment,
both of which have constant O(1) time complexity and not considered in Big O notation.

#### Space Complexity
O(1) as there is constant space complexity. Space is assigned to the variables: l1, l2, head, and node.

### LeetCode Diagnostics:
Runtime: 20 ms, faster than 99.99% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

### Notes:
In theory, this solution should have less memory usage and same runtime. In the low number of tests I have run, the recursion
solution runs faster. Note to self: investigate more into this later.
 ]
 */
"""

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


class RecursiveSolution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        returns new merged sorted linked list using recursion
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val < l2.val:
            node = l1
            not_node = l2
        else: 
            node = l2
            not_node = l1

        node.next = self.mergeTwoLists(node.next, not_node)
        return node

        
class IterativeSolution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Returns merged, sorted list using iteration
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val < l2.val:
            head = l1
        else: 
            head = l2
        
        node = head

        while l1 and l2 != None:
            if l1.val < l2.val:
                next_node = l1
                l1 = l1.next
            else:
                next_node = l2
                l2 = l2.next

            node.next = next_node
            node = node.next
        
        if l1 != None:
            node.next = l1
        else: 
            node.next = l2

        return head


def test_solutions():
    """
    runs unit tests for # 21
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

    node1 = ListNode(1, ListNode(2, ListNode(4)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    output = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    node = tester.mergeTwoLists(node1, node2)

    print('node', 'output', 
        sep = '\t')
    while node != None:
        print(node.val, output.val, 
            sep = '\t')
        node, output = node.next, output.next


def main():
    test_solutions()


if __name__ == '__main__':
    main()
