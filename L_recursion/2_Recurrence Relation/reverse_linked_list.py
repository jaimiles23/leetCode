"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-20 20:02:40
 * @modify date 2019-11-22 11:40:34
 * @desc [
leetCode's Reverse linked list problem, available [here](https://leetcode.com/problems/reverse-linked-list/)

There are two fundamentally different ways to approach this problem:
1. Recursively
2. Iteratively

## Recursive
To solve this problem recursively, we must determine how the larger problem is broken into subproblems, and what the smallest
subproblem is. To accomplish this, we must solve for the recursive relation and the base case.

### Outcome
To reverse a list of nodes, represented by L(n), we must reverse the order of nodes. Thus:
L(0), L(n) = L(n), L(0)
L(1), L(n-1) = L(n-1), L(n)
L(2), L(n-2) = L(n-2), L(2)
...

### Base case
If the last node is reached, return that node as the head. Thus:
L(n).next == None:
    return head

### Recursive relation
In order to reverse the linked list, you only need to look at two nodes while transversing the linked list:
1. The current (soon to be previous) node
2. The next (soon to be current) node, which should point at the previous node

### Function steps
1. The base case: if node == None or node.next == None
2. Recursion used to go to end of the tree. This is used to assign the new head, and tsart the next 2 steps at the end.
- head.next.next means the next node's next method will point to this node
- head.next = None such that first node becomes the tail. Recursion still functions because previous path in memory.
3. Return end node.

### leetCode Diagnostics:
Runtime: 36 ms, faster than 88.21% of Python3 online submissions for Reverse Linked List.
Memory Usage: 17.3 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.

### Thoughts
I struggled a lot with this solution. I will do a few more recursive leetCode challenges, and then move onto the 
listNode Explore Card. It was difficult for me to translate the recursive relation into function steps, and I attribute 
some of the difficulty to having less experience working with listNodes.
 ]
 */

## Iterative Solution
This solution follows the same approach as recursion. It looks at two list nodes at a time, and assigns next status. It will
return the final node as the head.

Note: referred to [moonlight16's solution)[https://leetcode.com/problems/reverse-linked-list/discuss/434665/Simple-in-place-Python-solution]

### leetCode diagnostics:
Runtime: 32 ms, faster than 95.74% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.

### Thoughts
I was able to brute force my way through this solution, albeit not very elegantly. Ultimately, I looked at other's code
for more guidance. This reinforces the indication that I need more practice working with listNodes.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class RecursiveSolution(): 
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        returns reversed ListNodes using recursion
        """
        # Base case
        if head == None or head.next == None:
            return head
        
        answer = self.reverse_list(head.next)   

        head.next.next = head  
        head.next = None

        return answer


class IterativeSolution():
    def reverse_list(self, head: ListNode) -> ListNode:
        """
        returns reversed listNodes using iteration
        """
        previous = None

        while head != None:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
                    
        return previous


def test_reverse_list():
    """
    runs unit tests for reverse lists
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

    print('test 1')
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next, n2.next, n3.next = n2, n3, n4
    output = tester.reverse_list(n1)

    while output.next != None:
        print(output.val)
        output = output.next
    print(output.val)


def main():
    test_reverse_list()


if __name__ == "__main__":
    main()