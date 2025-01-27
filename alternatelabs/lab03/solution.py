import random

# Set up some global 'constants'
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = f'Please guess a number between {MIN_VALUE} and {MAX_VALUE}: '

# Set up variables to be used in the game
game_over = False

while not game_over:
    # Initialise the number to be guessed - includes both end points
    number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    # Start the game
    print('Welcome to the number guess game')

    # Obtain their initial guess
    number_not_guessed = True
    while number_not_guessed and count_number_of_tries < MAX_NUMBER_OF_GUESSES:
        guess = int(input(GUESS_PROMPT))

        # Check if the user requested to reveal the number
        if guess == -1:
            print(f'The number to guess is {number_to_guess}')
            continue

        # Increment the attempt counter
        count_number_of_tries += 1

        # Check the guess and provide feedback
        if guess == number_to_guess:
            print('Well done, you won!')
            print(f'You took {count_number_of_tries} guesses to complete the game')
            number_not_guessed = False  # Exit the inner loop
        elif abs(guess - number_to_guess) == 1:
            print('Sorry, wrong number - you were out by 1')
        elif guess < number_to_guess:
            print('Sorry, wrong number. Your guess was lower than the number.')
        elif guess > number_to_guess:
            print('Sorry, wrong number. Your guess was higher than the number.')

    # If the player runs out of guesses
    if number_not_guessed:
        print("Sorry - you lose")
        print(f'The number you needed to guess was {number_to_guess}')

    # Ask if the player wants to play again
    input_not_accepted = True
    while input_not_accepted:
        play_again = input("Do you want to play again (y/n) or (yes/no)? ").lower()
        if play_again in ('n', 'no'):
            game_over = True
            input_not_accepted = False
        elif play_again in ('y', 'yes'):
            input_not_accepted = False
        else:
            print('Invalid input. Must be y/n or yes/no.')

print('Game Over')
