#!/usr/bin/env python3
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.


###############################################################################
# Body


def any_lowercase1(s):
    """only check the first char in the given s.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """ 'c' is an actual char, not a variable representing the char in s.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """the flag will be covered, can only test whther the last char is lowercase or not.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """this one is correct. test whether a lowercase occured.
    """
    flag = False
    for c in s:
        if c.islower():
            flag = True
        # flag = (flag or c.islower())
    return flag


def any_lowercase5(s):
    """test whether there is an uppercase char occured, not lowercase.
    """
    for c in s:
        if not c.islower():
            return False
    return True

###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print(any_lowercase1("DtO"))
    print(any_lowercase2("D0"))
    print(any_lowercase3("tO"))
    # print(any_lowercase4("tO"))
    print(any_lowercase5("tO"))

if __name__ == '__main__':
    main()
