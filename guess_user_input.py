# A guessing game
# import random


# def guess_user_input():
#     # random = random.randint(100) #Variable Name Conflict (random = random.randint(...)) 
#     # plus Wrong randint() Usage
#     secret_number = random.randint(1, 100)
#     limit = 3
#     # You're subtracting limit from user_guess, which makes no sense logically
#     # Better Approach:
#     # Use a loop to allow up to limit attempts.
#     # Track how many attempts were used.
#     attepmts = user_guess - limit
#     # You should get input, convert to int, and not print inside the assignment:
#     # user_guess = print(input('Guess the number between 1 and 100:')) #You're assigning user_guess to the result of print(...), which is None.
#     user_guess = int(input('Guess the number between 1 and 100:'))
#     # Logic Errors in Loop
#     # 'is not' compares object identity, not value.
#     # You should be comparing the value, and also tracking attempts.
#     while user_guess is not secret_number:
#         if user_guess < secret_number and user_guess < attepmts:
#             print(int(input('Too low! Try again:')))
#             print((f'You have {attepmts} attempts left'))
#         elif user_guess > secret_number and user_guess < attepmts:
#             print(int(input('Too high! Try again:')))
#             print((f'You have {attepmts} attempts left'))
#     else:
#         print(
#             input(f'Congratulations! You guessed it in {attepmts} attempts:'))
#         print((f'HUrrayy; You have completed it in {attepmts} attempts!!!'))
#     return


# guess_user_input()


# ✅ Better Approach:
# Use a loop to allow up to limit attempts.
# Track how many attempts were used.
# A guessing game

# import random

# def guess_user_input():
#     secret_number = random.randint(1, 100)
#     limit = 5

#     for attempt in range(1, limit + 1):
#         try:
#             user_guess = int(input(f'Attempt {attempt}: Guess the number between 1 and 100: '))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if user_guess == secret_number:
#             print(f'🎉 Congratulations! You guessed it in {attempt} attempt(s)!')
#             break
#         elif user_guess < secret_number:
#             print('Too low! Try again.')
#         else:
#             print('Too high! Try again.')

#         if attempt == limit:
#             print(f'Sorry, you have used all {limit} attempts. The number was {secret_number}.')

# guess_user_input()


# User chooses easy or hard.
# The game loops until the user quits.
# Keeps track of how many times the user guessed correctly.

import random

def guess_user_input():
    print("🎯 Welcome to the Number Guessing Game!")

    score = 0  # Track the number of successful guesses

    while True:
        # Choose difficulty level
        difficulty = input("Choose difficulty level (easy/hard): ").lower()
        if difficulty == 'easy':
            limit = 5
        elif difficulty == 'hard':
            limit = 3
        else:
            print("Invalid input. Defaulting to hard mode.")
            limit = 3

        secret_number = random.randint(1, 100)
        print(f"\nI'm thinking of a number between 1 and 100. You have {limit} attempts.")

        for attempt in range(1, limit + 1):
            try:
                user_guess = int(input(f'Attempt {attempt}: Enter your guess: '))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if user_guess == secret_number:
                print(f'🎉 Correct! You guessed it in {attempt} attempt(s).')
                score += 1
                break
            elif user_guess < secret_number:
                print('📉 Too low!')
            else:
                print('📈 Too high!')

            if attempt == limit:
                print(f'❌ You ran out of attempts. The number was {secret_number}.')

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\n🏁 Game Over! You won {score} time(s). Thanks for playing!")
            break

# Start the game
guess_user_input()
