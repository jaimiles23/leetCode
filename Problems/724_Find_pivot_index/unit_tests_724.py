"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-16 20:31:03
 * @modify date 2019-11-18 11:57:38
 * @desc [
Includes various unit tests for 724. Find Pivot Index. Unit tests include the two examples provided by the problem.
 ]
 */

"""

def unit_tests(solution) -> None:
    """
    runs unit tests for solution to #724 Find Pivot Index
    """

    print('test 1')
    nums = [1, 7, 3, 6, 5, 6]
    output = 3
    assert solution(nums) == output

    print('test 2')
    nums = [1, 2, 3]
    output = -1
    assert solution(nums) == output

    print('test 3')
    nums = [-1,-1,-1,-1,-1,-1]
    output = -1
    assert solution(nums) == output

    print('test 4')
    nums = [-1,-1,-1,-1,-1,0]
    output = 2
    assert solution(nums) == output

    print('test 5')
    nums = [-1,-1,-1,-1,0,1]
    output = 1
    assert solution(nums) == output

    print('test 6')
    nums = [-1,-1,0,1,0,-1]
    output = 4
    assert solution(nums) == output