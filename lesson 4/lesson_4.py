import pandas as pd

# methods of the Series class

names_list = ['Kevin', 'Jack', 'Bob', 'Robin']
nums_list = [10, -20, 50, -30, 40]

names = pd.Series(names_list)
nums = pd.Series(nums_list)

# ==== methods sum(), max(), min(), product(), mean(), lt(), gt(), eq(), ne(), ge(), le(), abs()
print(nums.sum())
print(names.sum())

print(nums.max())
# !! the maximum string is the one that is farthest in the alphabet
print(names.max())

print(nums.min())
# !! the minimum string is the one that is farthest in the alphabet
print(names.min())

# product() return the product of all values in the list
print(pd.Series([1, 2, 3]).product())

# mean() return the mean of all values in the list
print(nums.mean())

# lt() - less than (<)
print(nums.lt(2))

# gt() - greater than (>)
print(nums.gt(15))

# eq() - equal (==)
print(nums.eq(10))

# ne() - not equal (!=)
print(nums.ne(10))

# ge() - greater or equal (>=)
print(nums.ge(10))

# le() - less or equal (<=)
print(nums.le(10))

# abs() - return Series/DataFrame with absolute numeric value of each element
# !! abs() create new Series, not change the initial one
print(nums.abs())
