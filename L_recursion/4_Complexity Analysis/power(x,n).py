"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-25 23:19:28
 * @modify date 2019-11-25 23:19:28
 * @desc [
Solution to leetCode's [#50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

Three initial solutions:
1. Pythonic
2. Recursive
3. Iterative

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
 ]
 */
"""

class Pythonic():
    def myPow(self, x: float, n: int) -> float:
        """
        returns x ** n uses pythonic calculations
        """
        return round(x ** n, 5)


def test_solutions():
    """
    Runs unit tets for # 50. Pow(x, n)
    """
    tester = Pythonic()

    print('test 1')
    x, n = 2.00000, 10
    output = 1024.00000
    assert tester.myPow(x, n) == output
    # print(tester.myPow(x, n), output)

    print('test 2')
    x, n = 2.10000, 3
    output = 9.26100
    assert tester.myPow(x, n) == output
    # print(tester.myPow(x, n), output)

    print('test 3')
    x, n = 2.00000, -2
    output = 0.25
    assert tester.myPow(x, n) == output
    # print(tester.myPow(x, n), output)


def main():
    test_solutions()


if __name__ == '__main__':
    main()
