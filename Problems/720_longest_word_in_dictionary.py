"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-13 19:57:57
 * @modify date 2019-11-14 11:00:25
 * @desc [
Iterative solution to #720 Longest Word in Dictionary. This solution uses a list of list to speed when checking for building words


Leetcode diagnostics:
Runtime: 60 ms, faster than 100.00% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.

Notes:
This solution does not have substantial performance differences than the previous iterative solution. Both perform in the 99%ile.
The difference is that this algorithm has a marginally lower min runtime and memory usage than the previous solution.

This highlights the importance of functionality over optimization. Either solution will perform well, and the difference of ~ 20 MS is an optimization that 
can be implemented later.
 ]
 */
"""

class Solution():
    def longestWord(self, words: list) -> str:
        """
        Returns longest word in the list that can be built from other list elements.
        Note: uses list of lists.
        """
        ## Create lists for different word lengths
        max_length = len(max(words, key = lambda x: len(x)))
        w_lists = [[] for _ in range(max_length)]
        
        ## Assign words to list based on length
        for word in words:
            w_lists[len(word) - 1].append(word)
        
        ## remove unnecessary lists and sort each list reverse alphabetically
        for i in range(len(w_lists)):
            if len(w_lists[i]) == 0:
                w_lists = w_lists[0:i]
                break
            w_lists[i].sort(reverse = True)
        
        ## Check if words can be built

        ## Start with longest list
        for i in range(len(w_lists) - 1, -1, -1):
            ## Check lexographically smallest words first
            for j in range(len(w_lists[i]) - 1, -1, -1):
                word = w_lists[i][j]
                change_wlist = 0
                flag_check_word = True

                while flag_check_word:
                    change_wlist += 1
                    word = word[:-1]

                    if word not in w_lists[i - change_wlist]:
                        flag_check_word = False
                
                if i - change_wlist == - 1:
                    return w_lists[i][j]
        
        return ""


def test_solution():
    tester = Solution()

    print(1 * '#', 'test 1')
    words = ["w","wo","wor","worl", "world"]
    output = "world"
    assert tester.longestWord(words) == output
    
    print(1 * '#', 'test 2')
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple", "aaaaaaaa", "zanana", "yanana"]
    output = "apple"
    assert tester.longestWord(words) == output

    print(1 * '#', 'test 3')
    words = ["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]
    output = "e"
    assert tester.longestWord(words) == output
    """
    Failed 3rd test in implementation because return logic was in end of while loop. Note to self: pay attention to this. 
    """


def main():
    test_solution()


if __name__ == "__main__":
    main()
