"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-16 18:58:20
 * @modify date 2019-11-16 18:58:20
 * @desc [
Returns pivot index through binary search
 ]
 */
"""

## Modules
import unit_tests_724 as ut

class Solution():   
    def pivotIndex(self, nums: list) -> int:
        """
        returns pivot index for list using binay search method. If no pivot index, returns -1
        """
        def binary_search(nums: list, left: int, right: int, pivot: int) -> int:
            """
            binay search for index
            """

            if left >= right:
                return -1

            l_sum, r_sum = sum(nums[:pivot]), sum(nums[pivot + 1:])

            if l_sum > r_sum:
                right = pivot - 1
                pivot = pivot - int((right - left) / 2 + 0.5) 
            elif r_sum > l_sum:
                left = pivot + 1
                pivot = pivot + int((right - left) / 2 + 0.5)
            else: 
                return pivot
            
            return binary_search(nums, left, right, pivot)
        
        left = 0
        right = len(nums) - 1
        pivot = int(len(nums) / 2)
        return binary_search(nums, left, right, pivot)


def test_binary_search():
    """
    Unit tests for binary search
    """
    tester = Solution()

    print('test 1')
    nums = [1, 0, 0, 1, 0, 0, 0, 0, 1]
    # print(tester.pivotIndex(nums = nums))

    print('test 2')
    nums = [9, 0, 0, 0, 0, 0, 0, 0]
    # print(tester.pivotIndex(nums = nums))

    print('test 3')
    nums = [5, 0, 0, 0, 0, 6]
    # print(tester.pivotIndex(nums))


def main():
    # test_binary_search()
    tester = Solution()
    ut.unit_tests(tester.pivotIndex)

    



if __name__ == "__main__":
    main()
