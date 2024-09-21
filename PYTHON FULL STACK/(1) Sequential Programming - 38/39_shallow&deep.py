import copy

# A shallow copy creates a new list but does not create new objects for the elements inside the list

original_list = [1, [2, 3], [4, 5]]

# Creating a shallow copy
shallow_copy_list = copy.copy(original_list)

# Modifying the shallow copy
shallow_copy_list[1][0] = 'X'

# Printing both lists
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy_list)




print("="*100)
import copy
# A deep copy creates a new list and new objects for all elements within the list.

original_list = [1, [2, 3], [4, 5]]

# Creating a deep copy
deep_copy_list = copy.deepcopy(original_list)

# Modifying the deep copy
deep_copy_list[1][0] = 'Y'

# Printing both lists
print("Original List:", original_list)
print("Deep Copy:", deep_copy_list)

