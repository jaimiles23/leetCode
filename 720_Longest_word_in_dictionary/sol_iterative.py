"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-13 18:53:39
 * @modify date 2019-11-13 19:12:38
 * @desc [
     Iterative solution to #720 Longest Word in Dictionary

Runtime: 68 ms, faster than 99.66% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.

Note: What is important about this solution is the memory usage.  
To get this speed, online solutions use a set which requires much more memory. This solution has equivalent speeds, while minimizing memory consumption. 
 ]
 */
 """
 
## Iterative solution

class Solution():
    def longestWord(self, words: list) -> str:
        """
        Iterates to find the longest word in the list of words
        """
        ## TODO: Sort the list length and alphabetically
        words.sort(key = lambda x: (-len(x), x), reverse= True)
        ##TODO:
        """
        Come back and consider more efficient ways:
        - Create a list of lists. list[0] will contain words of len 1, list[1] will contain words of len 2.  Then, only check the appropriate list for 
        the words.

        This will reduce the number of words checked.  the list of words can be < len(1000)
        """
        ## TODO: Iterate through list backwards
        for word in reversed(words):
            check_word = word
            flag_check_word = True

            while flag_check_word and len(check_word) != 1:
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
