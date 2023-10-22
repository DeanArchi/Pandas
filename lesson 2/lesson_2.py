import pandas as pd

# # operations on Series

# a = [43, 54, 3, 654, 4, 65, 3, 543, 32, 32]
# table = pd.Series(a)

# # === + added 2 to all items.
# table_1 = table + 2
# print(table_1)
# print(table)

# # operator *
# table_1 = table * 2
# print(table_1)

# # operator -
# table_1 = table - 2
# print(table_1)

# # operator /
# table_1 = table / 2
# print(table_1)

# # operator **
# table_1 = table ** 2
# print(table_1)

# # operator //
# table_1 = table // 2
# print(table_1)

# # operator %
# table_1 = table % 2
# print(table_1)

# # operators >, >=, <, <=, ==, !=
# table_1 = table > 45
# print(table_1)
# table_2 = table >= 45
# print(table_2)
# table_3 = table < 45
# print(table_3)
# table_4 = table <= 45
# print(table_4)
# table_5 = table == 32
# print(table_5)
# table_6 = table != 45
# print(table_6)

# # functions max(), min(), sum(), sorted(), len(), list(), tuple(), set()
a = [43, 54, 3, 654, 4, 65, 3, 543, 32, 32]
table = pd.Series(a)
# print(max(table))
# print(min(table))
# print(sum(table))
# print(sorted(table))
# print(len(table))
# print(list(table))
# print(tuple(table))
# print(set(table))
b = ['car', 'motorcycle', 'airplane', 'yacht']
table_1 = pd.Series(b)
print(table_1 + ' abc')
print(table_1 * 2)
# !!!! The comparison is done character by character. For example, a < c < z
print(table_1 > 'abc')
print(table_1 > 'zbc')
