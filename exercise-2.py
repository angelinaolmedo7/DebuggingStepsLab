"""
Exercise 2
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
    # Expected:
        # False
        # True
    # Actual:
        # False
        # False
# - What error message (if any) is there?
    # No error message
# - What line number is causing the error?
    # No error 
# - What can you deduce about the cause of the error?
    # The error is probably being caused by something in the way we're couting consecutive numbers.


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
    # The last value of i in the loop should be the index two before the last one.
    # The if statement should compare the values at index i, i+1, and i+2.
    # I assume the code should loop through each trio of consecutive numbers. 
    # That's the bug, we're returning false after the first non-consecutive trio rather than waiting until we've gone through all of the trios. 
    # We should remove "else: return False", as only the return false after the loop has completed without returning true is necessary.

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True