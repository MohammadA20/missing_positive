"""
    This program will replace the negative number
    with the missing sequence of the list
"""

def first_missing_positive(numbers):
    """
        Like if we have 1,2,3,-7,5 the output will 4
        will replace -7
    """
    numbers.sort()
    missing_number = 1
    for positive in numbers:
        if positive == missing_number:
            missing_number += 1
        elif positive > missing_number:
            break
        return missing_number
MISSING_NUMBER_FOUND = first_missing_positive([1,2,4,5,6])
print(MISSING_NUMBER_FOUND)
