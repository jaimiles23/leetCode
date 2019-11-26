# Tail recursion
**Tail recursion** is a special case that is exempted from space overhead. Tail recursion is where the recursive call is the final instruction in the recursion function. There should only be _one_ recursive call in the function.

Observe the following code:

```
def sum_non_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list
    """
    if len(ls) == 0:
        return 0
    
    # not a tail reucrsion because it does some computation after the recursive call is returned.
    return ls[0] + sum_non_tail_recursion(ls[1:])

def sum_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list
    """
    def helper(ls, acc):
        if len(ls) == 0:
            return acc
        # this is a tail recursion because the final instruction is a recursive call
        return helper(ls[1:], ls[0] + acc)
    
    return helper(ls, 0)
```

The benefit of a **tail recursion** is taht it can avoid the accumulation of stack overheads during the recursive call, since the system can reuse a fixed amount of space for each recursive call. Because tail recursions ned in a recursive call, we know that we will immediately return each recursion. Thus, we can return straight to the original function and not use a call stack for recursive calls. This will save stack space. 

If f(3) -> f(2) -> f(1), since each recursion only changes the parameters of the other recursion, we can return f(1) directly to f(3) and avoid the entire call stack.

A tail recursion can be executed as non-tail recursion functions, i.e., with piles of call stacks.  This will not have impact on the result, however a compiler will recognize tail recursion patterns and optimize the execution. However, not all languages support tail recursion optimization, e.g., Java and Python -- self note: i believe this is because they are interpreted languages.