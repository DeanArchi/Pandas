import pandas as pd
from random import randint, shuffle
from string import ascii_lowercase

# slice of the Series object

nums_list = [randint(-50, 50) for _ in range(26)]
# nums = pd.Series(nums_list)
#
# print(nums[2:9])
# print(nums[5:17:3])
# print(nums[10:0:-1])
# print(nums[:10])
# print(nums[10:])
# print(nums[::-1])

let = list(ascii_lowercase)
print(let)
letters = pd.Series(nums_list, index=let)
# print(letters)
# print(letters['a':'f'])
# print(letters['f':'a':-2])

shuffle(let)
print(let)
letters_1 = pd.Series(nums_list, index=let)
print(letters_1['a':'b'])
