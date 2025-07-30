new_list = [1,2,3]


print("value: ", new_list[2])


for n in new_list:
    if n == 2:
        print(True)

numbers = []
print(len(numbers))

numbers.append(3)
numbers.append(200)
print(len(numbers))

numbers.extend([4,5,6])
print(len(numbers))

numbers.extend(new_list)

for i in range(len(numbers)):
    print( "index: ",i, "value: ", numbers [i])

