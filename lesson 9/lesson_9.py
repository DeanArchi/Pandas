import pandas as pd
from random import randint
from faker import Faker

fake = Faker()

nums_list = [randint(-50, 50) for _ in range(15)]
nums = pd.Series(nums_list)

n = [fake.name() for _ in range(15)]
names = pd.Series(nums_list, index=n)

# ==== sort_index() method
# nums.sort_values(inplace=True, ascending=False)
# print(nums)
# nums.sort_index(inplace=True)
# print(nums)

# !! how it works with string-keys:
# print(names)
# names.sort_index(inplace=True)
# print(names)
# names.sort_index(inplace=True, ascending=False)
# print(names)

# !! how it works with date-keys:
dates = [fake.date() for _ in range(15)]
d = pd.Series(nums_list, index=dates)
d.sort_index(inplace=True)
print(d)
d.sort_index(inplace=True, ascending=False)
print(d)
