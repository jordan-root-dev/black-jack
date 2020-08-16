
import sys
from classes import Card, Deck, Player, House
from functions import bust_check

print("\nLet's play Black Jack!!!\n")

# Instantiate player and house.
player = Player(10)
house = House()

# Create a new deck.
deck = Deck()

# Shuffle the deck
deck.shuffle()

# Play through whole deck discarding as you go until deck no longer has enough cards to play.    
#while len(new_deck.all_cards) > 0:

# Deal hands one card to player, one card to house until both have two cards.
for _ in range(2):
    player.hand.append(deck.deal_one())
    house.hand.append(deck.deal_one())

# set value of house and player hands and set ace counts for each.
for card in player.hand:
    player.hand_value += card.value
    if card.rank == 'Ace':
        player.ace_count += 1

for card in house.hand:
    house.hand_value += card.value
    if card.rank == 'Ace':
        house.ace_count += 1

# Print one of house' cards and one 'covered'
print(f'House Hand:\n{house.hand[0]}\nHidden Card\n')

# Print player cards.
print('Player Hand:')
for card in player.hand:
    print(card)

# Player Turn. Ask player to hit or hold. Use while loop
while True:
    
    hit_or_hold = input('\nHit or Hold? ').lower()
    
    while hit_or_hold not in ('hit', 'hold'):
        hit_or_hold = input("I didn't quite get that. Hit or hold?").lower()
    
    if hit_or_hold == 'hit':
            
        # Deal one card to player
        player.hand.append(deck.deal_one())

        # Add new card value to hand value
        player.hand_value += player.hand[-1].value

        # Check if card is an ace and add to ace_count
        if player.hand[-1].rank == 'Ace':
            player.ace_count += 1
        
        print('\nPlayer Hand:')
        for card in player.hand:
            print(card)

        # Check bust
        bust = bust_check(player)
        if bust:
            print('\n\nPlayer Bust!')
            print(f'Player Value: {player.hand_value}')
            print('\nGame Over!')
            sys.exit()
        else:
            continue
    else:
        break

# If player doesn't bust, house turn.
while True:
    if house.hand_value >= 17:
        break

    house.hand.append(deck.deal_one())
    house.hand_value += house.hand[-1].value
    
    if house.hand[-1].rank == 'Ace':
        house.ace_count += 1

    bust = bust_check(house)
    if bust:
        print('\n\nHouse busts! Player wins!\n\nHouse Hand:')
        for card in house.hand:
            print(card)
        print(f'House Value: {house.hand_value}')
        print('\nGame Over!')
        sys.exit()
    elif house.hand_value >= 17:
        break
    else:
        continue

if player.hand_value == house.hand_value:
    print('\n\nPush!\n')
    print('House Hand:')
    for card in house.hand:
        print(card)
    print(f'House Value: {house.hand_value}\n')
    print('Player Hand:')
    for card in player.hand:
        print(card)
    print(f'Player Value: {player.hand_value}')
elif player.hand_value > house.hand_value:
    print('\n\nPlayer Wins!\n')
    print('House Hand:')
    for card in house.hand:
        print(card)
    print(f'House Value: {house.hand_value}\n')
    print('Player Hand:')
    for card in player.hand:
        print(card)
    print(f'Player Value: {player.hand_value}')
else:
    print('\n\nHouse Wins!\n')
    print('House Hand:')
    for card in house.hand:
        print(card)
    print(f'House Value: {house.hand_value}\n')
    print('Player Hand:')
    for card in player.hand:
        print(card)
    print(f'Player Value: {player.hand_value}')

print('\nGame Over!')