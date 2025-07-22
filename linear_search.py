def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None  

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