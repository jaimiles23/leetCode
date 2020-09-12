"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-12 10:04:45
 * @modify date 2020-09-12 10:04:45
 * @desc [
    Solution to1108. Defanging an email address:
https://leetcode.com/problems/defanging-an-ip-address/

NOTE:
    - Not using .replace()
    - Python strings are immutable
    - create list of characters
    - check char
    - join list
 ]
 */
 """

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = [char for char in address]
        for i in range(len(address)):
            if address[i] == '.':
                address[i] = '[.]'
        return ''.join(address)