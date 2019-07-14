# -*- coding: UTF-8 -*-

import random
import codecs
import copy

cardJokers = ('♞', '♘')
cardMarks = ('♠', '♥', '♦', '♣')
cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')

deck = []
for c in cardJokers:
    deck.append(c)
#print(deck)

for cn in cardNumbers:
    for cm in cardMarks:
        card = cm + cn
        deck.append(card)
#print(deck)

f = codecs.open("deck-old-54.txt", "w", "utf-8")
for card in deck:
    f.write(card)
    f.write('\n')
f.close

#--------------
'''
shuffledDeck = []
count = len(deck)
for i in range(count):
    pickedCard = random.choice(deck)
    shuffledDeck.append(pickedCard)
    deck.remove(pickedCard)

f = codecs.open("deck-new-54.txt", "w", "utf-8")
for card in shuffledDeck:
    f.write(card)
    f.write('\n')
f.close
'''
# method 2:
shuffledDeck = copy.copy(deck)
random.shuffle(shuffledDeck)

f = codecs.open("deck-new-54.txt", "w", "utf-8")
for card in shuffledDeck:
    f.write(card)
    f.write('\n')
f.close

print('\n ------- Cutting line 1------')
p1_desk=[]
for i in range(0,19):
    p1_desk.append(shuffledDeck[i])
    shuffledDeck.remove(shuffledDeck[i])
print(p1_desk)

f = codecs.open("deck-player1-54.txt", "w", "utf-8")
for a in p1_desk:
    f.write(a)
    f.write('\n')
f.close


print('\n ------- Cutting line 2 ------')
p2_desk=[]
for i in range(0,19):
    p2_desk.append(shuffledDeck[i])
    shuffledDeck.remove(shuffledDeck[i])
print(p2_desk)

f = codecs.open("deck-player2-54.txt", "w", "utf-8")
for b in p2_desk:
    f.write(b)
    f.write('\n')
f.close


print('\n ------- Cutting line 3 ------')
p3_desk=[]
for i in range(0,19):
    p3_desk.append(shuffledDeck[i])
    shuffledDeck.remove(shuffledDeck[i])
print(p3_desk)

f = codecs.open("deck-player3-54.txt", "w", "utf-8")
for c in p3_desk:
    f.write(c)
    f.write('\n')
f.close


print('\n ------- Cutting line 4 ------')
p4_desk=[]
for i in range(0,19):
    p4_desk.append(shuffledDeck[i])
print(p4_desk)

f = codecs.open("deck-player4-54.txt", "w", "utf-8")
for c in p4_desk:
    f.write(c)
    f.write('\n')
f.close
