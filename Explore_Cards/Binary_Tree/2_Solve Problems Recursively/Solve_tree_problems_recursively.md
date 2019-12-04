# Solve Tree Problems Recursively
```
'Top-down' solution
'Bottom-up' solution
Conclusion
```
Recursion is one of the most frequently used techniques for solving tree problems.

A tree can be defined recursively as a node (root) that includes a value and a list of references to child nodes. Recursion is a natural freature of a tree, so many tree problems can be solved recursively. Each recursive function focuses on the current node, and calls the function recursively for each children. Typically solve a tree problem using either a top-down approach or a bottom-up approach.

## "Top-down" Solution
Start with the node first to come up with some values, adn then pass these values to its children when calling the function recursively. As such, a top-down approach can be considered a type of _preorder_ traversal. 

A top_down recursive function may have the following steps
1. Return specific value for null node
2. Update the answer if needed
3. left_ans = top_down(root.left, left_params)
4. right_ans = top_down(root.right, right_params)
5. return answer

Given a binary tree, find its maximum depth:

We know that the depth of the root node is `1`. If we pass a local variable, depth, and update it with each child-node, we can determine the maxmimum depth.  Here is pseudocode for the recursive function maximum_depth(root: TreeNode, depth: int):

1. return if root == null
2. if root:
   1. answer = max(answer, depth)
3. maximum_depth(root.left, depth + 1)
4. maximum_depth(root.left, depth + 1)

# "Bottom-up" Solution
Call the function recursively for all children nodes, and then determine the answer according to the returned values. This is a type of _postorder_ traversal. 

A bottom-up recursion may have the following steps:
1. Return specific value for null node
2. left_ans = bottom_up(root.left)
3. right_ans = bottom_up(root.right)
4. return ans

A bottom-up approach to the maximum tree depth question would observe the maximum depth of each subtree. If we know the maximum depth of each subtree, we can add `1` to get the current maximum depth. Thus,
`x = max(l, r) + 1`

Thus, we can get the answer for each node after solving the problem for its children. Here is the bottom_up pseudocode for the maximum_depth question
1. return 0 if not root
2. left_depth = maximum(depth.left) 
3. right_depth = maximum_depth(root.right)
4. return max(left_depth, right_depth) + 1

## Conclusion
When facing a tree problem, ask two questions:
1. Can you determine some parameters to help the node know its answers?
2. Can you use these parameters to pass parameters to its children?
If the answer to both is yes, use a `top-down` recursive solution.
_or_
1. If you know the answer of its children, can you calculate the answer of the node?
2. If the answer is yes, use a `bottom up` recursion.



