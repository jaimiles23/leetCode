'''
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-01-29 10:38:19
 * @modify date 2020-01-29 10:38:19
 * @desc [
Per definition, a happy number is derived through brute force calculuations. These calculations only stop when the number is caught in an infinite loop, 
i.e., the numbers are repeating each other.  This is an iterative brute force solution to determine the number
 
Results:
Runtime: 28 ms, faster than 87.55% of Python3 online submissions for Happy Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Happy Number.

Complexity analysis:
Time complexity:
O(N**2) - for loop embedded in a while loop. NOTE: per definition, I don't think you can be faster than O(N**2)
Space complexity:
O(N) - Store O(N) elements in set searched_nums, and O(1) elements for num, next_num, and searching flag.
 ]
 */
'''

class IterativeSolution:
    def isHappy(self, n: int) -> bool:
        # instantiate vars and flag
        num, next_num = n, 0
        searched_nums = {n}
        searching_happy = True
        
        while searching_happy:
            
            # Construct next_num
            for char in str(num):
                next_num += int(char) ** 2
            
            # Check Happy
            if str(next_num) == '1': 
                return True
            
            # Check if already checked
            elif next_num in searched_nums:
                searching_happy = False
            
            # Reset vars for next check
            else:
                num, next_num = next_num, 0
                searched_nums.add(num)
        
        return False