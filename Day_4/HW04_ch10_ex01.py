# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Example of nested list: [1, 2, [3]]
#
# I will be calling things like this: nested_sum([[1, 2], [3], [4, 5, 6]])
# I will be expected that to return, in this case, 21

# Verify you've tested w/ various nestings (perhaps by writing a test function
# like in the string exercises from Google (string1.py and string2.py))
#
# In your final submission:
#  - Do not print anything extraneous.
#  - Do not put anything but pass in main()

def nested_sum(alist):
    new_list = []
    for i in alist:
        if not isinstance(i, int):
            new_list.append(nested_sum(i))
        else:
            new_list.append(i)
    return sum(new_list)

if __name__ == "__main__":
    pass