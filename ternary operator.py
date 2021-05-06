age = 4

# if age >= 18:
#     adult = True
# else:
#     adult = False

adult = True if age >= 18 else False

# if adult:
#     print('you are adult ')
# else:
#     print('you are not adult')

print('you are adult' if adult else 'you are not an adult')

print('---------------------------------------------')

num = 10

print('number is very very large' if num > 1000 else 'this number is quite large' if num > 100 else 'this number is small')
