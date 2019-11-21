"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-20 14:21:00
 * @modify date 2019-11-20 17:41:29
 * @desc [
Taken from leetcode 118. [Pascsal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
Given a non-negative integer numRows, this script generates the first x rows (var = numRows) of Pascal's triangle.

Note: in this formula, i represents row and j represents column.

Basecases:
f(i, j) == 0 if j == 1 or j == i

Recursive relation:
f(i, j) = f(i - 1, j - 1) + f(i - 1, j)

LeetCode Diagnostics:
Runtime: 28 ms, faster than 94.68% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.

Thoughts:
I am not happy with my implementation. 
Steps:
1. Instantiate data structure
2. Double for loop: for each list, for each index
3. Recursive calls from the specified indices

By definition, this is a recursive solution, but it relies heavily on iterative elements. I would much prefer to implement
a pure recursive solution, but did not find such a solution.
]
 */
"""

class Solution:
    def generate(self, numRows: int) -> list:
        """
        User_defined.
        returns a list of lists until the numRows of Pascal's triangle.
        """
        # Define recursive function
        def fill_triangle(triangle: list, row: int, column: int) -> int:
            """
            returns integer to fill pascal's triangle index
            """
            # Base cases
            if column == 0 or column == row:
                return 1
            # Stored results in data structure to avoid time error
            try:
                return triangle[row][column]
            except IndexError:
            # Recursive relation
                return fill_triangle(triangle, row - 1, column - 1) + fill_triangle(triangle, row - 1, column)

        # Instantiate triangle data structure
        triangle = []
        for row in range(numRows):
            triangle.insert(row, [])
        
        # Iterate through structure
        for row in range(len(triangle)):
            for column in range(row + 1):
                triangle[row].insert(column, fill_triangle(triangle, row, column))          

        return triangle
            

def test_pascal_triangle():
    """
    runs units tests for pascal's triangle
    """
    tester = Solution()
    
    print('test 1')
    numRows = 5
    output = [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1]
        ]
    # print(tester.generate(numRows))
    assert tester.generate(numRows) == output
    

def main():
    test_pascal_triangle()


if __name__ == '__main__':
    main()
        


