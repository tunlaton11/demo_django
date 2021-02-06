

import math

def shuffle(deck):   

    front_deck = deck[0: math.ceil((len(deck)/4) / 2) * 4]
    rear_deck = deck.replace(front_deck, "")
    front_split = list(filter(("").__ne__,front_deck.split("|")))
    rear_split = list(filter(("").__ne__,rear_deck.split("|")))
    new_deck = [None] * (len(front_split) + len(rear_split))
    new_deck[::2], new_deck[1::2] = front_split, rear_split

    new_deck = "|" + '||'.join(new_deck) + "|"


    return new_deck

print(shuffle("|2H||3H||4H||5H||6H||7H||8H||9H||TH||JH||QH||KH||AH|"))