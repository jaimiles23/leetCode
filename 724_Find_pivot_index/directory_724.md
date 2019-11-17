# Overview
The probem asks to find the "pivot" of the list, where the sum(left_side) == sum(right_side). The simplest apporach to this problem would be to slowly add to one list and compare it to the other. However, there may be other shortcuts to more quickly determine the pivot index. 

* **binary index search** to determine the pivot index. 
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

### Thoughts


