"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-03 20:02:49
 * @modify date 2019-12-03 20:02:49
 * @desc [
# Maximum Depth of Binary Tree
Solutions to leetCode's [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

There are two dynamic programming approaches to this problem:
1. Top-down
2. Bottom-up

Both of these solutions are implemented recursively and iteratively.

## Top-down 
Top down recursion works by gathering information from the current node before moving onto child nodes. 
This solution starts with a global variable, depth, and modifies it if the recursive relation is greater than 
the recorded depth.

### TopDownRecursion

#### Recursive relation
F(N, depth) = max(F(n.left, depth + 1), F(n.right, depth + 1))

#### Base case
N == None: return 0

#### Complexity Analysis
##### Time complexity

##### Space complexity


 ]
 */
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class TopDownRecursion():
    def maxDepth(self, root: TreeNode) -> int:
        """
        returns maximum depth of a binary tree using a recusive top-down algorithm
        """
        result = 0

        def helper(node: TreeNode, depth: int) -> int:
            """
            utility recursive funciton
            """
            if node:
                if depth > result:
                    result = depth
            
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
        
        
        if root == None: return 0
        helper(root, 1)
        return result


def unit_tests():
    """
    Runs unit tests for Maximum Depth of Binary Tree
    """
    tester = TopDownRecursion()

    print('test 1')
    node = TreeNode(3,
                TreeNode(9, 
                    None,
                    None),
                TreeNode(20,
                    TreeNode(15),
                    TreeNode(7)))
    output = 3
    assert tester.maxDepth(node) == output


def main():
    unit_tests()


if __name__ == "__main__":
    main()

print('1')