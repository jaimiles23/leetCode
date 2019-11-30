"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-22 15:59:05
 * @modify date 2019-11-25 12:44:32
 * @desc [
# Fibonacci Number
Solution to [#509 Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

There are two fundamentally different ways to approach this problem:
1. Recursively
2. Iteratively

Additionally, I found a 3rd, mathematical approach to finding the Nth index of the Fibonacci sequence usin the:
3. Golden Ratio

## Recursive

### Recursive relation
F(N) = F(N - 1) + F(N - 2)

### Base Case
F(0) = 0
F(1) = 1

### Complexity Analysis
#### Time complexity
O(2 ** N) 
The amount of operations needed grows exponentially with N. This is because for each N, you must calculate two numbers:
N - 1, and N - 2. Solutions are not saved in memory.

#### Space Complexity
O(N) - need space proportionate to N to account for the max size of the stack in memory. There may be cases where there is
not enough physical memory, and leads to a `StackOverflowError` because the function recurses too deeply.

## Recursive with Memoization
### Memoization
Stores the results from the recursion in the cache to retrieve and avoid calculations.

### Complexity analysis
#### Time complexity
O(N) because each index until N is still calculated.

#### Space complexity
O(N) The size of the data structure is proportionate to N. Also, each N is also stored for O(1) space. Thus, 
practical space complexity is O(2N).

## Iterative
Checks for index 0 or 1 as base cases.

Determines next index by adding the two previous numbers. Loops until Nth index.

### Complexity Analysis
#### Time complexity
O(N) - must still calculate all values from 2 to N once.

#### Space complexity
O(1) - requires 1 space for N, and three spaces for result, t1, and t2. Since the amount of space doesn't change, 
this is constant space complexity.

## Golden Ratio
Utilizes the golden ratio to calculate the nth term of the Fibonacci sequence. This equation is taken 
from [mathisfun](https://www.mathsisfun.com/numbers/fibonacci-sequence.html),
and validated with unit tests.

### Equation:
GOLDEN_RATIO = 1.618034

`N = (GOLDEN_RATIO ** N - (1 - GOLDEN_RATIO) ** N) / 5 ** 0.5`

Before returning, must round to an integer

### LeetCode diagnostics
Runtime: 20 ms, faster than 99.67% of Python3 online submissions for Fibonacci Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Fibonacci Number.


## Bottom-Up Approaching using Memoization
Provided by leetCode. Very similar to previous solutions, but uses a wrapper function.

 ]
 */
"""

class RecursiveSolution():
    def fib(self, N: int) -> int:
        """
        Returns the Nth index of the Fibonacci sequence using recursion.
        """
        if N in [0, 1]:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


class RecursiveMemoizationSolution():
    def fib(self, N: int) -> int:
        """
        returns the Nth index of the Fibonacci sequence using recursion and memoization
        """
        fib_nums = {
            0: 0,
            1: 1,
        }
        def recursive_helper(N: int) -> int:
            if N in fib_nums.keys():
                return fib_nums[N]
            
            result = recursive_helper(N - 1) + recursive_helper(N - 2)
            fib_nums[N] = result
            return result

        return recursive_helper(N)


class MathSolution():
    def fib(self, N: int) -> int:
        """
        returns the Nth index of the Fibonacci sequence using the golden ratio.

        Note: The golden ratio is 1.618034
        # """

        GOLDEN_RATIO = 1.618034
        return int(round((GOLDEN_RATIO ** N - (1 - GOLDEN_RATIO) ** N) / 5 ** 0.5, 0))


class IterativeSolution():
    def fib(self, N: int) -> int:
        if N in [0, 1]: return N

        next_index = 0
        t1, t2 = 1, 0

        for _ in range(2, N + 1):
            next_index = t1 + t2
            t1, t2 = next_index, t1

        return next_index


class Approach2BottomUpMemoization:
    def fib(self, N: int) -> int:
        if N <= 1: 
            return N
        return self.memoize(N)
    
    def memoize(self, N: int) -> dict:
        """
        Helper function to create dictionary
        """
        nums = {
            0: 0, 
            1: 1
        }
        for i in range(2, N + 1):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[i]


class Approach3TopDownMemoization():
    def fib(self, N: int) -> int:
        if N <= 1: return N
        self.nums = {
            0 : 0, 
            1 : 1
        }
        return self.memoize(N)

    def memoize(self, N: int) -> int:
        if N in self.nums.keys(): 
            return self.nums[N]
        self.nums[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return self.memoize(N)
        




def test_fibonacci_sequence():
    """
    runs unit tests for the fibonacci sequence
    """
    f_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

    # tester = RecursiveSolution()
    # tester = MathSolution()
    # tester = RecursiveMemoizationSolution()
    # tester = IterativeSolution()
    # tester = Approach2BottomUpMemoization()
    tester = Approach3TopDownMemoization()

    print('index\t#')
    for i in range(len(f_seq)):
        print(i, '\t', tester.fib(i), sep = '')
        assert tester.fib(i) == f_seq[i]
    print('done')


def main():
    test_fibonacci_sequence()


if __name__ == "__main__":
    main()    

