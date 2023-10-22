import pandas as pd
from random import randint
from faker import Faker

# ==== apply() method - call function on values of Series

fake = Faker()

numbers = [randint(-10, 10) for _ in range(75)]
names = [fake.name() for _ in range(15)]

nums = pd.Series(numbers)


def sign(x):
    if x > 0:
        return 'positive'
    if x < 0:
        return 'negative'
    return 'zero'


print(sign(10))
# !!! returns new Series !!!
print(nums.apply(sign))


def get_surname(x):
    """
        Austin Taylor.
        split() - ['Austin', 'Taylor']
        split()[1] - 'Taylor'
    """
    return x.split()[1]


name = pd.Series(names)
print(name)
print(name.apply(get_surname))
print(name.apply(lambda x: x.split()[0]))
print(name.apply(lambda x: len(x)))

