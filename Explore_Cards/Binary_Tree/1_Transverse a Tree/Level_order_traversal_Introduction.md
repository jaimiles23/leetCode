# Level-order Traversal - Introduction

*Level order traversal* traverses a tree level by level, and is considered a type of **Breadth First Algorithm** (BFD). 
A **BFD** algorithm is used in data structures like trees or graphs. The algorithm starts with the root node, and visits the node itself. Then, the algorithm will traverse its neighbors, then traverse its second level neighbors, then traverse its third level neighbors, and so on. 

When we do a breadth first search in a tree, the order of the node we visit is in level order. 

Example:
                F
            /       \
            B       G
        /       \       \
        A       D       I
            /       \   /
            C       E   H

Using a BFS algorithm to collect values of each level, the result would be:
```
result = 
[
    [F]
    [B, G]
    [A, D, I]
    [C, E, H]
]
```


        