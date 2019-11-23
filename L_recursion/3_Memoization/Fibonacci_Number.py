"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-22 15:59:05
 * @modify date 2019-11-22 15:59:12
 * @desc [
# Fibonacci Number
Solution to [#509 Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

There are two fundamentally different ways to approach this problem:
1. Recursively
2. Iteratively

## Recursive

### Recursive relation
F(N) = F(N - 1) + F(N - 2)

### Base Case
F(0) = 0
F(1) = 1

 ]
 */
"""

class NaiveRecursiveSolution():
    def fib(self, N: int) -> int:
        """
        Returns the Nth index of the Fibonacci sequence using recursion.
        """
        if N in [0, 1]:
            return N
        
        return self.fib(N - 1) + self.fib(N - 2)


class RecursiveSolution():
    def fib(self, N: int) -> int:
        """
        Returns the Nth index of the Fibonacci sequence using recursion and memoization.

        Note to self: do once here alone, then check how to do it with the decorator function mentioned in notes.
        """


def test_fibonacci_sequence():
    """
    runs unit tests for the fibonacci sequence
    """
    f_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

    tester = NaiveRecursiveSolution()

    for i in range(len(f_seq)):
        assert tester.fib(i) == f_seq[i]
    print('done')


def main():
    test_fibonacci_sequence()


if __name__ == "__main__":
    main()    

