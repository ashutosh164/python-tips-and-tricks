number = [12,13,4,5,24,25]


def square(x):
    return x * x


new = []

for i in number:
    new.append(square(i))

print(new)
print('-------------------OR-----------------------')
number = [12,13,4,5,24,25]


def square(x):
    return x * x


new = [square(i) for i in number]


print(new)

print('-------------------OR---MAP--------------------')

number = [12,13,4,5,24,25]


def square(x):
    return x * x


new = map(square,number)
# new = map(str,number)
print(list(new))


import math


def area(r):
    return math.pi * (r**2)

redii = [2, 4, 3, 6]
areas = []

# for r in redii:
#     a = area(r)
#     areas.append(a)
# print(areas)

print(list(map(area, redii)))




