"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-12 12:58:24
 * @modify date 2019-11-12 13:20:52
 * @desc [

_String number 1:1 ratio_
In a decimal system, each digit is represented by a single string character, [0-9]. You may utilize this property to identify digits to check if the input number is self dividing.

### Steps
1. Transform the input number into a string. Each character of this string can then be considered a 'digit'.
2. Divide the integer version of the input number by each 'digit' of the string input number.
3. If the input number is divisible by all of its digits, it is a self dividing number.

### Pros_Cons
**Pros**
- Method is simple and easy to understand.
**Cons**
- Relies on each number being represented by a single string. Thus, this solution cannot be generalized to a system which uses multiple characters to represent numbers.]
 */
"""

## String number 1:1 ratio

class Solution():
    def selfDividingNumbers(self, left: int, right: int) -> list:
        """
        Purpose: Implements the string-number 1:1 ratio approach to access digits
        """

        self_dividing_nums = []

        for num in range(left, right + 1):
            flag_self_divide = True

            for digit in str(num):
                if int(digit) == 0:
                    flag_self_divide = False
                    break

                elif num % int(digit) != 0:
                    flag_self_divide = False
                    break

            if flag_self_divide:
                self_dividing_nums.append(num)
        
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

