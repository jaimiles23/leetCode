/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-12 13:48:06
 * @modify date 2019-11-12 14:30:14
 * @desc [description]
 */

# Overview
I have tested 2 solutions to [problem 728](https://leetcode.com/problems/self-dividing-numbers/submissions/)

* sol_stringNumber_ratio
* sol_baseNum

For each solution, this file provides general:
* descriptions
* steps
* pros/cons


# Solutions

## sol_stringNumber_ratio
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
- Relies on each number being represented by a single string. Thus, this solution cannot be generalized to a system which uses multiple characters to represent numbers.

## sol_baseNum
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


# Conclusion
Each solution has merits and may be implemented into a system depending on its intended functionality. I would default to using the **String Number 1:1 ratio** solution because of its ease of implementation and understanding. A fundamental principle of system design is accessibility - a system should be designed to be as simple, and thus accessible to other collaborators, as possible. As more self-taught, non-formally educated coders such as myself begin to collaborate, it's important to keep systems accessible to the largest common denominator. A more complex system, for instance one gated behind potentially non-intuitive math, limits the number of potential collaborators and the effort spent into system maintenance. 

Yet there are cases to implement the **Base X Number Solution**. The scalability of this solution is a boon; if the system may eventually require different inputs, e.g., binary, this solution should be implemented. Implementation of this solution may help reduce the labor required to expand the system.

