# Prog-05: The 24 Game
# 6???????21 Name ?

from itertools import permutations, product
import math

def generate_all_combinations(num_list, operators):
    all_combi = []
    for n,o in product(sorted(set(permutations(num_list))),
                                product(operators, repeat=3)):
        x = [None]*(len(n)+len(o))
        x[::2] = n
        x[1::2] = o
        all_combi.append(x)
    return all_combi
#---------------------------------------------------------
def cal(i):
    case1 = ['(','(',i[0],i[1],i[2],')',i[3],i[4],')',i[5],i[6]]
    case2 = ['(',i[0],i[1],'(',i[2],i[3],i[4],')',')',i[5],i[6]]
    case3 = ['(',i[0],i[1],i[2],')',i[3],'(',i[4],i[5],i[6],')']
    case4 = [i[0],i[1],'(','(',i[2],i[3],i[4],')',i[5],i[6],')']
    case5 = [i[0],i[1],'(',i[2],i[3],'(',i[4],i[5],i[6],')',')']
    case_check = [case1, case2, case3, case4, case5]
    for j in case_check:
        try:
            eval("".join(j))
        except ZeroDivisionError: #except divided by zero case
            continue
        if eval("".join(j)) == 24:
            
            return " ".join(j) + " = 24"

        else:
            continue


#---------------------------------------------------------
nums = input('Enter 4 integers: ')
num_split = nums.split( )


cases = generate_all_combinations( num_split, '+-*/' )
check_result = 0
for i in cases:
    result = cal(i)
    if result == None:
        continue
    else:
        print(result)
        check_result += 1
        break
if check_result == 0:
    print("No Solutions")
