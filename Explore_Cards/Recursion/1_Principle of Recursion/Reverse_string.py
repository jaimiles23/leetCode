"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-18 20:03:00
 * @modify date 2019-11-18 20:03:00
 * @desc [
print_reverse is the example I developed from the chapter.

reverse_string is the exercise from the next card.

Note: provided solution is s.reverse() - list method.

 ]
 */
"""

def print_reverse(word: str) -> str:
    """ 
    prints a string in reverse
    """
    if len(word) == 1: 
        print(word)
    else:
        print(word[-1], end = '')
        print_reverse(word[:-1])


def test_print_reverse():
    sentence = "I am currently sitting at Panera with Russel Okamura."
    words = sentence.split()

    for word in words:
        print(word)

    for word in words:
        print_reverse(word)


def reverse_string(letters: list) -> None:
    """
    returns the list in reverse by modifying the input inplace with O(1) extra memory (1 variable)
    """
    if len(letters) in (0, 1):  #base case
        return letters

    letters[-1], letters[0] = letters[0], letters[-1]
    letters[1:-1] = reverse_string(letters[1:-1])

    return letters


def test_reverse_string():
    """
    Runs leetCode supplied test case for the reverse_string function
    """
    print('Example 1')
    word = ['h','e','l','l','o']
    output = ['o','l','l','e','h']
    # print(reverse_string(word))
    # print(output)
    assert reverse_string(word) == output


    print('Example 2')
    word = ['H','a','n','n','a','h']
    output = ['h','a','n','n','a','H']
    # print(reverse_string(word))
    # print(output)
    assert reverse_string(word) == output

def reverse_string_recursive_pointers(letters: list) -> None:
    """
    Reverses a list uses recursion and pointers. 

    reverse_string exceeds memory consumption because it continually slices the same list instead of using pointer variables
    """
    def pointer_recursion(letters: list, left: int, right: int):
        """
        Recursive with pointers
        """
        if left < right:
            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1
            pointer_recursion(letters, left, right)
        
    pointer_recursion(letters, 0, len(letters) - 1)
        

def main():
    # test_print_reverse()
    test_reverse_string()


if __name__ == "__main__":
    main()
    pass

