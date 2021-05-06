num = [12,2,44,6]

even = lambda x: x % 2 == 0
result = [even(i) for i in num]
if any(result):
    print('At list one number is even')
else:
    print('No number is even!')
if all(result):
    print('all number are even')




