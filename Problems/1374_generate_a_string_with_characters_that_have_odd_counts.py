"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-12 10:12:14
 * @modify date 2020-09-12 10:12:14
 * @desc [
    Solution to: 1374. Generate a String With Characters That Have Odd Counts
    https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

    NOTE:
    - Divmod to find quotient and remainder. 
    - if even number, one fewer n 'a' and add a 'b'
 ]
 */
"""

## General logic solution
class Solution:
    def generateTheString(self, n: int) -> str:

        _, r = divmod(n, 2)
        if r:
            output = n * chr(97)
        if not r:
            output = (n - 1) * chr(97) + chr(98)
        return output


## 1 line solution
class Solution:
    def generateTheString(self, n: int) -> str:
        return n * 'a' if n % 2 else (n-1) * 'a' + 'b'
        