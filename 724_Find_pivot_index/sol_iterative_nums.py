"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-18 15:46:11
 * @modify date 2019-11-18 16:01:36
 * @desc [
### Description
This solution adds one index at a time and compares it to the remainder of the list.

### Steps
1. Find the total sum of the list. This will be list 1
2. Instantiate list2
3. For each item in the list
   1. Pivot = index
   2. Remove pivot value from list 1
   3. If list1 == list2: return pivot
   4. else list2.append(pivot)
4. return -1

### Time complexity
O(N) because the solution cycles through the entire list once.

####
 ]
 */
"""
## Modules
import unit_tests_724 as ut

class Solution():
    def pivotIndex(self, nums: list) -> int:
        """
        returns pivot index by iterating through the list
        """
        right_side = sum(nums)
        left_side = 0

        for i in range(len(nums)):
            right_side -= nums[i]

            if left_side == right_side:
                return i
            
            left_side += nums[i]
        
        return -1

def main():
    tester = Solution()
    ut.unit_tests(tester.pivotIndex)


if __name__ == "__main__":
    main()