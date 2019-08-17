#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    user_input = input('Please input a number: ')
    print(user_input)
    try: 
        user_input = float(user_input)
        if user_input == int(user_input):
            even = user_input % 2 == 0
            if even:
                print('The number is even')
            else:
                print('The number is odd')
        else:
            print('Must input an integer, not a decimal')

    except:
        print('Must input non-word numberals')
    return 


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    count = 1
    for i in range(10):
        row = []
        for j in range(10):
            row.append(count)
            count += 1
        print(row)


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    total = 0
    count = 0
    while True:
        user_input = input('Please input a number: ')
        try:
            user_input = float(user_input)
            total += user_input
            count += 1
        except:
            if user_input == 'done':
                print(total/count)
                break
            else:
                print("Must input a number or done")



##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
