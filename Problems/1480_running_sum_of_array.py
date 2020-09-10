"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-09 16:48:48
 * @modify date 2020-09-09 16:48:48
 * @desc [
     Solution to running sum of array:
        https://leetcode.com/problems/running-sum-of-1d-array/

Solution 1 - simple for loop iterating over list
    - Runtime: 40, 44 ms
    - Memory: 13.9, 14 MB

Solution 2 - Generator function to yield results
    - Runtime: 36, 40 ms
    - Memory: 14.1, 14.2 MB

Notes:
- both solutions have a time complexity of O(N).

 ]
 */
"""
## Solution 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        total = 0
        for num in nums:
            total += num
            sums.append(total)
        return sums

## Solution 2
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        def get_sums(nums):
            """
            Aux generator func to return num
            """
            total, n = 0, 0
            while n < len(nums):
                total += nums[n]
                yield total
                n += 1
        return [n for n in get_sums(nums)]
