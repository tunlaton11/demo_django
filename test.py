def cal(i):
    case1 = ['(','(',i[0],i[1],i[2],')',i[3],i[4],')',i[5],i[6]]
    return "".join(case1)

print(cal(['1', '+', '2', '+', '3', '+', '4']))