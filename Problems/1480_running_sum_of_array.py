"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-09 16:48:48
 * @modify date 2020-09-09 16:48:48
 * @desc [
     Solution to running sum of array:
        https://leetcode.com/problems/running-sum-of-1d-array/
 ]
 */
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        total = 0
        for num in nums:
            total += num
            sums.append(total)
        return sums