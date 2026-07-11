# Demonstration of negative indexing and slicing

lst = [10, 20, 30, 40, 50]

# Negative indexing
print("Last element:", lst[-1])
print("Second last element:", lst[-2])

# List slicing
print("Elements from index 1 to 3:", lst[1:5:1])
print("First three elements:", lst[:3])
print("Last three elements:", lst[-3:])
print("Reverse list:", lst[::-1])
