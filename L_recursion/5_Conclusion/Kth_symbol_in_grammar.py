"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-26 15:26:06
 * @modify date 2019-11-26 15:45:19
 * @desc [
Solutions to leet code's [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/)

Two dynamic programming approaches can be employed to solve this problem:
1. Recursive
2. Iterative

Both of these approaches are bottom-up, building the grammar structure until the Nth row is reached.  
Then, the Kth index of the Nth row is returned.

Note: both of these solutions run into Time Limit Exceptions when executed to high levels, e.g., n = 30, k = 434991989.

## Recursive
Builds final structure with recurison.

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

 ]
 */
"""

class RecursiveSolution():
    def kthGrammar(self, N: int, K:int) -> str:
        """
        Returns the Kth element of the Nth row of the grammar structure
        """
        def create_Nth_row(row: str, num: int) -> str:
            """
            returns next row of recursive structure
            """
            ## Basecase
            if N == num:
                return row
            
            new_row = str()
            for char in row:
                if char == '0':
                    new_row += '01'
                else:
                    new_row += '10'
            
            return create_Nth_row(new_row, num + 1)
        
        row = create_Nth_row('0', 1)
        print(row)
        return int(row[K - 1])


class IterativeSolution():
    def kthGrammar(self, N: int, K: int) -> str:
        row = '0'
        row_num = 1

        while row_num != N:
            new_row = str()
            
            for char in row:
                if char == '0':
                    new_row += '01'
                else:
                    new_row += '10'
            
            row = new_row
            row_num += 1
        
        return int(row[K - 1])


def test_solutions():
    """
    Runs unit tests for # 779
    """
    # tester = RecursiveSolution()
    tester = IterativeSolution()

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