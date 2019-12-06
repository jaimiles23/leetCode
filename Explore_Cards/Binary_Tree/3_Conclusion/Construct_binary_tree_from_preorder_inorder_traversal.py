"""/**

 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-06 12:05:44
 * @modify date 2019-12-06 12:05:44
 * @desc [
Contains solutions to leetCode's [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

# Construct binary tree from preorder and inorder traversal

As seen in the solutions to construct binay tree from postorder and inorder traversal, this solution can perhaps
best be visualized recursively. Thus, I implement a recursive solution to this problem. 
_Note_: I believe that the best solution will be an iterative hash (dictionary)

## RecursiveSolution

 ]
 */
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right




def unit_tests():
    """
    runs unit tests for algorithm
    """
    tester = None

    print('test 1')
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    output = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20,
                        TreeNode(15),
                        TreeNode(7))
    )
    assert tester.buildTree(preorder, inorder) == output


def main():
    unit_tests()


if __name__ == '__main__':
    main()