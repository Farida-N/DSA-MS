<<<<<<< HEAD
def linear_search(list, target):
    for i in range(0, len(list)):
        if i is target:
            return i
        else:
            print("Error")
=======
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None  
>>>>>>> ccc126fc075967845525de2407e56241d538949d

<<<<<<< HEAD
def verify(index):
    if index is None:
        print("target not found")

num = [1,2,3,4,5,6,7,8,9]
result = linear_search(num, 3);


=======
def verify(index):
    if index is None:
        print("target not found")
    else:
            print("found at index: ", index)

num = [1,2,3,4,5,6,7,8,9]
result = linear_search(num, 3)
verify(result)

result = linear_search(num, 11)
verify(result)
>>>>>>> ccc126fc075967845525de2407e56241d538949d