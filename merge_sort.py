def merge_sort(list):
    """
    sorts a list in ascending order
    returnds a new sorted list

    1)devide: find the mid point of the list and devide into sublists
    2)conquer: recursivly sort the sublists created in prev step
    3)combine: merge the sorted sublist created in prev step

    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):

    """
    devide teh unsorted list at midpoint into sublist 
    return 2 sublist - left, right
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    merges 2 arrays sorting them in the process 
    returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1


    while j < len(right):
        l.append(right[i])
        j += 1

    return l

alist = [1,2,3,4,5,6,7,8,9]
l = merge_sort(alist)
print(l)




    