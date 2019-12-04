"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-01 13:10:43
 * @modify date 2019-12-01 22:35:43
 * @desc [

# Binary tree level order traversal
This script contains solutions to leetCode's [Binary tree level order traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Binary tree level order traversal searches each level of a binary tree before searching the next level.
This is a type of Breadth First Search (BFS) algorithm.

Two dynamic programming approaches can be used to create a BFS algorith:
1. Recursion
2. Iterative

## RecursiveSolution

### Base case
root.left == None: return root.val
root.right == None: return root.val

### Recursive relation
F(root) = [root.val] + F(root.left + root.right) 

### Complexity Analysis
#### Time complexity
O(T) = R * O(s)
    = O(N) * O(1)
    = O(N)

#### Space complexity
= Recursive related space + non_Recursive related space
= Recursive stack (address, parameters, local variables) + global var tree_vals
= O(N) + O(N)
= O(2N)
= O(N)
** Practically worth noting that this is a 2-pass O(N) solution, 
however I think because all node.vals are stored, all memory solutions will be O(2N).

### leetCode diagnostics:
Runtime: 24 ms, faster than 99.55% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.4 MB, less than 61.29% of Python3 online submissions for Binary Tree Level Order Traversal.

## IterativeSolution1()
Tree Traversal iterative solutions typically contain two lists:
    1. tree_vals, to store the results
    2. todo_stack, to hold the next nodes to evaluate
This algorithm also has a third list:
    3. next_level, to hold nodes that will be placed in the next level.

Note: another solution may use a similar (n) integer and store an n corresponding to each node. However, 
having a separate list to represent the next level should save memory, by removing pointers in large sets. 

Additionally, this solution uses two while: loops. While this theoretically evaluates to O(N ** 2), it will never
reach O(N ** 2) because each listNode will only be evaluated once.

### Notes on challenge:

The method for IterativeSolution1() did _not_ work because of the use of the next_level list. 

The issue with using the next_level list is that the items are added in an order that does not represent the
left_most node. The root.left.left may be added to the list first, and then the root.right.right.
The will cause the to_do stack to read the root.right.right value first, and disrupt the order of results
in tree_vals.

I scrapped the solution and moved to the conventional solution of using two lists, with a level integer. Using 
a single todo_stack means that the left_most tree values will always be prioritized. With 2 lists, 
the order of values will be variable. 

Because of this, _I riverted to using an iterative solution with an 'n' integer to indicate the level_.
I implemented this iterative solution using both BFS and DFS algorithms. The key difference between the 
implementation of these two algorithms is the order that nodes are added to the stack, and the order
that nodes are removed from thes tack
- **BFS** adds node.left and node.right to the end of the stack, and accesses elements using pop(0)
- **DFS** adds node.right and node.left to the end of the stack, and accesses elements using pop()

## BfsSolution()
Breadth First Search algorithm searches an entire row before moving to the next. 

### Steps
While todo_stack:
    1. Start with top node, n = 0
    2. tree_vals[n].append(node.val)        # append to appropriate level
    3. todo_stack.append(node.left, n + 1)
    4. todo_stack.append(node.right, n + 1)
    5. node, n = todo_stack.pop(0)

The key to this method is taking the first element from the to_do list. Because the nodes are added all from 
one level before adding the next, in a left -> right order, the node order will be correct. 
_Note_: n is used to track the level to append to the list. 

### Complexity analysis
#### Time complexity
O(N) goes through the entire list

#### Space complexity
O(2N) because of the todo_stack and the tree_vals. 
However, in practice no more than O(N) will ever be instantiated. 

## DfsSolution()
Depth first search algorithm is quite similar to the BFS. The key difference is that the last element of the list
is used as the next node. 

### Steps
While todo_stack:
    1. node, n  = root, 0
    2. tree_vals[n].append(node.val)    #append val to appropriate level
    3. todo_stack.append(node.right, n + 1)
    4. todo_stack.append(node.left, n + 1)
    5. node = todo_stack.pop()

Notes:
- N is used to track the leve
- Because of the order that nodes are added to the tree, pop will always take the left most element.

### Complexity Analysis

#### Time complexity
O(N) - must traverse all nodes in the tree

#### Space complexity
O(2N) - two mutable lists that all nodes pass through. However, in practice, these lists will never consume more
space than O(N).

#### leetCode Diagnostics:
Runtime: 32 ms, faster than 92.82% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
]
 */
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class RecursiveSolution():
    """
    returns list of lists representing binary tree values using BFS recursive algorithm
    """
    def levelOrder(self, root: TreeNode) -> list:
        tree_vals = []
        if root == None: return tree_vals

        def get_level(root: TreeNode, n: int) -> list:
            """
            Recursive utility function:
            Returns values from each level of the treeNode. 
            """
            ## Generate Nth list
            try:
                 tree_vals[n]
            except IndexError:
                tree_vals.insert(n, [])
            
            ## Add root
            tree_vals[n].append(root.val)

            ## Add next lefts
            if root.left != None:
                get_level(root.left, n + 1)
            if root.right != None:
                get_level(root.right, n + 1)
        
        get_level(root, 0)
        return tree_vals

"""
The approach for IterativeSolution1 was fundamentally flawed. 
Please refer to: ## IterativeSolution1 --> ### Notes on challenges for discussion.
"""
# class IterativeSolution1():
#     """
#     returns list of lists representing binary tree values and levels using BFS iterative algorithm.
#     """
#     def levelOrder(self, root: TreeNode) -> list:
#         tree_vals, todo_stack, next_level = [], [root], []
#         n = 0
#         if root == None: return tree_vals

#         while todo_stack or next_level:
#             tree_vals.insert(n, [])

#             while todo_stack:
#                 node = todo_stack.pop()
#                 tree_vals[n].append(node.val)

#                 if node.right != None:
#                     next_level.append(node.right)
#                 if node.left != None:
#                     next_level.append(node.left)        

#             todo_stack, next_level = next_level, []
#             n+= 1

#         return tree_vals


class BfsSolution():
    """
    returns list of lists representing node values from levels of binary tree. 
    Uses a Bread First Search Iterative Algorithm.
    """
    def levelOrder(self, root: TreeNode) -> list:
        if root == None: return []
        
        tree_vals, todo_stack = [], [(root, 0)]

        while todo_stack:
            node, n = todo_stack.pop(0)

            if node:
                if len(tree_vals) < n + 1:
                    tree_vals.append([])
                
                tree_vals[n].append(node.val)
                todo_stack.append((node.left, n + 1))
                todo_stack.append((node.right, n + 1))
            
        return tree_vals


class DfsSolution():
    """
    returns list of lists 
    """
    def levelOrder(self, root: TreeNode) -> list:
        if root == None: return []

        tree_vals, todo_stack = [], [(root, 0)]

        while todo_stack:

            node, n = todo_stack.pop()
            
            if node: 
                if len(tree_vals) < n + 1: 
                    tree_vals.append([])

                tree_vals[n].append(node.val)
                todo_stack.append((node.right, n + 1))
                todo_stack.append((node.left, n + 1))
        
        return tree_vals


def test_solutions():
    """
    Runs unit tests for Binay tree level order traversal
    """
    # tester = RecursiveSolution()
    # tester = IterativeSolution1()
    # tester = BfsSolution()
    tester = DfsSolution()

    print('test 1')
    root = TreeNode(3, 
                TreeNode(9), 
                TreeNode(20,
                    TreeNode(15),
                    TreeNode(7)))
    output = [
        [3],
        [9, 20],
        [15, 7]
    ]
    assert tester.levelOrder(root) == output

    print('test 2')
    root = None
    output = []
    assert tester.levelOrder(root) == output

    print('test 3')
    root = TreeNode(1,
                TreeNode(2,
                    TreeNode(4)),
                TreeNode(3, 
                    None,
                    TreeNode(5)))
    output = [[1],
                [2,3],
                [4,5]
                ]
    assert tester.levelOrder(root) == output


def main():
    test_solutions()


if __name__ == '__main__':
    main()
