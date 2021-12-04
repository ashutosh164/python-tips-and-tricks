'''List comprehension'''

a = [2, 3, 4, 5, 6, 7, 8, 9]


'''print even number'''
b = []
for i in a:
    if i %2 == 0:
        b.append(i)

print(b)

b = [i for i in a if i % 2 == 0]

print(b)
c = [2 ** i for i in range(10) if i %5 == 0]
print(c)

word = ['car','anger','ancher','fox','automation']

a = [i.upper() if i.startswith('a') else i for i in word]
print(a)
b = [i.upper() for i in word if i.startswith('a')]
d = [i.upper() if i.startswith('a') else i for i in word]
print(b)
print(d)

c = [i.lower() for i in word if not i.startswith('a')]
print(c)

print(b + c)

print('-------------------------strings---------------------------')

'''  string   '''


name = 'ashu'
age = 23
s = 34.565676

print('hello my name is '+ name + 'and i am ' + str(age) + ' years old')
print('hello my name is {} and i am {} years old'.format(name,age))
print('hello my name is %s and i am %d years old' %(name,age))
print(f'hello my name is {name} and i am {age} years old, asd my number is {s:.2f}')

print('-------------------map function-----------------------------')

a = [23,45,3,66,45,67,878,4]


def square(i):
    return i * i

b = []
for i in a:
    b.append(square(i))
print(b)

x = map(square,a)
print(list(x))

print(list(map(str,a)))

print('-------------------ternary operator----------------------------')

age = 24
size = 32

# if age > 18:
#     print('you are an adult')
# else:
#     print('you are not an adult')
# print('**********************')

print('you are an adult' if age > 18 else 'you are not an adult')

# print('you are a sexy girl' if size == 32 and age == 24 else 'you a not sexy')
print('you are a sexy girl' if size == 32 and (age <= 24 or age >= 18) else 'you are old age' if age >= 24 else 'you are not sexy you size is too large' if size > 32 else 'you are fit')












