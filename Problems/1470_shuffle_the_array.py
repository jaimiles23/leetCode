"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-11 10:44:42
 * @modify date 2020-09-11 10:44:42
 * @desc [
    Solution to 1470. Shuffle the array:
        https://leetcode.com/problems/shuffle-the-array/
    
    Generator solution with 2 yields:

Runtime: 52 ms, faster than 98.82% of Python3 online submissions for Shuffle the Array.
Memory Usage: 13.7 MB, less than 97.38% of Python3 online submissions for Shuffle the Array.

Time complexity: O(N)
 ]
 */
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        def gen_shuffle_list(nums, n):
            for i in range(n):
                yield nums[i]
                yield nums[i + n]
                
        return list(gen_shuffle_list(nums, n))
