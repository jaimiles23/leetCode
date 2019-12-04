"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 12:21:25
 * @modify date 2019-12-04 13:04:00
 * @desc [
# Symmetric Tree
Contains solutions to leetCode's [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

I employ two DP approaches to this problem:
    1. Recursive
    2. Iterative

## RecursiveSolution()
The recursive algorithm compares the values of the left subtree to the values of the right subtree

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
O(1) - hold root value
= O(N) + O(1) 
= O(N)

### leetCode Diagnostics:
Runtime: 24 ms, faster than 99.35% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.

## IterativeSolution()
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


def unit_tests():
    """
    Runs unit tests for 101 Symmetric tree
    """
    tester = RecursiveSolution()

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