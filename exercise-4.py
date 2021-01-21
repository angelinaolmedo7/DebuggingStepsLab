"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
    # Expected: 4
    # Actual: Recursion Error
# - What error message (if any) is there?
    # Traceback (most recent call last):
    # File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/DebuggingStepsLab/exercise-4.py", line 41, in <module>
    #     answer = binary_search([1, 2, 4, 5, 7], 7)
    # File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/DebuggingStepsLab/exercise-4.py", line 37, in binary_search
    #     return binary_search(arr, element, mid, high)
    # File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/DebuggingStepsLab/exercise-4.py", line 37, in binary_search
    #     return binary_search(arr, element, mid, high)
    # File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/DebuggingStepsLab/exercise-4.py", line 37, in binary_search
    #     return binary_search(arr, element, mid, high)
    # [Previous line repeated 995 more times]
    # File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/DebuggingStepsLab/exercise-4.py", line 22, in binary_search
    #     if high == None:
    # RecursionError: maximum recursion depth exceeded in comparison
# - What line number is causing the error?
    # Technically Line 22, but 37 is more likely to be the problem area. 
# - What can you deduce about the cause of the error?
    # We aren't properly ending our recursion. We should check our base cases.


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
    # The code should catch when low and high have not been specified, and assign them at the ends if not.
    # The code should properly calculate the mid point.
    # The code should return mid if the target is at mid
    # Oh, it looks like the high number is never seached. Let's include a base case for that. We'll put it inside of the if high == None: block so it only happens once.
    # Alright, that worked. Let's add a couple more test cases to be sure.
    # Looks good!


def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1
        if arr[high] == element:
            return high

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid)

    else: 
        return binary_search(arr, element, mid, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)  # 4
    print(answer)
    answer = binary_search([1, 2, 4, 5, 7], 1)  # 0
    print(answer)
    answer = binary_search([1, 2, 4, 5, 7, 7], 7)  # 5
    print(answer)
    answer = binary_search([1, 2, 4, 5, 7], 2)  # 1
    print(answer)
    answer = binary_search([1, 2, 4, 5, 7], 4) # 2
    print(answer)