"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 18:53:53
 * @modify date 2019-12-06 11:39:23
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

_**NOTE**_
User developed algorithm incorrect. Use testcase 4
inorder: [2, 3, 1]
postorder: [3, 2, 1]
        1
    /
    2
        \
        30
However, user algorithm incorrectly assigned both variables. Must account that right subtree will be slide of
inorder[root:].

Instead, did secondary research and read solutions posted here:
- [GeeksforGeeks1](https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/)
- [GeeksforGeeks2](https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/)
- [programCreek](https://www.programcreek.com/2013/01/construct-binary-tree-from-inorder-and-postorder-traversal/)
- [Hui Lin blog post](https://medium.com/@huilin1618/constructing-binary-tree-from-inorder-and-postorder-traversal-3f92c4183d65)

## NaiveRecursiveSolution():
Naive recursive solution assigns the root using the last index of postorder. 
    - find left and right node with recursive solution
        - left recursion: pass inorder list that is left of previous node, pass slice of postorder list that is 
        same length as inorder list
        - right_recursion: pass inorder list to right of previous node, pass sliced post order list of same
        length as passed inorder list.

### Complexity analysis
#### Time complexity
O(T) = R * O(s)
    = O(N) * O(s)
    O(s) = .index() and list slicing for (left_io, left_po, right_io, and right_po) = O(N)
        = O(N) + O(N)
        = O(2N)
    = O(N) * O(2N) = O(2N**2)
    = O(N**2)

#### Space complexity
recursive related space + non_recursive related space O(1)
recursive related space = address, params, local vars (list slicing is O(N)). 
                        = O(N) * O(N)
                        = O(N**2)

leetCode Diagnostics:
Runtime: 196 ms, faster than 30.00% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 86.8 MB, less than 55.56% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

## nonSlicingRecursiveSolution
This solution employs the same ideas expressed in the above example and uses integers 
to track where to search the inorder (IO) list, instead of list slicing. This is more memory efficient, because
it does not slice the list and keep track of the sliced list in each recursion.

### leetCode Diagnostics:
Runtime: 284 ms, faster than 11.10% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

_Note_  This solution uses ~ 1/5 the memory usage of the naive solution, however runs even slower. Two reasons 
I can think of for this:
1. Overhead associated with calling the search function
2. time lag accessing the self.po_index variable - I am not very knowledgeable about this method.

]
 */
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

"""
User developed algorithm incorrect, reference above.
"""
# class incorrectUserSolution():
#     def buildTree(self, inorder: list, postorder: list) -> TreeNode:
#         """
#         Returns treenode from inorder and postorder lists uses inductively derived principles noted above
#         """
#         if inorder == []: return None
    
#         root = TreeNode(postorder[-1])
#         node, stack = root, [root]

#         while stack:
#             print('**')
#             node = stack.pop()
#             print('node:', node.val)

#             # left node
#             inorder_index = inorder.index(node.val)     
#             inorder[inorder_index] = None
            
#             left = inorder[inorder_index - 1] if (inorder_index - 1 >= 0) else None
#             print('left', left)

#             if left:             
#                 left = TreeNode(left)
#             node.left = left

#             # right node
#             postorder_index = postorder.index(node.val)
#             postorder[postorder_index] = None

#             right = postorder[postorder_index - 1] if (postorder_index - 1 >= 0) else None
#             if right and left: right = right if right != left.val else None
#             print('right', right)

#             if right:
#                 right = TreeNode(right)
#             node.right = right

#             if right:
#                 stack.append(right)
#             if left: 
#                 stack.append(left)

#         return root


class naiveRecursiveSolution():
    """
    Recreation of O(N ** 2) solution from GeekforGeeks
    """
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        # Base case
        if inorder == []:
            return None

        # Assign node
        node_val = postorder[-1]
        node = TreeNode(node_val)
        io_index = inorder.index(node_val)

        # left node
        if io_index == 0:   # Nothing to the left
            node.left == None
        else:
            io_left = inorder[:io_index]
            po_left = postorder[: len(io_left)]
            node.left = self.buildTree(io_left, po_left)
        
        # right node
        if io_index == len(inorder) - 1:    # nothing to right
            node.right == None
        else:
            io_right = inorder[io_index + 1: ]
            po_right = postorder[len(inorder[:io_index]): len(postorder) - 1]
            node.right = self.buildTree(io_right, po_right)

        return node


class nonSlicingRecursiveSolution():
    """
    This solution uses integers to search the appropriate indices instead of slicing the list. This is more
    memory efficient than the naiveRecursiveSolution above because we are storing ints, not lists: O(1) v O(N)
    """

    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        """
        Constructs binary tree from inorder and postorder traversal lists. 
        """
        self.po_index = len(inorder) - 1
        def create_node(inorder: list, postorder: list, io_start: int, io_end: int) -> TreeNode:
            """
            Returns treenode for tree
            """
            if io_start > io_end: 
                return None
            
            node = TreeNode(postorder[self.po_index])
            # print('node', node.val)
            self.po_index -= 1

            io_index = search(inorder, node.val, io_start, io_end)

            node.right = create_node(inorder, postorder, io_index + 1, io_end)
            node.left = create_node(inorder, postorder, io_start, io_index - 1)
            
            return node


        def search(inorder: list, val: int, io_start: int, io_end: int) -> int:
            """
            Searches inorder list from index[start] to index[end] to return index of value.
            More efficient search algorithm because we know range where index is in.
            """
            for i in range(io_start, io_end + 1):
                if (inorder[i] == val):
                    return i
        
        io_start, io_end = 0, len(inorder) - 1 
        return create_node(inorder, postorder, io_start, io_end)


def unit_tests():
    # tester = incorrectUserSolution()
    # tester = naiveRecursiveSolution()
    tester = nonSlicingRecursiveSolution()

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

    print('test 2')
    inorder = [2, 1]
    postorder = [2, 1]
    output = TreeNode(1,
                TreeNode(2))
    assert tester.buildTree(inorder, postorder) == output

    print('test 3')
    inorder = [1, 2]
    postorder = [2, 1]

    output = TreeNode(1,
                None,
                TreeNode(2))
    assert tester.buildTree(inorder, postorder) == output

    print('test 4')
    inorder = [2, 3, 1]
    postorder = [3, 2, 1]

    output = TreeNode(1,
                None,
                TreeNode(2))
    assert tester.buildTree(inorder, postorder) == output


def main():
    unit_tests()


if __name__ == '__main__':
    main()