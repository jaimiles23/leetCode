"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2019-11-18 20:03:00
 * @modify date 2019-11-18 20:03:00
 * @desc [
print_reverse is the example I developed from the chapter.

reverse_string is the exercise from the next card.
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
    
    pass

def test_reverse_string():
    """
    Runs leetCode supplied test cases for the function
    """
    print('Example 1')
    word = ["h","e","l","l","o"]
    output = ["o","l","l","e","h"]
    assert reverse_string(word) == output


    print('Example 2')
    word = ["H","a","n","n","a","h"]
    output = ["h","a","n","n","a","H"]
    assert reverse_string(word) == output


def main():
    # test_print_reverse()
    test_reverse_string()


if __name__ == "__main__":
    main()
    pass






