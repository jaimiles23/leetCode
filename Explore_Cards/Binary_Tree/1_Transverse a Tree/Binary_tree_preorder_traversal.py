"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-30 11:49:18
 * @modify date 2019-11-30 15:23:54
 * @desc [
Contains recursive and iterative solutions to [Binary Tree Preorder Transversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

Preorder Transversal:
1. Node
1. left subtree
1. right subtree

## Recursive solution
Start with empty list, tree_vals. Append node.val to tree_vals, then move to left subtree, and finally right subtree.

### Base case
if node == None: return tree_vals

### Recursive relation
F(tree, tree_vals) = F(tree - node, tree_vals + val)

### Complexity analysis

#### Time compelxity
O(T) = R * O(s)
O(T) = O(N) * O(1)
O(T) = O(N) 

#### Space complexity
= Recursion related space + non_recursion space
= O(N) + O(1)
= O(N)
Do note: O(N) space is kept for two steps. Once the node.left recursion is closed, 
the node.right recursion is opened. Thus, though O(N) is the maximum occurence, memory allocation will not 
transverse from N, to N-1, but from N, to N, to N-1, to N-1 ...

### leetCode Diagnostics
Runtime: 20 ms, faster than 99.30% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.

## Recursive Solution 2
Slight variations to original RecursiveSolution:
    1. Removed passing tree_node parameter
    2. Removed helper recursive function
    3. Used list + operator to combine steps
    4. Changed logic for basecase

### Complexity Analysis

#### Time complexity
O(T) = R * O(s)
     = O(N) * O(1)
     = O(N)

#### Space complexity
= Recursive space + non-Recursive related space
= O(N) + O(1)
= O(N)

### leetCode Diagnostics:
Runtime: 28 ms, faster than 90.33% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.

## Iterative Solution
The iterative solution requires two lists:
    1. Nodes TODO: a stack
    2. Nodes recorded: the results - Note: this can also substitute as a 'seen nodes' list 
    in cyclic data structures.

Instantiate the TODO stack with the root node. Then:
    1. Pop the node from the stack.
    2. Add node.val to the results
    3. Add node.right to todo_stack
    4. Add node.left to todo_stack
    5. Repeat until todo_stack is empty

Note: add .right before .left because pop takes far right item from the list.

### Complexity Analysis

#### Time complexity
O(T) = O(N)

#### Space complexity
O(N) - amortized space complexity, all listnodes may be held in the todo_stack.

### leetCode Diagnostics:
Runtime: 28 ms, faster than 90.33% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.

Note: The memory usage is comparable, but smaller on average across runs.
 ]
 */
"""

class TreeNode:
    def __init__(self, x: int, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class RecursiveSolution():
    def preorderTraversal(self, root: TreeNode) -> list:
        """
        Returns list of tree's values using recursion.
        """
        tree_nodes = []

        def recursion_helper(root: TreeNode, tree_nodes: list) -> list:
            if root == None:
                return tree_nodes

            tree_nodes.append(root.val)

            tree_nodes = recursion_helper(root.left, tree_nodes)
            tree_nodes = recursion_helper(root.right, tree_nodes)
            return tree_nodes
        
        return recursion_helper(root, tree_nodes)


class RecursiveSolution2():
    """
    Slight variations to original RecursiveSolution:
        1. Removed passing tree_node parameter
        2. Removed helper recursive function
        3. Used list + operator to combine steps
        4. Changed logic for basecase
    """
    def preorderTraversal(self, root: TreeNode) -> list:
        tree_nodes = []
        if root:
            tree_nodes.append(root.val)

            return tree_nodes + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        return tree_nodes


class IterativeSolution():
    def preorderTraversal(self, root: TreeNode) -> list:
        tree_nodes = [] # Nodes recorded
        todo_stack = [root]  # Nodes TODO

        while todo_stack:
            node = todo_stack.pop()
            if node: 
                tree_nodes.append(node.val)
                todo_stack.append(node.right)
                todo_stack.append(node.left)
        
        return tree_nodes
        

def test_solutions():
    # tester = RecursiveSolution()
    # tester = RecursiveSolution2()
    tester = IterativeSolution()

    print('test 1')
    tree = TreeNode(1, 
                    None, 
                    TreeNode(2, 
                        TreeNode(3)))
    output = [1,2,3]
    assert tester.preorderTraversal(tree) == output

    
def main():
    test_solutions()


if __name__ == '__main__':
    main()

