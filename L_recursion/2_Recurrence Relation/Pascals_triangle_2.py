"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-20 19:04:42
 * @modify date 2019-11-20 20:01:34
 * @desc [
Solution to leetcodes Pascal's Triangle II, from [here](https://leetcode.com/problems/pascals-triangle-ii/submissions/)

#############
user_solution:

leetCode diagnostics:
Runtime: 20 ms, faster than 99.77% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle II.

**Complexity analysis**
Time complexity:
O(n^2) because it's a double for-loop, cycle through the number of rows for each index in the row

Space_complexity:
O(K) because we use 2 * O(k) as we are only storing results and temp.
]
 */
"""

class user_solution():
    def getRow(self, rowIndex: int) -> list:
        """
        returns nth row of Pascal's triangle.

        This uses a bottom-up iterative approach to return the nth row. Each previous row is stored as a 'temp' row. 
        This is to preserve memory usage.
        """
        results = []
        
        for i in range(0, rowIndex + 1):
            temp = [1 for _ in range(i + 1)]

            for j in range(1, i):
                temp[j] = results[j - 1] + results[j]
            
            results = temp
        return results

def test_solutions():
    """
    runs unit tests for solution assigned to tester
    """
    tester = user_solution()
    
    print('test 1')
    row_index = 3
    output = [1,3,3,1]
    # print(tester.getRow(row_index))
    assert tester.getRow(row_index) == output


def main():
    test_solutions()

if __name__ == '__main__':
    main()