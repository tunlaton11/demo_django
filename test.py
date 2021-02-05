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

print(show_table_cards("|2H||3H||4H||5H|",3))