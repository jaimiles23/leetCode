"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-16 18:58:20
 * @modify date 2019-11-18 13:36:20
 * @desc [
     __SCRAPED__
Challenge
I tried to use a binary search algorithm to check for the pivot. However, the inclusion of negative numbers makes it unweidly to determine if you are moving left or right. I ran through about a dozen test cases in order to work out the math. Two example cases:
Starting at index [2], [-1,-1,0,1,0,-1] should move right to [4], [-1,-1,-1,-1,0,1] should move left to [1].  A solution may still be possible, but would require additional development, e.g., looking into the future, and seeing if movement would move closer or further from the desired solution. And then, there may be an issue of calculating -1, -1, … and then not including a 999 within the range

Lessons
This was the first solution to the problem that I attempted. I brainstormed different ideas, e.g., creating the sum of the list on index at a time, which is an(O(N)) solution time. And I wanted to start with an optimized solution.  
From this challenge, I learned that I am still developing some intuition for developing optimized algorithms, and that I should still start with the simplest solution. While developing the naïve solution, you solidify your understanding of the problem (e.g., negative numbers) and can better judge the merits of other optimized algorithms before investing time developing them.  


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

            print(f"""
            pivot\t{pivot}
            right\t{right}
            left\t{left}""")

            if left >= right:   #Base case
                return -1

            l_sum, r_sum = sum(nums[:pivot]), sum(nums[pivot + 1:])
            if l_sum == r_sum: return pivot

            ## Determine left or right pivot movement. Depends on negative numbers in list too
            l_move, r_move = False, False
            if l_sum > r_sum and r_sum > 0 and l_sum > 0:
                l_move = True
            elif l_sum < r_sum and l_sum < 0 and r_sum < 0:
                l_move = True
            else:
                r_move = True

            ## Move
            if l_move:
                right = pivot
                pivot = pivot - int((right - left) / 2 + 0.5) 
            elif r_move:
                left = pivot + 1
                pivot = pivot + int((right - left) / 2 + 0.5)
            

            return binary_search(nums, left, right, pivot)
        
        return binary_search(nums, 0, len(nums) - 1, int((len(nums) - 1) / 2))


def test_binary_search():
    """
    Unit tests for binary search
    """
    tester = Solution()

    print('test 1')
    nums = [1, 0, 0, 1, 0, 0, 0, 0, 1]
    print(tester.pivotIndex(nums = nums))

    print('test 2')
    nums = [9, 0, 0, 0, 0, 0, 0, 0]
    print(tester.pivotIndex(nums = nums))

    print('test 3')
    nums = [5, 0, 0, 0, 0, 6]
    print(tester.pivotIndex(nums))


def main():
    # test_binary_search()
    tester = Solution()
    ut.unit_tests(tester.pivotIndex)

    



if __name__ == "__main__":
    main()
