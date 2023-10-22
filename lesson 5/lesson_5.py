import pandas as pd
from random import randint

nums_list = [randint(-50, 50) for _ in range(100)]
nums = pd.Series(nums_list)

print(nums)
# !! if the Series has a size greater than 60, it is displayed in abbreviated form
# output:
# nums:
# 0    -41
# 1     50
# 2    -33
# 3     42
# 4     21
#       ..
# 95    -3
# 96   -40
# 97    38
# 98    38
# 99    46
# Length: 100, dtype: int64

# ==== head() return the first n rows.
print(nums.head())  # default it's 5
print(nums.head(10))

# ==== tail() return the last n rows.
print(nums.tail())  # default it's 5
print(nums.tail(10))

# ==== take() return the elements in the given positional indices along an axis
print(nums.take([7]))
print(nums.take([3]))
print(nums.take([10, 3]))
print(nums.take(range(10, 16)))
print(nums.take(range(10, 26, 2)))
