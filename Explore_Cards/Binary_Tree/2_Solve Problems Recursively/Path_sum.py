"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 16:52:40
 * @modify date 2019-12-04 16:52:40
 * @desc [
Contains solutions to leetCode's [112. Path Sum](https://leetcode.com/problems/path-sum/)

# Path Sum

Two fundamentally different DP solutions:
    1. Recursive
    2. Iterative



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
        pass
    



def unit_tests():
    """
    Runs unit tests to check for path sum
    """
    tester = None

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


def main():
    unit_tests()


if __name__ == '__main__':
    main()
