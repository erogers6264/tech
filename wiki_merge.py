import random

def merge(left, right):
    result = []
    
    while left and right:
        if left[0] <= right[0]:
            print("Left was smaller:", left[0])
            result.append(left[0])
            left = left[1:]
        else:
            print("Right was smaller:", right[0])
            result.append(right[0])
            right = right[1:]
    
    # Either left or right may have elements left; consume them.
    # (Only one of the following loops will actually be entered.)
    
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]
    return result


def merge_sort(a_list):
    # Base case. A list of zero or one elements is sorted, by definition.
    if len(a_list) <= 1:
        return a_list
        
    # Recursive case. First, divide the list into equal-sized
    # sublists consisting of the first half and second half of
    # the list. Lists start at index 0.
    left = []
    right = []
    for index, x in enumerate(a_list):
        if index < len(a_list)/2:
            left.append(x)
        else:
            right.append(x)
    
    # Recursively sort both sublists.
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Then merge the now-sorted sublists.
    return merge(left, right)
    
a = random.sample(range(1, 10009), 9999)
print a
print(merge_sort(a))