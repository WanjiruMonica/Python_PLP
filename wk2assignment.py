# creating an empty list
my_list = []

# appending vlues 10, 20, 30 and 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# appending value 15 to the second position
my_list.insert(1, 15)

# extending the list with values 50, 60, and 70
my_list.extend([50, 60, 70])

# removing the last element from the list
del my_list[-1]

# sorting the list in ascending order
my_list.sort()

# sorting the list in descending order
my_list.sort(reverse=True)

print(my_list.index(30))
