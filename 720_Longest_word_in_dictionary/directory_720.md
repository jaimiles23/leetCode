/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-13 16:41:20
 * @modify date 2019-11-13 16:41:20
 * @desc [description]
 */

# Overview
This problem asks to find the longest word that can be built by other existing words, excluding the last character. 

I find 2 immediate approaches: 
* **Recursive** start with the longest word and splice off the last character. If len() != 1, check that the splice is in the words list.
* **Iterative** Start with the longest word, splice the last character, and see if in list. Use a while statement to continue until len() == 1.

Example 2 illuminates two test characteristics that will be important to pass the test cases.
1. The words list will not necessarily be sorted by length.
2. The returned word must be the lexicographically smallest.

Regardless of the solution implemented, the first step will be to apply a 2-layer sort to the list:
1. Length, smallest -> largest
2. Alphabetically, Z-> A

This sort will allow the selected algorithm to begin with the longest and lexigraphically smaller test cases. Thus, when a solution is found it will immediately be returned.

For this problem, I found x solutions:
* **sol_iterative**: sorts the list and runs through each element of the list iteratively
* **sol_recursive**: sorts the list and uses recursion to check each element in the list

## Solutions
