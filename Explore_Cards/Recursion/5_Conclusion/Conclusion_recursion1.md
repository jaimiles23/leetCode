# Conclusion - Recursion 1
Recursion is a powerful tool but not a silver bullet. There may be time or space constraints to consider, and recursion may incur undesired side effects, e.g., stack overflow.

To better apply recursion to solve problems:

## Write down the recurrence relationship
It is not always evident how to apply a resursive algorithm. However, it is always helpful to deduct some relationships with the help of mathematical formulas, which can be represented by the recurrence relationship. This is shown in [Unique Binay Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/), which can be solved by recursion with the help of mathematical formulas

## Whenever possible, apply memoizaiton
Recursive algorithm development often starts with the naive solution that has duplicate calculations, e.g., Fibonacci numbers.  Memoization may greatly improve the time complexity with the trade of space complexity.

## When stack overflows, tail recursion might come to help
Different from memoization, tail recursion optimizes the _space complexity_ of the algorithm by eliminating the stack overhead incurred by recursion. Most importantly, tail recursion avoids the `stack overflow` that may come with recursion. Another advantage is that it's often easier to read and understand because there is no post-call dependency in tail recursion - a.k.a., there is no post-call dependency in tail recursion.

Whenever possible, one should strive to apply tail recursion.