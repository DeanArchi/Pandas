import pandas as pd

# # Series object is a table of 1 column (one-dimensional array)
# a = [54, 6, 7, 43, 43]
# b = [True, True, False, True, False]
# c = [54, 6, 7, 43, 'str']
# table_1 = pd.Series(a)
# table_2 = pd.Series(b)
# table_3 = pd.Series(c)
# print(table_1)
# print(table_2)
# print(table_3)

# # output:
# table_1:          table_2:            table_3:
# 0     54          0     True          0     54
# 1     6           1     True          1     6
# 2     7           2     False         2     7
# 3     43          3     True          3     43
# 3     43          4     False         4     'str'
# dtype: int64      dtype: bool         dtype: object

# # You can get an item in the table by key:
# print(table_1[2])
# print(table_3[4])

# # You can generate Series with func range()
# table = pd.Series(range(10, 110, 10))
# print(table)

# # Pandas uses 0, 1, ..., n for key numbering, but you can set your own values:
# # !!!! The number of  keys must match the number of items in the list !!!!
# lst = ['Hello', 'World']
# table_1 = pd.Series(lst, ['Привіт', 'Світ'])
# print(table_1)

d = {
    'Привіт': 'Hello',
    'Світ': 'World'
}

table_2 = pd.Series(d)
print(table_2)

# # output:
# table_1 and table_2:
# Привіт     Hello
# Світ       World
# dtype: object
