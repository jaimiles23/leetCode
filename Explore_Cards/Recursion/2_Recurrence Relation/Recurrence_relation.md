/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-20 11:12:45
 * @modify date 2019-11-20 14:19:55
 * @desc [part 2 of leetCode's recursion explore card]
 */
# Recurrence Relation
Notes in this section are taken from [here](https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1644/)

Before implementing a recursive function, you must determine 2 things:
1. **Recurrence relation**: The relationship between the results of the problem, and the result of its subproblems
2. **Base case**: The case where one can compute the answer directly without any furtther recursion calls. This is sometimes called the 'bottom case', since they are often the cases where the problem has been reduced to the minimal scale, if you consider dividing the problem down into subproblems.

Once these two elements are fleshed out, you can implement a recursive function by calling the function according to the recurrence relation until the base case is reached.

## Pascal's triangle
A classic example is _Pascal's triangle_
> Pascal's triangle are a series of numbers in the shape of a triangle. In the triangle, the leftmost and rightmost numbers of each row are always 1. FOr the rest, each number is the sum of the two numbers directla bove it in the row.

Given the above definition, one is asked to generate Pascal's triangle up to a certain number of rows.

### Recurrence relation
Define a function, f(i, j) which returns the number in the pascal's triangle in the i-th row and j-th column. The recurrence relation is represented with the following formula:

f(i, j) = f(i - 1, j - 1) + f(i - 1, j)

### Base cases

The leftmost and rightmost numbers of each row are the base cases, which are always equal to 1. As a result, define the base case as follows:
f(i, j) = 1, where j == 1 or j == i

### Example
After defining the _recurrence relation_ and the _base case_, it's more intuitive to implement the recursive function. To apply the recursive formula to calculate f(5, 3), i.e., the 3rd number in the 5th row of the Pascal Triangle.
```
f(5, 3) = f(4, 2) + f(4, 3)
    f(4, 2) 
        = f(3, 1) + f(3, 2) 
            = 1 + f(2, 1) + f(2, 2) 
                = 1 + 1 + 1
                    = 3
    f(4, 3) = 
        f(3, 2) + f(3, 3)
            = f(2, 1) + f(2, 2) + f(3, 3)
                = 1 + 1 + 1
                    = 3
    = 6
```
The value in the 5th row and 3rd column, f(5, 3), is 6.

This recursion is implemented in _Pascals_triangle.py_

### Next
Note: in the above example, the recursive solution can incur duplicate calculations, e.g., computing the same intermediate numbers. THe next chapter discusses how to avoid _duplicate calculations_.

