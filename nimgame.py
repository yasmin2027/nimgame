import math
import random 

#Function to check the validity of the number of coins.
def valid_n_coins():
    while True:
        try:
            n_coins = int(input("Enter the number of coins: "))
            if n_coins <= 0:
                raise ValueError("Please enter a positive integer.")
            return n_coins
        except ValueError as ve:
            print(ve)
#Function to check the validity of the number of move.
def valid_move(player, n_coins):
    while True:
        try:
            move = int(input(f"{player}: Please take a square number: "))
            if move <= 0:
                raise ValueError("Please enter a positive integer.")
            elif math.sqrt(move) != int(math.sqrt(move)):
                raise ValueError("Please enter a perfect square.")
            elif move > n_coins:
                raise ValueError("You cannot take more coins than available.")
            return move
        except ValueError as ve:
            print(ve)

def main():
    # Welcome message and display status
    print("Welcome to the game")
    
    # Select the number of coins
    choice = input("Enter A or B: ")
    if choice == 'A':
        n_coins = valid_n_coins()
    else:
        while True:
            n_coins = random.randint(10, 1000)
            if math.sqrt(n_coins) != int(math.sqrt(n_coins)):
                break
            print("Error! please enter another number")
    
    # Game playing
    while n_coins > 0:
        move = valid_move("Player_1", n_coins)
        n_coins -= move    
        print("Now we have:", n_coins)
        if n_coins == 0:
            print("Player_1 is the winner")
            break
        
        move = valid_move("Player_2", n_coins)
        n_coins -= move
        print("Now we have:", n_coins)
        if n_coins == 0:
            print("Player_2 is the winner")
            break

main()  
