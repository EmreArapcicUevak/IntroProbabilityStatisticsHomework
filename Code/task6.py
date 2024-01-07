import random

# Set the winning and losing amounts as constants
WIN_AMOUNT = 2
LOSE_AMOUNT = 1.5

def play_dice_game(starting_balance):
    balance = starting_balance
    roll_count = 0

    while balance > 0:
        roll_count += 1
        input("Press enter to throw the dice.")

        dice_roll = random.randint(1, 6), random.randint(1, 6)
        dice_total = sum(dice_roll)
        roll_is_even = dice_total % 2 == 0

        # Player wins if the dice roll total is even
        if roll_is_even:
            balance += WIN_AMOUNT
            outcome = "won"
            amount_changed = WIN_AMOUNT
        # Player loses if the dice roll total is odd
        else:
            balance = max(balance - LOSE_AMOUNT, 0)  # Prevent negative balance
            outcome = "lost"
            amount_changed = LOSE_AMOUNT

        # Print the results of the current roll
        print(f"Roll Number: {roll_count}, Dice1: {dice_roll[0]}, Dice2: {dice_roll[1]}, "
              f"You {outcome} {amount_changed}, Current balance: {balance}")

    # Game over message
    print(f"Game over. You lasted {roll_count} roll(s).")

# Prompt the player to enter their initial balance
initial_balance = int(input("Please enter the initial amount of money: "))
play_dice_game(initial_balance)
