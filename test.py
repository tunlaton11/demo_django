import random
import string

def setOfWords():
    words = [''.join(random.choices(string.ascii_uppercase,k=random.randint(3,7))) for x in range(500)]
    return set(words)

def createBooks(shelf):
    allWords = list(setOfWords())
    for i in range(1000):
        page = str(random.randrange(99,888))

    titleToken = random.sample(allWords,random.randint(3,5)) 
    postfix = random.randint(0,len(titleToken)-1)
    if random.choice([1,2,3,4,5]) == 3:
        titleToken[postfix]  =titleToken[postfix] + '\'s'  
    title = ' '.join(titleToken)
    title = title.capitalize()
    shelf.write(':'.join([title,page])+'\n')

shelf = open('book_shelf.txt','w')
createBooks(shelf)
shelf.close()

# เปิด file book_shelf.txt และ หาจำนวนหน้าเฉลี่ยต่อเล่ม ของหนังสือทุกเล่มซึ่งมี postfix 's อยู่ในชื่อ
## Your code begins here ##
def book_postfix(book_read):    
    book_name = book_read[0:book_read.find(":")].split(' ')
    for i in book_name:
        if i[-2:] == '\'s':
            return 'Book: '+ i + '\nHas: ' + book_read[book_read.index(':') + 1:]
        else:
            continue
    return 'not found postfix \'s book'

book = open('book_shelf.txt','r')
book_read = book.read()
print(book_postfix(book_read))
book.close()
