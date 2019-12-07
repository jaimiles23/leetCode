"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-12-06 15:52:03
 * @modify date 2019-12-06 17:18:02
 * @desc [
Solution to [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

## userSolution
User solution uses two lists:
    1. todo_stack which is used to add all nodes to list 2
    2. all_nodes, which contains all nodes.

After all nodes have been added to the list, set all nodes.next pointer to the subsequent nodes. However,
the binary tree nodes per level equation (2 ^ level - 1) will be used to determine which nodes.next == None

### leetCode diagnostics:
Runtime: 72 ms, faster than 39.44% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.

_Note_: math solution used much less memory than other solution (1 MB), while ~ 20 ms slower than fastest solution.
 ]
 */
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class UserSolution():
    def connect(self, root: Node) -> Node:
        if not root: return None

        import math
        
        to_visit, nodes = [root], []

        while to_visit:
            node = to_visit.pop(0)
            if node:
                nodes.append(node)
                to_visit.append(node.left, node.right)
        
        no_nexts = []
        for i in range(1, int(math.log(len(nodes) + 1) / math.log(2)) + 1):
            no_nexts.append(2 ** i - 1)
        level_end = 0
        
        for i in range(0, len(nodes) - 1):
            
            if i == no_nexts[level_end] - 1:
                nodes[i].next = None
                level_end += 1

            else:
                nodes[i].next = nodes[i + 1]
                
        return nodes[0]


class RecursiveSolution():
    """
    Taken from [here](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/439349/Simple-Python-solution-beats-100)
    """
    def connect(self, root):
        def helper(root, rightroot):
            if root == None:        # base case
                return None
            helper(root.left, root.right)   # bottom-up recursive call

            if rightroot:
                root.next = rightroot
                helper(root.right, rightroot.left)      # fix nodes
            else:
                helper(root.right, None)        # set all subtree right nodes to none initially

        helper(root, None)
        return root
        
"""
This is a bottom up algorithm that assigns the .next address to different roots - you can tell this because
the first line is a recursion.

It will set each subtrees.right node to None, before moving up and checking the larger subtree. It will then assign
the root.next to the right node outside of the subtree with: helper(root.right, rightroot.left)
"""