myname = ['ashu','jilu','silu','lilu','bulu','sana','anil']
counter = 0
for name in myname:
    print(f'{counter}: {name}')
    counter += 1

print('------------------------------------')
for index, name in enumerate(myname):
    print(f'{index}: {name}')

print(list(enumerate(myname)))
print(dict(enumerate(myname)))




