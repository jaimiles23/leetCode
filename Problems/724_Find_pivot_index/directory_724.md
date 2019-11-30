# Overview
The probem asks to find the "pivot" of the list, where the sum(left_side) == sum(right_side). The simplest apporach to this problem would be to add to one list an index at a time and compare it to the rest of the list. However, there may be other shortcuts to more quickly determine the pivot index. 

* **binary index search** to determine the pivot index. -- discarded solution.
* **mean index skip** use the mean of the lists to determine the number of indices to skip. For instance, if list1 is > list2 by 20, and the mean of the lists is 10, we would move 2 indices and re-assess.


# Solutions

## sol_binary_index_search
### Description
This solution uses a recursive binary search to determine the index to the pivot index. 

### Steps
1. Define binary search function
2. Recursively call binary search function

### Pros/cons
**Pros**
* Conventional binary search - easily understood
* Avoids unnecessary searching of entire list

### Challenge
I tried to use a binary search algorithm to check for the pivot. However, the inclusion of negative numbers makes it unweidly to determine if you are moving left or right. I ran through about a dozen test cases in order to work out the math. Two example cases:
Starting at index [2], [-1,-1,0,1,0,-1] should move right to [4], [-1,-1,-1,-1,0,1] should move left to [1].  A solution may still be possible, but would require additional development, e.g., looking into the future, and seeing if movement would move closer or further from the desired solution. And then, there may be an issue of calculating -1, -1, … and then not including a 999 within the range

### Lessons
This was the first solution to the problem that I attempted. I brainstormed different ideas, e.g., creating the sum of the list on index at a time, which is an(O(N)) solution time. And I wanted to start with an optimized solution.  
From this challenge, I learned that I am still developing some intuition for developing optimized algorithms, and that I should still start with the simplest solution. While developing the naïve solution, you solidify your understanding of the problem (e.g., negative numbers) and can better judge the merits of other optimized algorithms before investing time developing them.  

## Naive solution
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

### Leetcode diagnostics
Runtime: 144 ms, faster than 99.89% of Python3 online submissions for Find Pivot Index.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find Pivot Index.

This is fairly good runruntime and memory usage (high percentile) -- would like to return and experiment with different algorithms. A different solution (e.g., binay) would third the runtime.

## Thoughts:
Very simple solution - took me ~ 15 minutes to write the algorithm and the documentation. Need to return and look for better solution, e.g., starting in the middle and traveling left and right??

Note: provided solution enumerates the list, which is 2 pass O(N), and completely recalculates right side for each iteration, which adds a slight fraction more than my solution. This adds ~ 35 ms to the submission.

