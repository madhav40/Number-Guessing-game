import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Difficulty level selection
    print("Select difficulty level:")
    print("1. Easy (Unlimited attempts)")
    print("2. Medium (10 attempts)")
    print("3. Hard (5 attempts)")
    difficulty = input("Enter 1, 2, or 3: ")
    
    if difficulty == '1':
        max_attempts = float('inf')  # Infinite attempts
    elif difficulty == '2':
        max_attempts = 10
    elif difficulty == '3':
        max_attempts = 5
    else:
        print("Invalid input. Defaulting to Easy.")
        max_attempts = float('inf')
    
    # Generate random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while attempts < max_attempts:
        try:
            user_guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low, try again!")
            elif user_guess > number_to_guess:
                print("Too high, try again!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
        
        if attempts == max_attempts:
            print(f"Game Over! You've used all {max_attempts} attempts. The number was {number_to_guess}.")
    
    # Option to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()
    else:
        print("Thanks for playing!")

# Start the game
number_guessing_game()
