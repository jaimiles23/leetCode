# Duplicate calculation in recursion
Recursion can be an intuitive and powerful way to implement an algorithm. However, it can bring undesired penalties in performance, e.g., duplicate calculations. For instance, in Pascal's triangle, intermediate results are calculated multiple times.

One common technique to address duplicate calculations is **memoization**. 

## Fibonnaci number
The [Fibonnaci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) is a series of numbers representing the sum of the two preceding numbers, starting with 0 and 1. 

### Recurrence relation
If we use the function F(n) to represent the Fibonacci number at index n, can derive the following recurrence relation:
F(n) = F(n - 1) + F(n - 2)

### Base cases
F(0) = 0, F(1) = 1

0 is the base case, and 1 is the 1st index. Index 2 == 1 because F(0) + F(1) == 1.

### Code
Given this definition, we can implement the following function
```
def fibonacci(self, n: int) -> int:
    """
    returns the nth index of the fibonnaci sequence
    """
    if n in [0, 1]: return n

    return F(n - 1) + F(n - 2)
```

### Demonstration
To know the number of F(4), we can derive the following formula:
```
F(4) = F(3) + F(2)
    = F(2) + F(1) + F(1) + F(0)
        = F(1) + F(0) + 1 + 1 + 0
            = 1 + 0 + 1 + 1 + 0
                = 3
Thus, F(4) = 3
or
0, 1, 1, 2, 3
```

### Memoization
To eliminate the duplicate calculations above, _store_ the intermediate results in the cache to reuse them later. This is called **memoization**.

`Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. (Source: wikipedia)`
_Note: This definition does not necessarily anchor memoization to recursive function, although it is heavily associated_

To incorporate memoization, use a hash table to track the results of F(n) with each n as the key. The hash table serves as a cache to avoid duplicate calculations.  The memoization technique is a good example to reduce compute time _in exchange for additional space_.

```
def fibonacci(self, N: int) -> int:
    """
    returns fibonnaci number at nth index. Uses memoization to decrease speed complexity but increase space complexity.
    """
    fib_num = {0: 0, 1: 1}

    def fib_recur(N):
        if N in fib_num.keys():
            return fib_num[N]
        
        else: 
            result = fib_recur(N - 1) + fib_Recur(N - 2)

            fib_num[N] = result
            return result
        
    return fib_recur(N)
```

Implement memoizaiton in the following two problems: 
1. [Fibonacci number](https://leetcode.com/problems/fibonacci-number/)
2. [Climing stairs](https://leetcode.com/problems/climbing-stairs/)

