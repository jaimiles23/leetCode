"""/**

 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-06 12:05:44
 * @modify date 2019-12-06 13:35:55
 * @desc [
Contains solutions to leetCode's [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

# Construct binary tree from preorder and inorder traversal

As seen in the solutions to construct binay tree from postorder and inorder traversal, this solution can perhaps
best be visualized recursively. Thus, I implement a recursive solution to this problem. 
_Note_: I believe that the best solution will be an iterative hash (dictionary)

## RecursiveSolution
The recursive solution utilizes the preorder traversal. preorder[0] = root of the tree/subtree. 
First, take this root and locate its index in the inorder traversal. Then, elements to the left of that index
compose the left subtree, elements to the right compose the right subtree. 
Note: travel left node -> right node because inorder traversal lists: root -> left -> right.

### Base case
len(inorder) == 0: return None (indicating no other elements)

### Recursive relation
f(node, inorder, postorder) = f(node.next, preorder[x:y], inorder[x:y])

### Complexity analysis
#### Time complexity
O(T) = R * O(s)
    = O(N) * O(s)
        = O(N) * O(N)
        = O(N** 2)

#### Space complexity
Recursive space + non_recursive space (O(1))
= O(N) * (address + parameters + local vars) - note: param of listslice is O(N)
    = O(N) * O(N)
        = O(N**2)

### leetCode diagnostics:
Runtime: 136 ms, faster than 62.47% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 51.1 MB, less than 71.05% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

## 
 ]
 */
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class naiveRecursion():
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(inorder) == 0: 
            return None
        
        node = TreeNode(preorder.pop(0))
        n_index = inorder.index(node.val)

        node.left = self.buildTree(preorder, inorder[:n_index])
        node.right = self.buildTree(preorder, inorder[n_index + 1:])
        return node
        

def unit_tests():
    """
    runs unit tests for algorithm
    """
    tester = naiveRecursion()
 
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