#!/usr/bin/env python3
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

# Here is an opportunity to use things like `try`, `except`, and/or `finally`.

# Please write a docstring for every function you write.

###############################################################################
# Imports
import math

# Body
def eval_loop():
    """return a math result with a given python string formula.
    """
    while(True):
        print('please input a expression')
        input_v = input()
        if input_v == 'done':
            try:
                print('last expression calculated is: ', res)
                break
            except:
                print('No previous expression evaluated! ')
                break
        else:
            res = input_v
            try:
                print(eval(input_v))
            except:
                print('Illegal input！')


###############################################################################
def main():
    eval_loop()


if __name__ == '__main__':
    main()
