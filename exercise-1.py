"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
    # Expected: 
    #     4
    # Actual: Error

# - What error message (if any) is there?
    # Traceback (most recent call last):
    #     File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/exercise-1.py", line 35, in <module>
    # answer = find_largest_diff([5, 3, 1, 2, 6, 4])
    #     File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/exercise-1.py", line 27, in find_largest_diff
    # diff = abs(list_of_nums[i] - list_of_nums[i+1])
    # IndexError: list index out of range

# - What line number is causing the error?
    # Line 27

# - What can you deduce about the cause of the error?
    # We're trying to retrieve an index outside of the length of the list


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
    # The first thing we do is set the largest difference variable to 0. 
    # If the code were functional, I assume this value would be changed unless all the numbers were identical. 
    # I assume the code should loop through each pair of consecutive numbers. 
    # This should stop with the pair of numbers at the last and second-to-last number.
    # That's the issue, it goes one index too far. I'll fix this by changing the range to include -1

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums) -1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)