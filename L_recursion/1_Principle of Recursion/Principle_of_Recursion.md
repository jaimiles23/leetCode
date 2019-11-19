# Principle of Recursion
**Recursion** is an approach to solving problems using a function that calls itself as a subroutine.

Each time a recursive function calls itself, it reduces the given problem into subproblems. The recursion call continues until it reaches a point where the subproblem can be solved without further recursion - AKA a "base case."

A recursive function has 2 properties to prevent an infinite loop:
1. A simple base case (or cases) that does not use recursion to produce an answer.
2. **Recurrence relation**, a set of rules that reduces all other cases to the base case.

# Example
Simple programming problem: print a string in reverse order:

This is an easy problem to solve iteratively via range(len(word) - 1, - 1, - 1)

To solve recursively, we must define the desired function:
**Python** - user defined code
```
def print_reverse(word: str) -> None:
    """ 
    prints a string in reverse
    """
    if len(word) == 1: 
        print(word)
    else:
        print(word[-1], end = '')
        print_reverse(word[:-1])
```
**C++**
```
void printReverse(const char *str) {
  if (!*str)
    return;
  printReverse(str + 1);
  putchar(*str);
}
```
**Java**
```
private static void printReverse(char [] str) {
  helper(0, str);
}

private static void helper(int index, char [] str) {
  if (str == null || index >= str.length) {
    return;
  }
  helper(index + 1, str);
  System.out.print(str[index]);
}
```

Note: recursion can be done by modifying the input array **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory - allocated to a temporary variable.

# Reverse_string solution notes
Use this example to discuss 2 points:
1. In-place space complexity
2. Two pointers approach

By definition, an in-place algorithm transforms input using no auxiliary data structure. However, space is used by other actors, e.g., temp variables. A recursive function _is_ in place, but not constance space. This is because of **recursion stack**.

## Approach 1: Recursion In-Place O(N) Space
This example uses two helper pointers, left and right, which are passed to the recursive helper function.

### Python solution
```
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
```

### Complexity Analysis
**Time complexity**: O(N) time to perform N/2 swaps.
**Space complexity**: O(N) to keep the recursion stack - the recursion will call list slices until N/2.

## Approach 2: Two Pointers, Iteration, O(1) Space
Two points are used to process two array elements at the same time. Implementation has one pointer at the beginning, and another pointer at the end. These pointers are incremented until they converge.
_note: sometimes this needs to be generalized to more points, e.g., for the classical Sort Colors problem._

### Python solution
```
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
```
### Complexity Analysis
**Time complexity**: O(N) to swap N/2 elements
**Space complexity**: (O1), as it's constant space solution





