from itertools import product
suits = ('пик', 'треф', 'бубен', 'червей')
nominals = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
ejected = input()
suits_without = tuple(filter(lambda x: x != ejected, suits))
cards = product(nominals, suits_without)
for card in cards:
    print(*card)
