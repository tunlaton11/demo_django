import random

a = 'abcdefghijklmnopqrstuvwxyz'
randomStrings = [''.join(random.choices(a,k=5)) for x in range(1000)]
print(randomStrings)
print('-----------------')


for i in randomStrings:
    if i.count('a') == 2:
        print(i)
    else:
        continue

