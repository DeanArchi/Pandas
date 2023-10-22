import pandas as pd
from random import randint, choice

# accessing Series items

nums_list = [randint(-50, 50) for _ in range(10)]
indices = [choice([0, 1, 2, 3]) for _ in range(10)]
letters = [choice('abcd') for _ in range(10)]

nums = pd.Series(nums_list)

# indices can be repeated:
# nums_1 = pd.Series(nums_list, index=indices)
# print(nums_1)
nums_2 = pd.Series(nums_list, index=letters)
print(nums_2)

# ==== method loc() - return all elements with index n
# print(nums_1.loc[3])
# print(nums_1.loc[[3, 0]])
# print(nums_1.loc[[2, 0, 3]])

# !! using loc() you can change all values of elements with index n:
# nums_1.loc[3] = 100
# nums_1.loc[[3, 1]] = 100
# print(nums_1)

# print(nums_2.loc[['a', 'c']])

# ==== method iloc() - integer-location based indexing for selection by position, not index
# print(nums_1.iloc[1])
# print(nums_1.iloc[[4, 2, 9]])

# print(nums_2.iloc[[0, 3]])
