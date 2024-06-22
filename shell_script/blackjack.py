import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            card = (suit, rank)
            deck.append(card)
    return deck

def play_game():
    wins = 0
    total_games = 0
    while True:
        # Set up game
        deck = create_deck()
        random.shuffle(deck)
        username = get_username()  # Moved inside the function
        bet_amount = get_bet_amount()

        # Deal initial cards
        player_hand = deal_cards(deck, 2)
        dealer_hand = deal_cards(deck, 2)

def get_username():
    username = input("What is your username? ")
    return username


def get_bet_amount():
    while True:
        try:
            bet = int(input("How much do you want to bet? (Minimum 20) "))
            if bet >= 20:
                return bet
            else:
                print("Bet amount must be at least 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def deal_cards(deck, num_cards):
    cards = []
    for _ in range(num_cards):
        card = random.choice(deck)
        deck.remove(card)
        cards.append(card)
    return cards


def calculate_hand_value(hand):
    total = 0
    has_ace = False
    for card in hand:
        rank = card[1]
        value = values[rank]
        if rank == "A":
            has_ace = True
        total += value
    # Adjust ace value if necessary
    if has_ace and total > 21:
        total -= 10
    return total


def display_cards(player_hand, dealer_hand):
    for card in player_hand:
        print(f"\t{card[0]} {card[1]}")
    print(f"Your total: {calculate_hand_value(player_hand)}")
    print("Dealer's hand:")
    print(f"\t{dealer_hand[0][0]} {dealer_hand[0][1]} (hidden)")


def ask_hit_or_stand():
    while True:
        choice = input("Hit (h) or Stand (s)? ").lower()
        if choice in ("h", "s"):
            return choice
        else:
            print("Invalid choice. Please enter 'h' for hit or 's' for stand.")


def update_wins_percentage(wins, total_games):
    if total_games > 0:
        percentage = wins / total_games * 100
        print(f"{username}'s win percentage: {percentage:.2f}%")


def play_game():
    wins = 0
    total_games = 0
    while True:
        # Set up game
        deck = create_deck()
        random.shuffle(deck)
        username = get_username()
        bet_amount = get_bet_amount()

        # Deal initial cards
        player_hand = deal_cards(deck, 2)
        dealer_hand = deal_cards(deck, 2)

        # Game loop
        game_over = False
        while not game_over:
            display_cards(player_hand, dealer_hand)
            choice = ask_hit_or_stand()
            if choice == "h":
                new_card = deal_cards(deck, 1)[0]
                player_hand.append(new_card)
                # Calculate player_total after adding the new card
                player_total = calculate_hand_value(player_hand)
                if player_total > 21:
                    print("Busted!")
                    game_over = True
                    break
        # while not game_over:
        #     display_cards(player_hand, dealer_hand)
        #     choice = ask_hit_or_stand()
        #     if choice == "h":
        #         new_card = deal_cards(deck, 1)[0]
        #         player_hand.append(new_card)
        #         player_total = calculate_hand_value(player_hand)
        #         if player_total > 21:
        #             print("Busted!")
        #             game_over = True
        #             break
            else:
    # Reveal dealer's cards and calculate total
                dealer_total = calculate_hand_value(dealer_hand)
                while dealer_total < 17:  # Added the missing '<' operator
                    new_card = deal_cards(deck, 1)[0]
                    dealer_hand.append(new_card)
                    dealer_total = calculate_hand_value(dealer_hand)
# Determine winner
                print("Dealer's hand:")
                for card in dealer_hand:
                    print(f"\t{card[0]} {card[1]}")
                print(f"Dealer's total: {dealer_total}")

                if player_total > 21:
                    print(f"{username} loses. Busted!")
                elif player_total > dealer_total or (player_total == 21 and dealer_total != 21):
                    print(f"{username} wins!")
                    wins += 1  # Update wins if player wins
                    total_games += 1  # Update total games played
                elif player_total == dealer_total:
                    print("It's a tie!")
                else:
                    print(f"{username} loses.")
                    total_games += 1  # Update total games played

                    # Calculate and display winnings/losses
                    if bet_amount > 0:
                        print(f"{username} loses ${bet_amount}.")
                    else:
                        print(f"{username} doesn't win anything this round.")
                    update_wins_percentage(wins, total_games)

                        # Ask if the player wants to play again
                play_again = input("Play again? (y/n) ").lower()
                if play_again not in ("y", "yes"):
                                break
if __name__ == "__main__":
    play_game()

