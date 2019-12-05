"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 12:21:25
 * @modify date 2019-12-04 16:51:04
 * @desc [
# Symmetric Tree
Contains solutions to leetCode's [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

I employ two DP approaches to this problem:
    1. Recursive
    2. Iterative

## RecursiveSolution()
The recursive algorithm compares the values of the left subtree to the values of the right subtree.
Note: This is a DFS, because it will traverse one side of the tree first before comparing across a level.

### Recursive relation
F(node1, node2) =  
    if:
        node1.left == node2.right
        node1.right == node1.left
            return True
    
### Base case
if not node: 
    return None

### Complexity analysis
#### Time complexity
O(T) = R * O(S)
    = O(N) * O(1)
    = O(N)

#### Space complexity
= Recursive related space + non-Recursive related space

Recursive related space = Recursive stack * Recursive calls
    = (address, params, local vars) * Recursive calls
        = O(1) * O(N)

non Recursive related space:
O(1) to hold root node
= O(N) + O(1) 
= O(N)

### leetCode Diagnostics:+
Runtime: 24 ms, faster than 99.35% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.

## IterativeSolution()
The iterative algorithm uses a stack to contain the different nodes of the binary tree. 
_Note_ This will be a Breadth First Search algorithm because it will check one level at a time.

The stack of treeNodes is traversed until either: 
    - all nodes have been checked
    - two corresponding nodes are the tree are not symmetric, incase false is returned.

### Complexity Analysis
#### Time complexity
O(N) - must cycle through all nodes in the binary tree

#### Space complexity
O(log(N)) - node1 and node2 are O(1) space, while the stack is BFS
level order traversal, which only only ever contain 2 levels of the binary tree maximum.

### leetCode diagnostics
Runtime: 24 ms, faster than 99.35% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
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
    def isSymmetric(self, root) -> bool:
        """
        returns boolean val indicating symmetry using a recursive top down algorithm.
        """

        def check_sym(node1: TreeNode, node2: TreeNode) -> bool:
            """
            Recursive check of outside and inside symmetry.
            """
            if node1 and node2:

                if node1.val != node2.val:
                    return False

                outside_sym = check_sym(node1.left, node2.right)
                inside_sym = check_sym(node1.right, node2.left)
                return outside_sym and inside_sym

            elif not node1 and not node2:
                return True

            else:
                return False
        
        if not root:
            return True

        return check_sym(root.left, root.right)


class IterativeSolution():
    def isSymmetric(self, root) -> bool:
        """
        Returns boolean indicating symmetry for binary tree using iterative, BFS algorithm
        """
        if not root: 
            return True

        stack = [root.left, root.right]

        while stack:
            node1, node2 = stack.pop(0), stack.pop(0)
            if node1 and node2:

                if node1.val != node2.val:
                    return False
                stack += [node1.left, node2.right]
                stack += [node1.right, node2.left]

            elif not node1 and not node2:
                continue

            else:
                return False
        
        return True


def unit_tests():
    """
    Runs unit tests for 101 Symmetric tree
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

    print('test 1')
    node = TreeNode(1, 
                TreeNode(2, 
                    TreeNode(3),
                    TreeNode(4)),
                TreeNode(2,
                    TreeNode(4),
                    TreeNode(3))
                    )
    output = True
    assert tester.isSymmetric(node) == output

    print('test 2')
    node = TreeNode(1,
                TreeNode(2, 
                    None,
                    TreeNode(3)),
                TreeNode(2,
                    None,
                    TreeNode(3))
                    )
    output = False
    assert tester.isSymmetric(node) == output


def main():
    unit_tests()


if __name__ == "__main__":
    main()