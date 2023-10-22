import pandas as pd
from random import randint
from faker import Faker

nums_list = [randint(-50, 50) for _ in range(15)]
nums = pd.Series(nums_list)

# ==== sort_values() method - return new sorted Series

# print(nums)
# print(nums.sort_values())

# !! to sort the list and immediately save it to the same variable - use the inplace=True parameter:
# nums = nums.sort_values(inplace=True)
# print(nums)

# !! parameter ascending (default True). if it False - the series will be sorted in descending order
# print(nums.sort_values())
# print(nums.sort_values(ascending=False))

# !! How it works with string-value:
fake = Faker()

n = [fake.name() for _ in range(15)]
names = pd.Series(n)

print(names)
# this method sorts values alphabetically
print(names.sort_values())
print(names.sort_values(ascending=False))
