# Prog-07: EAN-13 Barcode
# ??3?????21 Name ?

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code):      
    x = [[int(e) for e in ean13_code]]   
    plt.axis('off')   
    plt.imshow(x, aspect='auto', cmap='binary')   
    plt.title(digits)    
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')    
    codes = encode_EAN13(digits)  
    if codes == '':       
        print(digits, 'is not an EAN-13 number.')        
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================

pattern_L_G = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', \
               'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL' ]


def codes_of(digits, patterns):
    codes = ''
    for i, j in zip(digits,patterns):
        if j == 'L':
            codes += L_codes[int(i)]
        elif j == 'G':
            codes += G_codes[int(i)]
        elif j == 'R':
            codes += R_codes[int(i)]
    return codes



def digits_of(codes):
    digits = ''
    check_digits = ''
    for i in range(0, len(codes), 7):
        check_digits += (codes[i : i + 7])
        if check_digits in L_codes:
            digits += str(L_codes.index(check_digits))
        elif check_digits in G_codes:
            digits += str(G_codes.index(check_digits))
        elif check_digits in R_codes:
            digits += str(R_codes.index(check_digits))
        else:
            digits = ''
            break
        check_digits = ''
    return digits



def patterns_of(codes):
    patterns = ''
    check_patterns = ''
    for i in range(0, len(codes), 7):
        check_patterns += (codes[i : i + 7])
        if check_patterns in L_codes:
            patterns += 'L'
        elif check_patterns in G_codes:
            patterns += 'G'
        elif check_patterns in R_codes:
            patterns += 'R'
        else:
            patterns = ''
            break
        check_patterns = ''
    return patterns



def check_digit(digits):
    check_digit = 0
    check_sum = 0
    check_product = '131313131313'
    for i, j in zip(digits, check_product):
        check_sum += int(i) * int(j)        
    if check_sum % 10 == 0:
        check_digit = 0
    else:
        check_digit += ((check_sum // 10) * 10 + 10) - check_sum
        
    return str(check_digit)



def encode_EAN13(digits):
    for i in digits: #1. check is digits ?
        if not i.isdigit():
            return ''
    if len(digits) == 13: #2. check length equal to 13 ?
        if check_digit(digits[0: 12]) == digits[12]: #3. check digit is correct ?
            group_1 = codes_of(digits[1:7], pattern_L_G[int(digits[0])])
            group_2 = codes_of(digits[7:], 'RRRRRR')
            return '101' + group_1 + '01010' + group_2 + '101'
        else:
            return ''
    else:
        return ''
    
    


def decode_EAN13(codes):
    group_1, group_2 = codes[3:45], codes[50:92]
    if patterns_of(group_1) == 'GGGGGG': #check flip pattern
            group_1 = group_2[::-1], group_2 = group_1[::-1]
    for i in codes:
        if not i.isdigit() or i not in ('0','1'): #1 check is digit or equal to 0,1 ?
            return ''
    if len(codes) == 95: #2. check length equal to 95 ?        
        if digits_of(group_1) == '' or digits_of(group_2) == '': #3. check codes can find values?
            return ''
        else: 
            num = str(pattern_L_G.index(patterns_of(group_1))) + digits_of(group_1) + digits_of(group_2)
            if check_digit(num[0: 12]) == num[12]: #4. check digit is correct ?
                return num
            else:
                return ''
    else:
        return ''



#-------------------------------------------------
test1()