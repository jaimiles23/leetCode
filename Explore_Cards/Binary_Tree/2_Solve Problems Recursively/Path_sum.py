"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 16:52:40
 * @modify date 2019-12-04 17:25:54
 * @desc [
Contains solutions to leetCode's [112. Path Sum](https://leetcode.com/problems/path-sum/)

# Path Sum

Two fundamentally different DP solutions:
    1. Recursive
    2. Iterative

## RecursiveSolution()
Applies a TopDown Depth First Search algorithm that checks sub-branches so long as running sum < desired total.

### Recursive relation
F(node, sum) = F(node.next, sum + node.val)
_note_ will need to check both node.left nad node.right for each relation

### Base case
if not node: return 0

### Complexity analysis

#### Time analysis

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
    Returns boolean indicating if binary tree has path equating to summation
    """
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if not root:
            if total == None: 
                return True
            return False
        
        def checkSum(node: TreeNode, running: int) -> bool:
            if node:
            
                running += node.val
                if running > total:
                    return False

                elif running == total:
                    if node.left == None and node.right == None:
                        return True

                else:
                    left = checkSum(node.left, running)
                    right = checkSum(node.right, running)
                    if left or right:
                        return True 
            return False
        
        return checkSum(root, 0)


def unit_tests():
    """
    Runs unit tests to check for path sum
    """
    tester = RecursiveSolution()

    print('test 1')
    node = TreeNode(5,
                TreeNode(4,
                    TreeNode(11,
                        TreeNode(7),
                        TreeNode(2))),
                TreeNode(8,
                    TreeNode(13),
                    TreeNode(4,
                        None,
                        TreeNode(1)))
    )
    total, output = 22, True 
    assert tester.hasPathSum(node, total) == output

    print('test 2')
    node = TreeNode(1,
                TreeNode(2))
    total, output = 1, False
    assert tester.hasPathSum(node, total) == output

    print('test 3')
    node = TreeNode(-2,
                None,
                TreeNode(-3))
    total, output = -5, True
    assert tester.hasPathSum(node, total) == output



def main():
    unit_tests()


if __name__ == '__main__':
    main()
