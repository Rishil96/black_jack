# Day 11 Project Black Jack

import random

# Simplified Deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to Deal Cards
def deal_card():
    return random.choice(cards)


# Function to check Ace condition
def ace_in_hand(hand):
    return 11 in hand


# Function to check if player is busted
def check_bust(total):
    return total > 21


# Function to check winner of the game
def check_winner(player, dealer):
    if player > dealer:
        return 1
    elif dealer > player:
        return 2
    else:
        return 0


# Final Game function
def black_jack():

    player_hand = []
    dealer_hand = []

    for card in range(0, 2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    player_total = sum(player_hand)
    dealer_total = sum(dealer_hand)

    print(f"\nPlayer Hand: {player_hand}\nTotal: {player_total}")
    print(f"\nDealer's First card: {dealer_hand[0]}")

    game_on = True
    early_result = False
    while game_on:

        play = 'user decision'
        while play not in ['h', 's']:
            play = input("Type 'h' Hit and 's' to stand: ")

        if play == 'h':
            card = deal_card()
            player_hand.append(card)
            player_total += card
            print(f"\nYour current hand: {player_hand}\nTotal: {player_total}")

            if check_bust(player_total):

                if ace_in_hand(player_hand):
                    player_total -= 10
                    player_hand.remove(11)
                    player_hand.append(1)
                    print("Your Ace has value 1 now to save you from getting Busted!")
                    print(f"\nYour current hand: {player_hand}\nTotal: {player_total}")

                    if check_bust(player_total):
                        print("BUSTED!")
                        print("Dealer Wins.")
                        early_result = True
                        break
                else:
                    print("BUSTED!")
                    print("Dealer Wins.")
                    early_result = True
                    break
            else:
                pass

        else:
            game_on = False
            print("Dealer's turn")
            print(f"\nDealer's Hand: {dealer_hand}\nTotal: {dealer_total}")
            while dealer_total < 17:
                card = deal_card()
                dealer_hand.append(card)
                dealer_total += card
                print(f"\nDealer's Hand: {dealer_hand}\nTotal: {dealer_total}")
                if check_bust(dealer_total):

                    if ace_in_hand(dealer_hand):
                        dealer_hand.remove(11)
                        dealer_hand.append(1)
                        dealer_total -= 10
                        print("Dealer's Ace took the value 1 to avoid getting BUSTED!")
                        print(f"\nDealer's Hand: {dealer_hand}\nTotal: {dealer_total}")

                        if check_bust(dealer_total):
                            print("Dealer BUSTED!")
                            print("You win!")
                            early_result = True
                            break

                        else:
                            pass
                    else:
                        print("Dealer BUSTED!")
                        print("You win!")
                        early_result = True
                        break
                else:
                    pass

    if not early_result:
        winner = check_winner(player_total, dealer_total)
        if winner == 1:
            print("\nCongratulations! You Win.")
        elif winner == 2:
            print("\nDealer Wins! Better luck next time.")
        else:
            print("\nTough Game! It was a Tie.")

    play_again = input("\nWould you like to play again? y/n: ")

    if play_again == 'y':
        black_jack()
    else:
        print("\nHave a nice day!")


playing = input("\nWelcome to Black Jack.\nPress 'y' to play or 'n' to exit: ")

if playing == 'y':
    black_jack()
else:
    print("\nHave a nice day!")
