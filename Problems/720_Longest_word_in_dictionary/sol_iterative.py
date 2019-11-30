"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-13 18:53:39
 * @modify date 2019-11-14 12:18:54
 * @desc [
Iterative solution to #720 Longest Word in Dictionary

Leetcode diagnostics
Runtime: 68 ms, faster than 99.66% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.

Notes: 
What is important about this solution is the memory usage.  
To get this speed, online solutions use a set which requires much more memory. This solution has equivalent speeds, while minimizing memory consumption. 
 ]
 */
 """
 
## Iterative solution

class Solution():
    def longestWord(self, words: list) -> str:
        """
        Iterates to find the longest word that can be built from other list elements
        """
        ## Sort the list length and alphabetically
        words.sort(key = lambda x: (-len(x), x), reverse = True)

        ## Iterate through the list largest -> smallest, then z -> a
        for word in reversed(words):
            check_word = word
            flag_check_word = True

            while flag_check_word and len(check_word) != 1:
                ## Note: the and conditional checks the len(check_word) every iteration. 
                #  This is improved to be checked only once in the improved iterative solution
                check_word = check_word[:-1]
                if check_word not in words:
                    flag_check_word = False
            
            if flag_check_word:
                return word

        return ""


def test_solution():
    tester = Solution()

    print(1 * '#', 'test 1')
    words = ["w","wo","wor","worl", "world"]
    output = "world"
    assert tester.longestWord(words) == output

    print(1 * '#', 'test 2')
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    output = "apple"

    assert tester.longestWord(words) == output


def main():
    test_solution()


if __name__ == "__main__":
    main()
