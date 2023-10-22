import pandas as pd

# # attributes of the Series class

names = ['Bob', 'Jack', 'Kevin', 'Robin']
letters = ['b', 'j', 'k', 'r']
numbers = [10, 20, 30, 40, 50]

n = pd.Series(names)
nums = pd.Series(numbers)
print(n.values)
print(nums.values)
print(n.index)
print(nums.index)

n_letters = pd.Series(names, index=letters)
print(n_letters.index)

print(n.size)
print(nums.size)

# ==== is_unique returns True if all elements is unique otherwise False
print(n.is_unique)
names = ['Bob', 'Bob', 'Kevin', 'Robin']
n = pd.Series(names)
print(n.is_unique)

# ==== is_monotonic_decreasing return True if values in the object are monotonically decreasing
print(nums.is_monotonic_decreasing)
# ==== is_monotonic_increasing return True if values in the object are monotonically increasing
print(nums.is_monotonic_increasing)

# ==== ndim number of dimensions of the underlying data, by definition 1
print(nums.ndim)

# ==== dtype return the dtype object of the underlying data.
print(n.dtype)
print(nums.dtype)
