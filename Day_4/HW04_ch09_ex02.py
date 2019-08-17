#!/usr/bin/env python3

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
def has_no_e(s):
    """Judge whether the string has letter e.
    
    Arguments:
        s {str} -- A string.
    
    Returns:
        bool -- Whether the giben string has no e.
    """
    return 'e' not in s 
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list that have no "e".
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def print_no_e(l):
    """Print no e word and calculate its percentage.
    
    Arguments:
        {[]str} -- A list of words.
    """
    no_e = 0
    for word in l:
        if has_no_e(word):
            print(word)
            no_e += 1
    print('No e words percentage is {0:.2f}%. '.format(100 *no_e/len(l)))



##############################################################################
def main():
    print_no_e(['apple', 'banana', 'pineapple'])


if __name__ == '__main__':
    main()
