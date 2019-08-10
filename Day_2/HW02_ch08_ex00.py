#!/usr/bin/env python3
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

# Please write a docstring for every function you write.

###############################################################################
# Imports


# Body
def count(word, char):
    """count a perticular char in a word.
    
    Arguments:
        word {str} -- a word.
        char {[type]} -- a letter to be counted.
    """
    count = 0
    for letter in word:
        if letter == char:
            count = count + 1
    print(count)

###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count('banana', 'a')
    count('banana and apple', 'p')


if __name__ == '__main__':
    main()
