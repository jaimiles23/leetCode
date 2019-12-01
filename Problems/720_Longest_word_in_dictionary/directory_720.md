/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-13 16:41:20
 * @modify date 2019-11-14 12:59:43
 * @desc [description]
 */

# Overview
This problem asks to find the longest word that can be built by other existing words, excluding the last character. I refer to the words that build other words as "building blocks".

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
* **sol_iterative_improved**: optimizes the sol_iterative by using separate lists for each word length
* **sol_recursive**: sorts the list and uses recursion to check each element in the list

# Solutions

## sol_iterative

### Description
This solution iterates through each item of the list in reverse. Each word is then shortened until it reaches len(1), or the modified word no longer exists in the words list and is thus disqualified for longest word in dictionary.

### Steps
1. Sort list smallest -> largest, then z -> a
2. Check each word, starting at the end of the list
   1. Shorten the word by 1.
   2. Check that the new word is in the list. If not, next word
   3. If len(new_word) == 1: return
   4. Repeat
3. If no new words are found, return an empty string.

### Pros and Cons
**Pros**

- Simple implementation, essentially 2 step methods
- Fast - competes with other solutions, e.g., the suggested hash solution

**Cons**
- Efficiency can still be improved

### Performance
**Leetcode diagnostics**
Runtime: 68 ms, faster than 99.66% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.

### Thoughts: 
What is important about this solution is the memory usage. To get this speed, online solutions use a set which requires much more memory. This solution has equivalent speeds, while minimizing memory consumption. 

## sol_iterative_improved
### Description
This solution optimizes the idea taken from sol_iterative via creating different lists for each word length. All words of length 1 are placed into a list, all words of length 2 into a different list, etc. When checking each word for its building blocks, only the list of the word length - 1 is checked. This reduces the number of words in each loop.

### Steps
1. Create list of lists for different word lengths
2. Place words into list by word length
3. For each list:  
   1. If the list is empty, delete it and all subsequent lists (no adequate building blocks for those words)
   2. Sort the list alphabetically
4. Check each word, starting with the longest, lexographically smallest word
   1. Shorten the word by 1
   2. Check that the new word is in the list of words of len(new_word).  If not, next word
   3. If len(new_word) == 1: return word
   4. Repeat
5. If no words, return empty string

### Pros and cons
**Pros**
- Fastest solution.
- List instead of hash decreases memory consumption

**Cons**
- Complex implementation. But offset by function efficiency.

### Performance
**Leetcode diagnostics**
Leetcode diagnostics:
Runtime: 60 ms, faster than 100.00% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.

### Thoughts
This solution does not have substantial performance differences than the previous iterative solution. Both perform in the 99%ile.
The difference is that this algorithm has a marginally lower min runtime and memory usage than the previous solution.

This highlights the importance of functionality over optimization. Either solution will perform well, and the difference of ~ 20 MS is an optimization that 
can be implemented later.
