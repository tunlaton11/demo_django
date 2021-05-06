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
    postfix_book = 0
    pages = 0
    for i in book_read:
        book_name = i[0:i.find(":")].split(' ')
        for j in book_name:
            if j[-2:] == '\'s':
                postfix_book += 1
                pages += int(i[i.find(':') + 1:])
            else:
                continue
    avg_pages = pages / postfix_book
    return avg_pages

book = open('book_shelf.txt','r')
book_read = book.read().split('\n')
print(book_postfix(book_read))
book.close()



