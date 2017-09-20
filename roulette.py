"""Roulette Game."""
# just imports randint into memory
from random import randint
# imports all of randit
import random

bank_account = 1000

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 29, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def which_bet():
    """Ask the user which bet selection they want to make."""
    answer = ""
    while answer != "number" and answer != "color" and answer != "both":
        print("Would you like to bet on a number, color, or both?")
        answer = input()
    return answer


def take_bet_amount():
    """Take in betting amount, and validate infomration."""
    bet_amount = 0
    while bet_amount <= 0 or bet_amount >= bank_account:
        print("How much would you like to bet?")
        bet_amount = int(input())
    return bet_amount


def take_bet_number():
    """Take in betting number, and validate information."""
    bet_number = 40
    while bet_number > 37 or bet_number < 0:
        print("Which number would you like to bet on?")
        bet_number = input()
        if bet_number == "00":
            bet_number = 37
        else:
            bet_number = int(bet_number)
    return bet_number


def take_bet_color():
    """Take in betting color, and validate infomration."""
    bet_color = ""
    while bet_color != "black" and bet_color != "red" and bet_color != "green":
        print("Which color would you like to bet on?")
        bet_color = input()
    return bet_color


def roll_ball():
    """Return a random number between 0 and 37."""
    ball_number = random.randint(0, 37)
    return 2


def check_results_color(ball_number, bet_color):
    """Return comparisons between player's and random's color."""
    try:
        if green.index(ball_number) >= 0:
            ball_color = "green"
    except:
        pass
    try:
        if red.index(ball_number) >= 0:
            ball_color = "red"
    except:
        pass
    try:
        if black.index(ball_number) >= 0:
            ball_color = "black"
    except:
        pass
    print("The ball landed on " + ball_color)
    if bet_color == ball_color:
        if bet_color == "green":
            return "green_won"
        else:
            return "color_won"
    else:
        return "color_lost"


def check_results_number(ball_number, bet_number):
    """Prints number roll and returns comparison with player's number."""
    print("The ball landed on " + str(ball_number))
    if bet_number == ball_number:
        return "number_won"
    else:
        return "number_lost"


def payout(bet_amount, result):
    """Return total amount won or lost by user based on check_results."""
    global bank_account
    if result == "green_won":
        bank_account += bet_amount * 17
        return "You won: $" + str(bet_amount * 17)
    elif result[0] == "n":
        if result == "number_lost":
            bank_account -= bet_amount
            return "You lost: $" + str(bet_amount)
        else:
            bank_account += bet_amount * 35
            return "You won: $" + str(bet_amount * 35)
    else:
        if result == "color_lost":
            bank_account -= bet_amount
            return "You lost: $" + str(bet_amount)
        else:
            bank_account += bet_amount
            return "You won: $" + str(bet_amount)


def play_again():
    """Checks if the player wants to play again."""
    print("Would you like to keep playing?")
    again = input()
    if again == "yes":
        play_game()
    elif again == "no":
        print("You left with $" + str(bank_account))
    else:
        print("Was that a 'yes' or a 'no'?")
        play_game()


def play_game():
    """All of the funtions to play the game."""
    bet_type = which_bet()
    if bet_type == "number":
        print("bank account:" + str(bank_account))
        bet_amount_number = take_bet_amount()
        bet_number = take_bet_number()
        ball_roll = roll_ball()
        number_result = check_results_number(ball_roll, bet_number)
        print(payout(bet_amount_number, number_result))
        print("bank account:" + str(bank_account))
    if bet_type == "color":
        print("bank account:" + str(bank_account))
        bet_amount_color = take_bet_amount()
        bet_color = take_bet_color()
        ball_roll = roll_ball()
        color_result = check_results_color(ball_roll, bet_color)
        print(payout(bet_amount_color, color_result))
        print("bank account:" + str(bank_account))
    if bet_type == "both":
        print("bank account:" + str(bank_account))
        print("For your bet on the number:")
        bet_amount_number = take_bet_amount()
        bet_number = take_bet_number()
        print("For your bet on the color:")
        bet_amount_color = take_bet_amount()
        bet_color = take_bet_color()
        ball_roll = roll_ball()
        number_result = check_results_number(ball_roll, bet_number)
        color_result = check_results_color(ball_roll, bet_color)
        print(payout(bet_amount_number, number_result))
        print(payout(bet_amount_color, color_result))
        print("bank account: " + str(bank_account))
    play_again()


play_game()
