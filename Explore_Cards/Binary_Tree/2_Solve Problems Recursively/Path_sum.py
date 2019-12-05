"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-04 16:52:40
 * @modify date 2019-12-04 18:50:26
 * @desc [
Contains solutions to leetCode's [112. Path Sum](https://leetcode.com/problems/path-sum/)

# Path Sum

Two fundamentally different DP solutions:
    1. Recursive
    2. Iterative

## RecursiveSolution()
Applies a TopDown, DFS algorithm that checks sub-branches for sum.

### Recursive relation
F(node, sum) = F(node.next, sum + node.val)
_note_ will need to check both node.left nad node.right for each recursive relation

### Base case
if not node: return 0

### Complexity analysis
#### Time complexity
O(T) = R * O(s)
    = O(N) * O(1)
    = O(N)
#### Space complexity
Note: If all nodes are contained in a single branch, recursive stack may contain all nodes. 

Space = Recursion related space + non-Recursion related space
        Recursion related space = Recursive stack (address, params, local vars) * R
                                = O(1) * R
                                = O(N)
        +
        non-Recursion related space = 0
    = O(N)

### leetCode Diagnostics
Runtime: 36 ms, faster than 98.19% of Python3 online submissions for Path Sum.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Path Sum.

## IterativeSolution()
A BFS algorithm that checks for a root-leaf path that is equivalent to the total parameter.

As common with iterative solutions to binary tree problems, this solution uses a stack to hold tree nodes.

### Steps
while stack:
    node, running = stack.pop()
        if node:
            1. if node.val == sum and .next == None: return true
            2. stack += [(node.next, sum - node.val)]   # add next nodes to end of stack, with tracked sum

Note: BFS will never have more than 2 levels at a time because items are added to the end.

### Complexity analysis
#### Time complexity
Worst case, will check all nodes in the tree

#### Space complexity
O(log(n)). The stack [] contains nodes, however because it traverses the tree in level order, it will 
never have more than 2 levels of the tree inside thes tack. Thus, O(log(n)).

### leetCode Diagnostics
Runtime: 40 ms, faster than 93.89% of Python3 online submissions for Path Sum.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Path Sum.
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

        if root:
            total -= root.val

            if total == 0:
                if root.left is root.right is None:
                    return True

            left = self.hasPathSum(root.left, total)
            right = self.hasPathSum(root.right, total)
            if left or right:
                return True

        return False

class IterativeSolution():
    """
    Returns boolean if binary tree has terminating path equating total
    """
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        stack = [(root, total)]

        while stack:
            node, total = stack.pop(0)

            if node:
                total -= node.val

                if total == 0:
                    if node.left == None and node.right == None:
                        return True
                
                stack += [(node.left, total), (node.right, total)]
        
        return False


def unit_tests():
    """
    Runs unit tests to check for path sum
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

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

    print('test 4')
    node = TreeNode(1,
                TreeNode(-2,
                    TreeNode(1,
                        TreeNode(-1)),
                    TreeNode(3)),
                TreeNode(-3,
                    TreeNode(-2))
    )
    total, output = -1, True
    assert tester.hasPathSum(node, total) == output


def main():
    unit_tests()


if __name__ == '__main__':
    main()
