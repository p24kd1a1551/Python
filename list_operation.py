# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Slicing the list
print("Sliced List (index 1 to 3):", my_list[1:4])

# Adding elements
my_list.append(60)
my_list.insert(2, 25)
print("List after adding elements:", my_list)

# Deleting elements
del my_list[3]      # delete by index
my_list.remove(25)  # delete by value
print("List after deleting elements:", my_list)