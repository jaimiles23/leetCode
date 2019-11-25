# Space Complexity - Recursion

There are two main parts of the space consumption to bear in mind:
1. Recursion related space
2. non-Recursion related space

## Recursion related space
This refers to the space that is incurred directly by the recursion, i.e., the stack to keep track of recursive function calls. TO do this, the system allocates space in the stack to hold 3 pieces of information. The:
1. **returning address** of the function call, to know where to return to after the function call.
2. **parameters** that are passed to the function.
3. **local variables** within the function call.

The space in the stack is the minimal cost that is incurred during a function call. Once the function call is completed, the space is freed.

For recursive algorithsms, the function calls chain successively until the _base case_ is reached. Thus, the space for each function call is accumulated. If there is _no other memory consumption_, the recursion incurred space will be the space upper-bound of the algorithm.

In the exercise [printReverse](https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1439/), no extra memory is used outside the function call since the character is only printed. 

If each recursive call uses space up to a constant value, and the recursive call chains up to `n` times, where `n` is the size of the input string, then the space complexity of the recursive algorithm is O(n). 

Illustration of recursive function call available [here](https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/1671/)


It is due to recursion-related space consumption that one runs into a [stack overflow](https://en.wikipedia.org/wiki/Stack_overflow). This happens when the stack allocated for the program reaches its maximum space limit and the program creashes. When designing a recursive algorithm, check for stack overflow as input scales.

## non-Recursion related space
This refers to the memory space not directly related to recursion. This may include storing input as global variables before other function calls, or intermediate results from the recursive calls, i.e., **memoization**. 