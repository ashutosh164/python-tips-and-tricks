num = [18,16,22,99,11,54,13,53]
new = []
for i in num:
    if i % 2 == 0:
        new.append(i)
print(new)

print('--------------------OR--------------------------')

# LIST COMPREHENSIONS
num = [18,16,22,99,11,54,13,53]
new = [i for i in num if i % 2 == 0]
print(new)


number = [1,2,3,4,5,6,7]
new1 = [2 ** i for i in number]
print(new1)

print('--------------------------------------')

word = ['automate','python','anchor','car','anger']
# x = [word.upper() if word.startswith('a') else word for word in word]
x = [i.upper() for i in word if i.startswith('a')]
print(x)




