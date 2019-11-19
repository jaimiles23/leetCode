# Recursion Function
Given a problem defined by F(x), where x is the input and defines the scope of the problem.  Ti implement a recursive solution following these guidelines.

1. Break the problem into smaller scopes
   1. X0: X, X1: X, X2: X ... Xn: X
2. Call the function recusrively to solve the subproblems
   1. Call F(X0), F(X1), F(Xn)
3. Process the results from the recursive function calls to solve the problem
   
## Example
Given a linked list, swap every two adjacent nodes and return its head.

e.g., for a list, 1 -> 2 -> 3 -> 4, one should return the head of the list as 2 -> 1 -> 4 -> 3

The function to implement is swap(head), wehre head refers to the head of a linked list. The function should return the head of the new linked list that has any two adjacent nodes swapped.

Following the guidelines above:
1. Swap the two nodes in the list, head and head.next
2. Call the function recurseively as swap (head.next.next) to swap the following two nodes
3. Connect the linked list.

Implement the solution in **Swap Nodes in Pairs**

