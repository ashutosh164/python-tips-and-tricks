name = ['ashu','jilu','silu','lilu','bulu']
age = [25,23,21,22,27]

for i in range(len(name)):
    print(f'Name: {name[i]},Age: {age[i]}')

print('---------------------------------')
# ANOTHER METHOD
for name,age in zip(name,age):
    print(f'Name: {name}, Age: {age}')

print('-----------------------------')


sales = [500,3400,3333,25555,22425,134667,25656]
costs = [400,3000,2500,2000,2000,12000,20534]
print('Profit is:')
for sales,costs in zip(sales,costs):
    print(int(sales-costs))
print('--------------------------------------')

zipped = [('ashu',25),('jilu',23),('lilu',21),('silu',20)]

name , age = zip(*zipped)
print(list(name))
print(list(age))

print('---------------------------')

latters = ['b','d','a','c']
numbers = [3,2,4,1]

data = sorted(zip(latters,numbers))
print(list(data))
latters,numbers = zip(*data)
print('===========================')
print(latters)
print(numbers)

print('-----------------------------')

latters = ['b','d','a','c']
numbers = [3,2,4,1]
mydict = dict(zip(latters,numbers))
print(mydict)











