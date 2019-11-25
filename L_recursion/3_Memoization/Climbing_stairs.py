"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-25 12:48:43
 * @modify date 2019-11-25 12:52:28
 * @desc [
Contains solutions for [#70 Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

Note: This problem is for all intents and purposes equivalent to solving the Nth index of the Fibonacci number.
This is because the number of possibilities is dependent on the possibilities of the previous two steps. 
Step 1 = 1 solution: 1 step
Step 2 = 2 solutions: 1 step + 1 step, and 0 steps + 2 steps.

I will solve this problem in 2 ways:
1. Recursively
2. Iteratively

Note: Both solutions will have O(N) time complexity, but the iterative solution will use constant, O(1), space.
However, when initially reasoning the problem, I consider the recursive solution a more intuitive approach.

## Recursive Solution
### Base cases
0 stairs = 0
1 stair = 1

### Recursive relation
stair(N) = stair(N - 1) + stair(N - 2)

### Complexity analysis
#### Time complexity
O(N) - calculate all numbers up until N once. Stores each number into memory

#### Space complexity
O(N) - keeps recursion data structure in memory for O(N). Also keeps cache of O(N), so practical memory is
O(2N).

### Leetcode Diagnostics:
Runtime: 28 ms, faster than 91.41% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

## Iterative Solution
This solution uses the dynamic programming sub-problem optimization as the recursive solution; the number of possibilities is 
found by combining the number of possibilities to the previous 2 steps.

The difference between the two solutions is the memory complexity. 
Because this solution uses 4 variables (n, result, prev_1, and prev_2), and does not recursively call another function, 
it has constant memory and is thus O(1).

### Complexity analysis
#### Time complexity
O(N) time complexity as each calculation to N is performed once.

#### Space complexity
Explained in the solution preview above.
 ]
 */
"""

class RecursiveSolution():
    """
    returns # of possibly combinations to reach the end point, 
    """
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        self.possible_combs = {
            0 : 0, 
            1 : 1,
            2 : 2
        }   
        return self.memoize(n)
    
    def memoize(self, n: int) -> int:
        """
        Dictionary cache of possible combinations to each staircase
        """
        if n in self.possible_combs.keys():
            return self.possible_combs[n]
        self.possible_combs[n] = self.memoize(n - 1) + self.memoize(n - 2)
        return self.memoize(n)
        

class IterativeSolution():
    def climbStairs(self, n: int) -> int:
        """
        Returns number of possible combinations to reach the Nth staircase iterative dynamic programming
        """
        if n <= 2: return n

        result = 0
        prev_1, prev_2 = 2, 1

        for _ in range(3, n + 1):
            result = prev_1 +  prev_2
            prev_1, prev_2 = result, prev_1

        return result


def test_solution():
    """
    Runs test cases for solutions to the Climbing stairs problem
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

    print('test 1')
    case = 2
    output = 2
    assert tester.climbStairs(case) == output

    print('test 2')
    case = 3
    output = 3
    assert tester.climbStairs(case) == output

    print('test 3')
    case = 4
    output = 5
    assert tester.climbStairs(case) == output



def main():
    test_solution()


if __name__ == "__main__":
    main()