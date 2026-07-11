# Convert different data types into list

# 1. String to list
s = "Python"
print("List from string:",list(s))

# 2. Tuple to list
t = (1, 2, 3, 4)
list_from_tuple = list(t)
print("List from tuple:", list_from_tuple)

# 3. Set to list
st = {10, 20, 30}
list_from_set = list(st)
print("List from set:", list_from_set)

# 4. Dictionary keys to list
d = {1: 'a', 2: 'b', 3: 'c'}
list_from_dict_keys = list(d)
print("List from dictionary keys:", list_from_dict_keys)

# 5. Dictionary values to list
list_from_dict_values = list(d.items())
print("List from dictionary values:", list_from_dict_values)
