# List is a mutable datatype - you can add,update,delete in list
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

# Append any element in list
# list1.append(6)
# print(list1)

# Remove any element from list
# list1.remove(5)
# print(list1)

# Count any element from list
# print(list1.count(3))

# Get index of any element 
# print(list1.index(3))

# Add new list in existing list
# list1.extend(list2)
# print(list1)

# Insert element at specific index
# list1.insert(2,2.5) # index,value
# print(list1)

# Remove element from list if you not give any value it will remove last value from list
# list1.pop()
# print(list1)

# Reverse the list 
# list1.reverse()
# print(list1)


# List Comprehension 
# listcomp = [i for i in range(11)]
# print(listcomp)

# List Comprehension for even number
listcomp = [i for i in range(11) if i % 2 == 0]
print(listcomp)