"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 18:53:53
 * @modify date 2019-12-05 14:24:43
 * @desc [
Contains solutions to leetCode's [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/_)

# Construct Binary Tree from Inorder and Postorder Traversal
I was unfamiliar with constructing binary trees from inorder and post order traversal. To solve this problem I
wrote out test cases on a piece of paper and assigned each index a representation of where it was on the tree. 
From this assignment, I derived the following patterns:
1. postOrder[-1] = root
2. postOrder[-2] = root.right
3. inOrder[inOrder.index(root) - 1] == root.left

I believe that we can follow this same pattern to re-create the tree. For each node:
    - node.right = postOrder[node - 1]
    - node.left = inOrder[inOrder.index(node) - 1]

To implement these two principles, I will use an iterative algorithm. The algorithm will modify the
inOrder and postOrder lists to be tuples of two values (node, visited). The visited variable will be a 
binary indicator if the node has been used. If the node adjacent to a visited node is used, then that node 
will be considered a leaf (ending) on that adjacent side.
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