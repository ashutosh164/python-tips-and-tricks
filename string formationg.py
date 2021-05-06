name = 'ashu'
age = 23
fv_num = 34.234567

print(f'my name is {name} and i am {age} years old and my favourite number is {fv_num:.2f}')

print('--------------map function---------------------------')

number = [14,23,5,45,90,6,79]


def square(x):
    return x * x


new_list = [square(i) for i in number]
print(new_list)

print('-----------OR-------------------')


def square(x):
    return x * x


new_list = map(square,number)
print(list(new_list))





