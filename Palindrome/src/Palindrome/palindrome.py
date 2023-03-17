def is_palindrome(word):
    """
    Check if a word is a palindrome.
    """
    word = word.lower() # convert to lowercase
    reversed_word = word[::-1] # reverse the word
    return word == reversed_word
