"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-10 16:58:33
 * @modify date 2020-09-10 16:58:33
 * @desc [
    Solution to https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

    Uses generator function here: 
    NOTE: No benefit from generator since all items must be generated before processing answer.
 ]
 */
"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        def get_can_distribute(candies, extraCandies):
            for kid in candies:
                yield kid + extraCandies >= max(candies)
        
        return list(get_can_distribute(candies, extraCandies))
