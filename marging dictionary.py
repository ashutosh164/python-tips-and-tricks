dict = {'a':1, 'b':7}
dict2 = {'b':4,'c':8}

# dict.update(dict2)
dict2.update(dict)
print(dict2)

dict3 = {**dict,**dict2}
print(dict3)
print('-------------------------')
dict3 = dict | dict2
print(dict3)
print('----------------------')


