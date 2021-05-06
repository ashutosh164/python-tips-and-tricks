my_square = lambda x: x * x
print(my_square(3))


mysum = lambda x,y: x + y
print(mysum(4,5))


mysum = lambda *args: sum(args)
print(mysum(12,23,34,45,4))


print((lambda x:x ** 3)(5))


numbers = [2,34,3,5,6,7,8,998,24,54,45,6]

even= filter(lambda x: x%2 == 0,numbers)
print(list(even))


square= list(map(lambda x: x ** 2,numbers))
print(square)


def myfunc(num):
    return lambda x: x * num
ten_multy = myfunc(10)
print(ten_multy(54125))


print((lambda x:x*10)(69))