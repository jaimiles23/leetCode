"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-03 20:02:49
 * @modify date 2019-12-04 12:21:41
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
O(T) = R * O(s)
    = O(N) * O(1)
    = O(N)
    Because the recursion must cycle through all nodes.

##### Space complexity
= Recursive space + non-recursive space
Recursive space = recursive stack = Address, params, and local variables.
= O(N) * O(3) = O(N) * O(1) = O(N)

#### leetCode diagnostics
Runtime: 40 ms, faster than 89.84% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.9 MB, less than 90.62% of Python3 online submissions for Maximum Depth of Binary Tree.

### TopDownIterative
This solution uses a stack that contains 2 values:
- Node
- Depth value

If the node != None, 
    += 1 to depth 
    check the result for max depth
    Add node.left and node.right to the stack (order does not matter).

Note: This is a DFS (Depth first search) because pop() takes the last index. 
A Breadth First Search (BFS) would insert new values at index 0, and take new nodes from the end of the list.

#### Complexity analysis
##### Time complexity
O(N) - cycles through all nodes in the list

##### Space complexity

O(log(N)). This is because the iterative solution contains the answer O(1) and a list of nodes, O(N).  
However, this solution will never contain all nodes at once, and uses a DFS algorithm.

#### leetCode Diagnostics:
Runtime: 44 ms, faster than 76.49% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Maximum Depth of Binary Tree.

_Note_: Memory usage 1 MB difference in memory usage reflects space complexity.

## BottomUp
Bottom up solutions use answers from child nodes in order to solve the problem. Because these answers a binay tree
must access subtrees through the main node, a Bottom Up approach is of recursive nature. 

### Recursive relation
F(node, depth) = F(node.next, depth + 1)

### Base case
node == None: return 0 # indicates no depth

### Complexity Analysis
#### Time complexity
O(T) = R * O(s) 
    = O(N) * O(1)
    = O(N)
#### Space complexity
Recursion related space + non-recursion related space
= recursive stack (address, params, local vars) = O(N)

### leetCode diagnostics
Runtime: 36 ms, faster than 96.56% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15 MB, less than 90.62% of Python3 online submissions for Maximum Depth of Binary Tree.

_Note_: again, the space complexity is reflected in the 15 MB memory usage.
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
        def helper(node: TreeNode, depth: int, result: int) -> int:
            """
            utility recursive funciton
            """
            if node:
                depth += 1
                if depth > result:
                    result = depth                    
            
                result = helper(node.right, depth, result)
                result = helper(node.left, depth, result)

            return result

        return helper(root, 0, 0)


class TopDownIterative():
    def maxDepth(self, root: TreeNode) -> int:
        """
        returns max depth of a binary tree using an iterative top down recursion.
        """
        result = 0
        stack = [(root, result)]

        while stack:
            node, depth = stack.pop()

            if node:
                depth += 1
                result = max(result, depth)

                stack.append((node.right, depth))
                stack.append((node.left, depth))
        return result


class BottomUpRecursion():
    def maxDepth(self, root: TreeNode) -> int:
        """
        returns max depth of binay tree using bottomUp recursion
        """
        def helper(node, depth) -> int:
            """
            utility recursive function
            """
            if not node:
                return 0
            
            left = helper(node.left, depth) + 1
            right = helper(node.right, depth) + 1
            return max(left, right)

        return helper(root, 0)


def unit_tests():
    """
    Runs unit tests for Maximum Depth of Binary Tree
    """
    # tester = TopDownRecursion()
    # tester = TopDownIterative()
    tester = BottomUpRecursion()

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
