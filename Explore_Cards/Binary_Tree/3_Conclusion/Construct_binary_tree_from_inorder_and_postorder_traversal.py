"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 18:53:53
 * @modify date 2019-12-04 18:54:00
 * @desc [
Contains solutions to leetCode's [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/_)

# Construct Binary Tree from Inorder and Postorder Traversal



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
    tester = None

    print('test 1')
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    output = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                    TreeNode(15),
                    TreeNode(7))
    )
    assert tester.buildTree(inorder, postorder) == output


def main():
    unit_tests()


if __name__ == '__main__':
    main()