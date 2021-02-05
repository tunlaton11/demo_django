# Prog-03: Card Game
# 6???????21 Name ?


import time
import random
import math

def generate_deck(n_cards, n_shuffles):
    print('Shuffle', end='')
    deck = ''
    for suit in 'CDHS':
        for face in 'A23456789TJQK':
            deck += '|' + face + suit + '|'
    for i in range(n_shuffles):
        deck = cut(deck, random.randint(0,n_cards))
        deck = shuffle(deck)
        time.sleep(0.1)
        print('.', end='')
    print()
    return deck[:4*n_cards]

def play(n_cards):
    print('Start a card game.')
    deck = generate_deck(n_cards, 20)

    p1, deck = deal_n_cards(deck, 5)
    p2, deck = deal_n_cards(deck, 5)
    players = [p1, p2]
    
    table_cards, deck = deal_n_cards(deck, 1)
    fail = False
    turn = 0
    
    while True:
        show_table_cards(table_cards, 10)
        show_player_cards(players[turn], turn+1)
        k = select_card_number(players[turn])
        valid = (k != 0)
        if valid:
            cards = players[turn]
            card = peek_kth_card(cards, k)
            valid = eq_suit_or_value(card, table_cards[-4:])
            if valid:
                table_cards += card
                players[turn] = remove_kth_card(cards, k)
                fail = False
        if not valid:
            print('  ** Invalid **')
            if len(deck) == 0:
                if fail: break
                fail = True
            if len(deck) > 0:
                print('  >> get a new card')
                card, deck = deal_n_cards(deck, 1) 
                players[turn] = card + players[turn]
                
        show_player_cards(players[turn], turn+1)
        if len(players[turn]) == 0: break
        turn = (turn + 1) % len(players)

    if len(deck) == 0:
        print('\n** No more cards **')
    print('*****************')
    if len(deck) == 0 and \
         len(players[0]) == len(players[1]):
            print('Draw!!!')
    elif len(players[0]) < len(players[1]):
        print('Player # 1 win!!!')
    else:
        print('Player # 2 win!!!')        

def eq_suit_or_value(card1, card2):
    return card1[1] == card2[1] or \
                 card1[2] == card2[2]

def show_player_cards(cards, k):
    print('  Player #', k, ':', cards)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass

def select_card_number(cards):
    n = len(cards)//4
    k = input_int('  Select card # (1-'+ str(n)+') : ')
    if not(1 <= k <= n): k = 0
    return k
#---------------------------------------
def peek_kth_card(cards, k):
    cards_split = cards.split("|")
    cards_split = list(filter(("").__ne__,cards_split))
    the_kth_card = "|" + cards_split[k - 1] + "|"

    return the_kth_card
#---------------------------------------
def remove_kth_card(cards, k):
    del_cards = peek_kth_card(cards, k)
    new_cards = cards.replace(del_cards, "")

    return new_cards
#---------------------------------------
def deal_n_cards(deck, n):
    deck_split = deck.index("|", n*4 % len(deck))
    cards = deck[0: deck_split]
    new_deck = deck[deck_split:]

    return cards, new_deck
#---------------------------------------
def cut(deck, m):
    move_card = deal_n_cards(deck, m)
    new_deck = move_card[1] + move_card[0]


    return new_deck
#---------------------------------------
def shuffle(deck):
    front_deck = deck[0: math.ceil((len(deck)/4) / 2) * 4]
    rear_deck = deck.replace(front_deck, "")
    front_split = list(filter(("").__ne__,front_deck.split("|")))
    rear_split = list(filter(("").__ne__,rear_deck.split("|")))
    new_deck = [item for pair in zip(front_split, rear_split + [0]) for item in pair] 
    if new_deck[-1] == 0:
        del new_deck[-1]

    new_deck = "|" + '||'.join(new_deck) + "|"


    return new_deck
#---------------------------------------
def show_table_cards(cards, m):
    card_split = cards.index("|", m*-4 % len(cards))
    if m * 4 >= len(cards):
        card = cards
        print("-"*7 + "-"*len(cards))
        print("Table:", card)
        print("-"*7 + "-"*len(cards))
    else:
        card = "..." + cards[card_split:]
        print("-"*10 + "-"*len(cards[card_split:]))
        print("Table:", card)
        print("-"*10 + "-"*len(cards[card_split:]))
#-----------------------------------------    
play(51)