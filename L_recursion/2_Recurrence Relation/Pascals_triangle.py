"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-20 14:21:00
 * @modify date 2019-11-20 18:43:51
 * @desc [
Taken from leetcode 118. [Pascsal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
Given a non-negative integer numRows, this script generates the first x rows (var = numRows) of Pascal's triangle.

Note: in this formula, i represents row and j represents column.

Base cases:
f(i, j) == 0 if j == 1 or j == i

Recursive relation:
f(i, j) = f(i - 1, j - 1) + f(i - 1, j)

user solution() LeetCode Diagnostics:
Runtime: 16 ms, faster than 99.93% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.

Thoughts:
I am not happy with my implementation. 
Steps:
1. Instantiate data structure
2. Double for loop: for each list, for each index
3. Recursive calls from the specified indices

By definition, this is a recursive solution, but it relies heavily on iterative elements. Despite it's good performance, 
I would much prefer to implement a pure recursive solution that does not rely on try|except. This may require a top-down 
approach.

The practical time complexity would be:
    num_rows(1 (create list) + 1 (outerloop) + num_rows (inner loops)), which simplies to O(num_rows ^ 2)

#####################
approach1() leetCode diagnostics

leetCode diagnostics:
Runtime: 24 ms, faster than 98.36% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.

Thoughts:
Although this solution has the same practical results (natural run-time variation), I appreciate the cleaner coding and 
removing the additional O(N) pass. 

Complexity Analysis:
**Time analysis**
O(numsRows ^ 2) because the outerloop runs num_rows times, and for each of those iterations the inner loops runs 
num_rows times.
    Thus:
    num_rows(num_rows + 1) / 2 = num_rows ^ 2 / 2 + num_rows / 2 = O(num_rows ^ 2)
**Space compelexity**
Because results from each loop are stored in the data structure, it requires O(num_rows ^ 2) memory.

]
 */
"""

class user_solution():
    def generate(self, numRows: int) -> list:
        """
        User_defined.
        returns a list of lists until the numRows of Pascal's triangle.

        This function uses a bottom-up approach where after the existing data structure is initialized, the simplest sub-problems,
        i.e., the base cases, are solved first, and then used to solve more complex sub-problems. 
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
"""
Note: when comparing this to approach 1: dynamic programming solution - this solution is inefficient. First, both solutions
are O(n^2) because of the dual for loops. However, this solution also instantiates the list in a separate for-loop, thus 
in a practical setting having an extra O(n) pass.

Additionally, this iterative bottom-up approach avoids any try/excepts. This is not recursion (does not call itself), but 
it is a type of dynamic programming.
"""

class approach_1():
    """
    This is a replication of the Approach 1: Dynamic Programming solution applied to the problem by leetCode. 
    """
    def generate(self, numRows: int) -> list:
        triangle = []
        for i in range(numRows): 
            row = [1 for _ in range(i + 1)]

            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle


def test_pascal_triangle():
    """
    runs units tests for pascal's triangle
    """
    # tester = user_solution()
    tester = approach_1()
    
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
        


