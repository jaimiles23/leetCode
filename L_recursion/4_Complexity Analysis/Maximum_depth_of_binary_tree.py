"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-25 22:56:28
 * @modify date 2019-11-25 23:16:20
 * @desc [
Solution to leetCode's [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)'

On initial inspection, I was a confused with the direction of the problem. It was recommended that people do the binary tree Explore card before 
studying recursion, and my struggle to create a solution suggests that I need more familiarity working with n-ary tree structures. 

I implemented [this](https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/139585/Explanations-in-Python) solution that
I found online. I did feel confident re-creating it and understanding the logic.
 ]
' */
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class foundSolution():
    """
    Re-creating solution I found online.
    Returns maximum tree depth from the structure.
    """
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def test_solution():
    """
    Runs unit tests to Maximum Depth of Binay Tree solution
    """
    tester = foundSolution()

    print('test 1')
    node_1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert tester.maxDepth(node_1) == 3 


def main():
    test_solution()


if __name__ == '__main__':
    main()