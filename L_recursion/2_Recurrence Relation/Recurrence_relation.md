/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-20 9:12:45
 * @modify date 2019-11-20 11:15:04
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


