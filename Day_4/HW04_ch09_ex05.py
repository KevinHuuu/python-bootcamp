#!/usr/bin/env python3

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all

# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: favourite
#   - # of words that use all aeiouy: 
##############################################################################
# Imports
from collections import Counter
# Body
def uses_all(word, letter_list):
    """Uses given letters at least once.
    
    Arguments:
        word {str} -- Given word
        letter_list {str} -- The letters  be used.
    
    Returns:
        bool -- Whether uses every letter at least once.
    """
    lookup = Counter(word)
    for char in letter_list:
        if lookup[char] == 0:
            return False
    return True

##############################################################################
def main():
    word = 'favourite'
    letter_list = 'aeiou'
    print(word, letter_list, uses_all(word, letter_list))

if __name__ == '__main__':
    main()
