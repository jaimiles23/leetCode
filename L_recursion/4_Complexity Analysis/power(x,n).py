"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-25 23:19:28
 * @modify date 2019-11-26 11:36:25
 * @desc [
Solution to leetCode's [#50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

Three initial solutions:
1. Pythonic
2. Recursive
3. Iterative

Note: To avoud Runtime error, must understand special rule for powers:
When a value is raised to an even power, square the value and divide the power / 2.
E.g.,
    9 ** 2 == 9*9 ** 2/1 
    9 ** 4 == 91 ** 2 == 9 * 9 * 9 * 9

## Pythonic
This solution uses base Python calculations to determine the solution:
` x ** n`

### Complexity analysis
#### Time complexity:
O(1) - one calculation
#### Space complexity
O(1) - holds 2 variables: x and n, and thus has a constant space complexity.

### Leetcode diagnostics
Runtime: 28 ms, faster than 92.38% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pow(x, n).

## Recursive
Created helper function to check for select parameters outside of the recursion:
- n < 0
- x == 0
- n == 0

### Basecase
n == 1: return x

### Recursive relation:
x ** n == x * x ** (n-1)
    and
if n / 2 == 0:
    x ** n == (x*x) ** (n/2)

### Complexity Analysis
#### Time complexity
O(log n) since N is halfed with each iteration -- whenever it is an even number.

#### Space complexity
O(log n) since the recursive structure will be the same as the number of calculations.

### LeetCode Diagnostics:
Runtime: 28 ms, faster than 92.38% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pow(x, n).

## Iterative solution
This dynamic programming approach utilizes the same relations as the recursive solution:
    x ** n == x * x ** (n-1)
    and
    x ** n == (x * x) ** (n/2)

### Complexity Analysis
#### Time complexity
O(log N) as each even iteration halves the length of N

#### Space complexity
O(1) as there is constant space complexity. There is space assigned to 3 variables: x, n, and result

### LeetCode Diagnostics
Runtime: 28 ms, faster than 92.38% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
 ]
 */
"""

class Pythonic():
    def myPow(self, x: float, n: int) -> float:
        """
        returns x ** n uses pythonic calculations
        """
        return round(x ** n, 5)


class Recursive():
    def myPow(self, x: float, n: int) -> float:
        """
        returns x ** n using recursion
        """
        def helper(x: float, n: int) -> float:
            if n == 1: return x
            elif n % 2 == 0:
                return helper(x * x, n / 2) 
            else: 
                return x * helper(x, n - 1)
        
        if x == 0: 
            return 0
        elif n == 0: 
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        return round(helper(x, n), 5)


class Iterative():
    def myPow(self, x: float, n: int) -> float:
        """
        returns x ** n uses iterative dynamic programming
        """
        if x == 0: return 0
        if n == 0: return 1
        if n < 0:
            x = 1 / x
            n = -n

        result = x
        while n > 1:
            if n % 2:
                result, n = result * x, n - 1
            else:
                result, x, n = result * x, x * x, n / 2

        return round(result, 5)


def test_solutions():
    """
    Runs unit tets for # 50. Pow(x, n)
    """
    # tester = Pythonic()
    # tester = Recursive()
    tester = Iterative()

    print('test 1')
    x, n = 2.00000, 10
    output = 1024.00000
    print(tester.myPow(x, n), output)
    assert tester.myPow(x, n) == output

    print('test 2')
    x, n = 2.10000, 3
    output = 9.26100
    print(tester.myPow(x, n), output)
    assert tester.myPow(x, n) == output

    print('test 3')
    x, n = 2.00000, -2
    output = 0.25
    print(tester.myPow(x, n), output)
    assert tester.myPow(x, n) == output

    print('test 4')
    x, n = 8.88023, 3
    output = 700.28148
    print(tester.myPow(x, n), output)
    assert tester.myPow(x, n) == output

    print('test 5')
    x, n = 1.00001, 123456
    output = 3.43684
    print(tester.myPow(x, n), output)
    assert tester.myPow(x, n) == output


def main():
    test_solutions()


if __name__ == '__main__':
    main()
