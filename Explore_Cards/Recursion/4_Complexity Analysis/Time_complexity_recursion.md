# Time Complexity - Recursion
These notes demonstrate how to calculate the time complexity for recursive algorithms.

A recursive algorithm's time complexity is the product of the number of recursion invocations (denoted as R) and the time complexity of calculated (denoted as O(s)) that incurs with each recursion call:

```O(T) = R * O(s)```

## Example
In the problem [printReverse](https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1439/), you print the string in the reverse order.

A recurrence relation to solve the problem is expressed as follows:

```printReverse(str) = printReverse(str[1...n]) + print(str[0])```

where `str[1...n]` is the substring of the input string str, without the leading character `str[0]`

The function is recusrively invoked `n` times, where `n` is the size of the input string.  At the end of each recursion, print the leading character.  THus, the time complexity is constant, O(1).

The overall time complexity of the recursive function printReverse(str) is 
```O(printReverse) = n * O(1) = O(n)```

## Execution tree
It is rare that the number of recursion calls are linear to the size of the input. For example, the Fibonacci recursion relation is defined as `f(n) = f(n - 1) + f(n - 2)`. It does not seem straightforward to calculate the number of recursion invocations during the execution of the Fibonacci function.

In this case, resort to th e **execution tree**, which denotes the execution flow of a recursive function.  Each node in the tree represents an invocation of the recursive function. Therefore, the total number of nodes is the number of recursion calls.

The execution tree of a recursive function would form an **n-ary tree**, where n is the number of times the recursion appears in the recurrence relation.

The Fibonacci function forms a **binary tree** because the recurrence relation calls the function twice:
1. f(n - 1)
2. f(n - 2)
e.g.,
`f(4) = f(3) + f(2)`

In a full binay tree with n levels, the total number of nodes would be ` 2 ** n - 1`.  Therefore, the upper bound for the number of recursion in f(n) would be `2 ** n -1 `. Thus, we can estimate the time complexity for f(n) to be O(2**n).

## Memoization
By caching and reusing the intermediate results, memoization can greatly reduce the number of recursion calls, i.e., reducing the number of branches in the execution tree. Take this reduction into account when analyzing the time complexity of recursion algorithms with memoization. 

In this case, memoization would save the result of the Fibonnaci number for each index n. Thus, each calculation will only occur once. From the recurrence relation, we know that the indices must be calculated to f(n - 1) to calculate the preceding numbers.

Thus, to calculate the time complexity of memoization, use `O(n) * O(s)`, which in this case is O(1), thus resulting in O(n).



