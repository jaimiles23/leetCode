"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-26 15:26:06
 * @modify date 2019-11-26 18:25:12
 * @desc [
Solutions to leet code's [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/)

Two dynamic programming approaches can be employed to solve this problem:
1. Recursive
2. Iterative

Both of these approaches are bottom-up, building the grammar structure until the Nth row is reached.  
Then, the Kth index of the Nth row is returned.


## Recursive & Iterative
Both solutions build final structure using bottom-up approaches

### Base case:
row = N: return [k]

### Recursive relation
F(structure, row) == F(modified structure, row + 1)

### Complexity Analysis
#### Time complexity
O(N) - required to build the Nth layer, and then return the Kth index.

#### Space complexity
O(N) - Each recursive call will be stored in memory, and the variables for row, N, and K.

### leetCode Diagnostics

Note: both of these solutions run into Time Limit Exceptions when executed to high levels, e.g., n = 30, k = 434991989.

# Heuristics:
Instead of using bottom-up algorithms, where the entire data structure is constructed, we can instead use a top down approach
that depends on 3 principles to determine the value at K.
1. The value of K depends on Nth - 1 row directly.
    This is true because each subsequent row is built by the previous rule. This may seem tediously obvious, but it is 
    important to acknowledge in order to prove heuristics (2) and (3).
2. The Kth term is dependent on the Kth // 2 element of the Nth - 1 row. Remembering that this problem deals with index 1,
the following are true:
    2a. If the Kth element is odd, it will be the same as the Kth // 2 element. 
    2b. If the Kth element is even, it will be the inverse of the Kth // 2 element.

Step 2 is true because 0 yields 01, and 1 yields 10.

As such, I will use these heuristics to create the recursive solution below.
## Recursive solution 
### LeetCode Diagnostic:
Runtime: 20 ms, faster than 99.11% of Python3 online submissions for K-th Symbol in Grammar.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for K-th Symbol in Grammar.


 ]
 */
"""

class RecursiveSolution():
    def kthGrammar(self, N: int, K: int) -> str:
        """
        Returns the Kth element on the Nth row using recursion
        """
        # Base case for the top and left side of pyramid
        if N == 1 or K == 1:
            return 0
        
        if K % 2 == 1:
            return self.kthGrammar(N - 1, K // 2 + 1)
        
        if self.kthGrammar(N - 1, K // 2) == 1: 
            return 0
        else:
            return 1


def test_solutions():
    """
    Runs unit tests for # 779
    """
    # tester = RecursiveSolution()
    tester = RecursiveSolution()

    print('test 1')
    n, k = 1, 1
    output = 0
    assert tester.kthGrammar(n, k) == output
    
    print('test 2')
    n, k = 2, 1
    output = 0
    assert tester.kthGrammar(n, k) == output
    
    print('test 3')
    n, k = 2, 2
    output = 1
    assert tester.kthGrammar(n, k) == output
    
    print('test 4')
    n, k = 4, 5
    output = 1
    assert tester.kthGrammar(n, k) == output

    print('test 5')
    n, k = 30, 434991989
    # print(tester.kthGrammar(n, k))


def main():
    test_solutions()


if __name__ == '__main__':
    main()