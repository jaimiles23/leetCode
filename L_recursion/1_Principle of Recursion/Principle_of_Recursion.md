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


