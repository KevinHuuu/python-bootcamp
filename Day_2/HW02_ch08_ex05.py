# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.
# Please write a docstring for every function you write.

def rotate_word(s, num):
    """return the rotated word by num.
    
    Arguments:
        s {str} -- the given string
        num {int} -- the num of steps to rotate
    
    Returns:
        str -- rotated string.
    """
    new_s = ''
    for i in s:
        new_s = new_s + chr(ord(i) + num)
    return new_s

if __name__ == "__main__":
    print('The rotation of changran is:')
    for i in range(25):
        print(rotate_word('changran', i))