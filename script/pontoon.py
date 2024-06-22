import random

# Define card values and suit symbols
card_values = {
  "A": 11,  # Ace can be 1 or 11
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 10,
  "Q": 10,
  "K": 10
}

suit_symbols = {
  "♠": "Spades",
  "♥": "Hearts",
  "♦": "Diamonds",
  "♣": "Clubs"
}

# Function to deal a card
def deal_card(deck):
  card = random.choice(deck)
  deck.remove(card)
  return card, card_values[card]

# Function to calculate hand value (considering Ace as 1 if bust)
def hand_value(hand):
  value = 0
  for card in hand:
    value += card[1]
    if value > 21 and "A" in [card[0] for card in hand]:  # Adjust Ace value if bust
      value -= 10
  return value

# Function to display a card
def display_card(card):
  value, suit = card
  symbol = suit_symbols[suit]
  print(f"{value}{symbol}", end=" ")

# Simulate Blackjack gameplay
def play_blackjack():
  # Initialize deck and player/dealer hands
  deck = list(card_values.keys()) * 4  # Create 4 decks
  random.shuffle(deck)
  player_hand = []
  dealer_hand = []

  # Deal initial cards
  for _ in range(2):
    player_card, player_value = deal_card(deck)
    player_hand.append((player_card, player_value))
    dealer_card, dealer_value = deal_card(deck)
    dealer_hand.append((dealer_card, dealer_value))

  # Player turn (hit until bust or choose stand)
  while True:
    # Show only the first dealer card
    print(f"Dealer hand: [{dealer_hand[0][0]}{suit_symbols[dealer_hand[0][1]]}, ?]")

    print(f"Player hand: {display_cards(player_hand)} (Total: {hand_value(player_hand)})")
    action = input("Hit (h) or Stand (s)? ").lower()
    if action == 's':
      break
    new_card, new_value = deal_card(deck)
    player_hand.append((new_card, new_value))
    if hand_value(player_hand) > 21:
      print("Player Bust!")
      break

  # Dealer turn (hit until 17 or higher)
  while hand_value(dealer_hand) < 17:
    new_card, new_value = deal_card(deck)
    dealer_hand.append((new_card, new_value))

  # Determine winner
  player_value = hand_value(player_hand)
  dealer_value = hand_value(dealer_hand)
  print(f"Dealer hand: {display_cards(dealer_hand)} (Total: {dealer_value})")
  if player_value > 21:
    print("You lose!")
  elif dealer_value > 21:
    print("You win!")
  elif player_value > dealer_value:
    print("You win!")
  elif player_value == dealer_value:
    print("Push (Tie)")
  else:
    print("You lose!")

# Play a round
play_blackjack()
