#!/usr/bin/env python

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - manually type favorite sentence(s) here:
#       1: hello face
#       2: face of he
#       3: cafe coffee
##############################################################################
# Imports

# Body
def uses_only(word, letter_list):
    """Uses only given letters.
    
    Arguments:
        word {str} -- Given word.
        letter_list {str} -- The letters can be used.
    
    Returns:
        bool -- Whether only uses given letters.
    """
    for char in word:
        if char not in letter_list:
            return False
    return True


##############################################################################
def main():
    word = 'helloface'
    letter_list = 'acefhlo'
    print(word, letter_list, uses_only(word, letter_list))


if __name__ == '__main__':
    main()
