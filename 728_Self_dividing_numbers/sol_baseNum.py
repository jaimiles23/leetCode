"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-12 13:23:53
 * @modify date 2019-11-12 13:44:11
 * @desc [

_Base number system_
A decimal system uses base 10 to represent digits. Dividing by the base number results in the next 'digit' that the number contains. 
This method can be used to access the digits of the input number, and then check if the input is self dividing

### Steps
1. Divide the input number by 10 and find the remainder. This remainder is the far left digit of the number.
2. Divide the original input number by the remainder. If the answer is not 0, then the number is not self-dividing.
3. Repeat steps 1 and 2 until all digits have been tested.

### Pros_Cons
**Pros**
- This method can be generalized to other base X systems, e.g., base 2, base 3, etc.
**Cons**
- Harder to implement/understand
 ]
 */
"""

## Base number system

class Solution():
    def selfDividingNumbers(self, left: int, right: int) -> list:
        """
        Purpose: Implements the base number system to access digits
        """
        self_dividing_nums = []

        for num in range(left, right + 1):
            self_dividing_num = num
            flag_self_dividing = True

            while num > 0:
                digit, num = num % 10, num // 10

                if digit == 0:
                    flag_self_dividing = False
                    num = float('-inf')
                
                elif self_dividing_num % digit != 0:
                    flag_self_dividing = False
                    num = float('-inf')
            
            if flag_self_dividing:
                self_dividing_nums.append(self_dividing_num)
            
        return self_dividing_nums


def test_Solution():
    tester = Solution()
    left = 1
    right = 22
    output =[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert tester.selfDividingNumbers(left, right) == output


def main():
    test_Solution()


if __name__ == "__main__":
    main()




            






