"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-20 14:21:00
 * @modify date 2019-11-20 14:21:01
 * @desc [
Taken from leetcode 118. [Pascsal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
Given a non-negative integer numRows, this script generates the first numRows of Pascal's triangle.

Note: in this formula, i will represent the row, and j the column.

Basecases:
f(i, j) == 1 if j == 1 or j == i

Recursive relation:
f(i, j) = f(i - 1, j - 1) + f(i - 1, j)

 ]
 */
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        returns a list of lists until the nth row of Pascal's triangle.
        """
        def generate_rows(i: int, j: int, num_rows: int) -> list:
            """
            returns list of lists representing pascal's triangle.
            uses two integers to track rows and columns.
            """
            if i == 1 or j == 1 or j == i:
                return 1
            pass
            



