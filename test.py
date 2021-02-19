
def check(i):
    for j in i:
        try:
            j
        except ZeroDivisionError:
            continue
        if j == 24:
            return True
        else:
            continue 

print(check([1, 3, 3/0, 24]))