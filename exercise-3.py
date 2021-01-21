"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
    # Expected:
        # [1,2,3,5,6]
    # Actual:
        # Error
# - What error message (if any) is there?
    # Traceback (most recent call last):
    # File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/exercise-3.py", line 37, in <module>
    #     answer = insertion_sort([5, 2, 3, 1, 6])
    # File "/Users/angelinaolmedo/term8/SPD-2.3-Debugging-Steps-Lab-main/exercise-3.py", line 29, in insertion_sort
    #     while key < arr[j] : 
    # IndexError: list index out of range
# - What line number is causing the error?
    # Line 29
# - What can you deduce about the cause of the error?
    # j is greater than the length of the list or less than 0


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
    # The for loop runs once for each item in the array except the first value.
    # "key" is set to the value at index i
    # j should not go out of range. Clearly, per the error message, it does. Let's add a couple print statements so we can keep track of j.
    # That didn't help much. Let's instead track the comparison in the line that gives us the issue.
    # Okay, I see. j should not be allowed to become less than 0. The code is then parsed as the index that far from the end.
    # We'll add another comparison to the while statement: j >= 0
    # Yep, that seems to have fixed it.
    # Comment out the print statements we made.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        # print(j)
        # print(str(key) + ", " + str(arr[j]))
        while j >= 0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
            # print(j)
            # print(str(key) + ", " + str(arr[j]))
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

