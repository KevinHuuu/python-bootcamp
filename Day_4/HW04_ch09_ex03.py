#!/usr/bin/env python3

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word, forbid_letters):
    for char in word:
        if char in forbid_letters:
            return False
    return True


def forbidden_prompt(l_word):
    forbid_letters = input('enter forbidden letters')
    for word in l_word:
        flag = False
        for char in word:
            if char in forbid_letters:
                flag = True
        if flag == False:
            print('{} does not contain any letter in {}'.format(word, forbid_letters))


def forbidden_param(l_word, forbid_letters):
    for word in l_word:
        flag = False
        for char in word:
            if char in forbid_letters:
                flag = True
        if flag == False:
            print('{} does not contain any letter in {}'.format(word, forbid_letters))

def find_five(l_word):
    from collections import Counter
    total_char = ''.join(l_word)
    lookup = Counter(total_char)
    
    five_letters = list(zip(*sorted(lookup.items(), key=lambda x:x[1])[:5]))[0]
    print(five_letters)
    for word in l_word:
        flag = False
        for char in word:
            if char in five_letters:
                flag = True
        if flag:
            print(word, ' is excluded by ', five_letters)



##############################################################################
def main():
    find_five(['apple', 'banana', 'peach', 'watermelon', 'jake', 'hose'])


if __name__ == '__main__':
    main()
