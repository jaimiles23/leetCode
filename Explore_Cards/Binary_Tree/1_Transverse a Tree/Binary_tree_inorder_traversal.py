"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-30 15:37:15
 * @modify date 2019-11-30 16:35:24
 * @desc [

# Binary Tree Inoder Traversal
Solution to leetCode's [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

Inorder traversal:
1. Left subtree
2. Node
3. Right subtree

This soluution uses two dynamic programming approach to traverse the tree in order:
1. Recursive
2. Iterative

## RecursiveSolution

### BaseCase:
root == None: return none

#### Recursive relation
f(root) = f(root.left) + f(root.val) + f(root.right)

### Complexity Analysis

#### Time complexity
O(T) = R * O(s) 
O(T) = O(N) * O(1)
= O(N)

#### Space complexity
Recursion related space + non-recursion related space
Recursion related space: stack space including return address, parameters, local variables
non-recursion related space: None

= Recursive related space = O(1) * R
= O(N)

### leetCode diagnostics:
Runtime: 28 ms, faster than 90.85% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.

## IterativeSolution
An iterative solution to transvering an n-ary tree uses two lists:
    1. todo_stack, to hold the nodes to return to. 
    2. results, the tree values to return.

The todo_stack will place nodes onto the stack in order to be used.
The .pop() method will be used to retrieve the last node, and as such, 
the node.left will always be added to the stack last.

### Complexity Analysis

#### Time complexity
O(N) - All list nodes are transversed

#### Space complexity
O(N) becasue in worst case, all list objects may be in the TODO_stack.

### leetCode Diagnostics:
Runtime: 28 ms, faster than 90.85% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
]
 */
"""
class TreeNode:
    def __init__(self, x: int, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class RecursiveSolution():
    """
    return list of inorder binary tree values using recursion
    """
    def inorderTraversal(self, root: TreeNode) -> list:
        node_vals = []
        if root:
            node_vals += self.inorderTraversal(root.left)
            node_vals.append(root.val)
            node_vals += self.inorderTraversal(root.right)

        return node_vals


class IterativeSolution():
    def inorderTraversal(self, root: TreeNode) -> list:
        """
        return list of inorder binary tree values using iteration. 
        """
        tree_vals = []              # inorder list of values 
        todo_stack = [root]         # stores nodes TODO

        while todo_stack:
            node = todo_stack.pop()

            if node:

                if node.left != None:
                    left, node.left =  node.left, None
                    todo_stack += [node, left]

                else:
                    tree_vals.append(node.val)
    
                    if node.right != None:
                        todo_stack.append(node.right)
                        
        return tree_vals


def test_solutions():
    """
    Runs unit tests for inorder tree traversal
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

    print('test 1')
    node = TreeNode(1,
                    None,
                    TreeNode(2,
                        TreeNode(3)))
    result = [1,3,2]
    assert tester.inorderTraversal(node) == result

    print('test 2')
    node = TreeNode(3, 
                TreeNode(1,
                    TreeNode(2)))
    result = [1, 3, 2]



[3,1,2]

def main():
    test_solutions()


if __name__ == '__main__':
    main()
