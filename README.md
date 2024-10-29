# **Old Maid Card Game**

Welcome to **Old Maid**, a classic card game brought to life with Python! This game follows traditional Old Maid rules, where players aim to discard all paired cards from their hands and avoid holding the unmatchable card – the Queen.

## **Game Description**

**Old Maid** is a classic children’s card game that can be played by two or more players. The objective is simple: avoid being the last player holding the "odd" card. Players match pairs of equal ranks (ignoring suits) and remove them until only one card – the Old Maid – remains. **Whoever holds the Old Maid loses the game.**

## **Features and Functions**

This implementation includes various functions that simulate a complete game of Old Maid between the player (Human) and a computer opponent (Robot). Here’s a breakdown of each function:

- **`make_deck()`**: Creates a deck with all cards, excluding one Queen to form the “Old Maid.”
- **`shuffle_deck(deck)`**: Shuffles the deck randomly to start the game.
- **`deal_cards(deck)`**: Distributes the cards between the player and the computer.
- **`remove_pairs(l)`**: Identifies and removes all pairs from a hand, then shuffles the remaining cards.
- **`print_deck(deck)`**: Prints the cards in a player's hand.
- **`get_valid_input(n)`**: Ensures the player’s input is a valid card choice from the dealer's hand.
- **`add_card_human(integer, dealer, human)`**: Adds a chosen card from the dealer’s deck to the player’s hand and updates the player’s deck.
- **`add_card_dealer(integer, dealer, human)`**: Adds a randomly selected card from the player’s deck to the dealer’s deck.
- **`play_game()`**: Main function to start and manage the game flow until one player loses.

## **How to Play**

1. Clone or download this repository.
2. Run the following code in a Python environment to start the game:
   ```python
   play_game()

## **Additional Resources**

Want to learn more about the rules and history of Old Maid? Check out this [link to the game](https://www.classicgamesandpuzzles.com/Old-Maid.html).
