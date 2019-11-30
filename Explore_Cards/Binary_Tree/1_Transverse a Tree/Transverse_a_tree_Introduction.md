# Transverse a tree
Notes from this section are available from [here](https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/)

This card focuses on transversal methods used in binary trees. Understanding these methods provides insight into the tree structure, and provide a further foundation for future study. This chapter covers:
1. Different transversal methods
2. Solving preorder, inorder, and postorder transveral recursively
3. Solving preorder, inorder, and postorder transversal iteratively
4. Solving _level transveral_ using _BFS_

## Preorder Transversal
1. Visits the root of the tree
2. Transverses the left subtree
3. Transverses the right subtree

## Inorder Transveral
1. Transverses the left subtree
2. Visits the root of the tree
3. Transverses the right subtree

Typically in a _binary search tree_, we can retrieve all data in sorted order using in-order transversal. This will be covered in [Introduction to Data Structure - Binary Search Tree](https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/)

## Post-order Transversal
1. Transverses the left subtree 
2. Transverses the right subtree
3. Visits the root

_Note_: deleting nodes in a tree is **post-order**; you must delete the left and right child nodes before deleting a root node. Post-order is used widely in mathematical expressions, as it is easier to parse a post-order expression. A tree with numbers and operations is read inorder, however a program must check for the order of operations. Thus, the program will read it post order. Then, whenever the program reaches an operation, it pops the last 2 elements from the stack. Graphic available in [postorder transversal](https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/992/)

# Recursive or Iterative
Practice the 3 transversal methods iteratively and recursively in the following exercises.

