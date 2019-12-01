"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-30 22:58:29
 * @modify date 2019-11-30 23:23:55
 * @desc [
Solution to leetCode's [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

# Postorder Traversal
Post order traversal of a binary tree is as follows:
1. Left subtree
2. Right subtree
3. RootNode

In order to traverse the left and right subtrees, you can use two dynamic programming approaches:
1. Recursion
2. Iteration

Note: both of these are depth-first searches (DFS), because they travel to the end of the tree before
backtracking.

## Recursion
The recursive solution can use a single recursive function to return a list of the node values

### BaseCase
node.left == None: return None
node.right == None: return None     #root node is last, or postorder

### Recursive relation
F(node) = f(node.left) + f(node.right) + node.val

### Complexity Analysis

#### Time complexity
O(T) = R * O(s)
O(T) = O(N) * O(1)
O(N), because the recursive function is called for each node.

#### Space complexity
O(N), because each recursion overhead is added to the stack. Note: recursion overhead includes
3 variables: address, parameters, and local variables, which have O(1) space complexity.

### leetCode diagnostics
Runtime: 24 ms, faster than 96.38% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.

## IterativeSolution
To postOrder traverse a binary list using iteration, you need two lists:
1. todo_stack: list of nodes that have not yet been added to the value list
2. tree_vals: list of results

### Steps:
Instantiate two lists, and add rootNode to todo_stack.
    1. Repeat until todo_stack is empty
    2. node = todo_stack.pop()
    3a If node.left == None and node.right == None:
        tree_vals.append(node.val)
    3b else:
        todo_stack += [node, node.right, node.left]
    4. node = todo_stack.pop()
    

#### Notes on each step
    1. Will continue through all nodes
    2. Take the last node from the stack - because pop() takes the last element, order adding to the list is important
    3a. If the node has no children, or its children have already been accessed, add value to results
    3b. If the node has children, add all nodes back to the stack. 
        - Set the root pointers to None. Otherwise there will be an infinite loop
        - Order is important here, it must go: root -> right -> left
        - APpend

### Complexity Analysis

#### Time complexity
O(N) - must read each value in the binary tree

#### Space complexity
O(N) - the stack may technically hold all nodes in some binary trees

### leetCode Diagnostics
Runtime: 20 ms, faster than 99.19% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.
 
### Notes: 
I posted the iterative solution [here](https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/441602/Python-Iterative-explained)
 ]
 */
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class RecursiveSolution:
    def postorderTraversal(self, root: TreeNode) -> list:
        node_vals = []
        
        if not root: 
            return node_vals

        node_vals += self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return node_vals


class IterativeSolution():
    def postorderTraversal(self, root: TreeNode) -> list:
        tree_vals, todo_stack = [], [root]

        while todo_stack:
            node = todo_stack.pop()

            if node.left == None and node.right == None:
                tree_vals.append(node.val)
            else:
                left, right, node.left, node.right = node.left, node.right, None, None
                todo_stack += [x for x in [node, right, left] if x != None]
        
        return tree_vals


def test_solutions():
    """
    Run unit tests for binary tree postOrder traversal
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

    print('test 1')
    node = TreeNode(1, 
                None,
                TreeNode(2, 
                    TreeNode(3)))
    output = [3, 2, 1]
    assert tester.postorderTraversal(node) == output


def main():
    test_solutions()


if __name__ == '__main__':
    main()
