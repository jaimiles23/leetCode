"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-12 14:34:18
 * @modify date 2019-11-12 15:06:02
 * @desc [
     This file compares the run time of the different solutions for 728. Self Dividing Numbers.
 ]
 */
"""
##### Modules
# Standard
import time

# User Created 
import sol_baseNum, sol_stringNumberRatio

##### Test
def func_time(func, repeat = 10 ** 7):
    """
    Returns the time it takes to run the passed function REPEAT times.
    """

    start = time.time()
    for i in range(repeat):
        func
    end = time.time()

    return end - start


def dif_func_times(*args):
    """
    Prints the time required for each function.
    """
    for arg in args:
        print(func_time(arg))


def main():
    dif_func_times(
        sol_stringNumberRatio.test_Solution(),
        sol_baseNum.test_Solution()
    )


if __name__ == "__main__":
    main()

"""
Note to self: Come back and use the timeit module to test the solutions.

"""