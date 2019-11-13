/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-12 13:48:06
 * @modify date 2019-11-13 13:01:50
 * @desc [description]
 */

# Overview
The main challenge to test a self dividing number is to identify the digits.

I have found 2 solutions to determine the digits [728: Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/submissions/)

* **sol_stringNumber_ratio**: converts the number into a string and uses each character of the string as a digit.
* **sol_baseNum**: divides the input number by the base number to acquire each digit.

For each solution, this file documents the:
* _Description_
* _Steps_
* _Pros/Cons_

# Solutions

## sol_stringNumber_ratio
### Description
_String number 1:1 ratio_

In a decimal system, each digit is represented by a single string character, [0-9]. This solution utilizes this property to identify the digits to check if the input number is self dividing.

### Steps
1. Transform the input number into a string. Each character of this string can be considered a 'digit'.
2. Divide the original input number by each 'digit' of the string input number.
3. If the input number is divisible by all of its digits, it is a self dividing number. If it is not, it is not a self dividing number.

### Pros_Cons
**Pros**
- Method is simple and easy to understand.

**Cons**
- Relies on each number being represented by a single string. This solution may not be generalizable to a system which uses multiple characters to represent numbers.

## sol_baseNum
_Base X number system_

A decimal system uses base 10 to represent digits. This solution continually divides the base number by 10 to locate the next 'digit'.

### Steps
1. Divide the input number by 10 and find the remainder. This remainder is the far right digit of the number.
2. Divide the original input number by the remainder. If the answer is not 0, then the number is not self-dividing.
3. Repeat steps 1 and 2 until all digits have been tested.

### Pros_Cons
**Pros**
- This method can be generalized to other base X systems, e.g., base 2, base 3, etc.

**Cons**
- Harder to implement/understand


# Conclusion
Each solution has merits and should be implemented into a system depending on its intended functionality. I would default to using the **string number 1:1 ratio** solution because of its ease of implementation and understanding. A fundamental principle of system design is accessibility - a system should be designed to be as  accessible to other collaborators as possible; one key component of accessibility is simplicity. A more complex system, for instance one gated behind potentially non-intuitive math, limits the number of potential collaborators and the effort spent into system maintenance. 

Yet there are cases to implement the **base X number solution**. The scalability of this solution is a boon; implement this solution if the system may eventually require different inputs, e.g., binary. Implementation of this solution may help reduce the labor required to expand the system.