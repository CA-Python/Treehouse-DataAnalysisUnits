import random

def start_game():
    answer = random.randint(1, 100)
    print(answer)
    guesses = 0
    print(
        """
            *****************************

            Welcome to Guess That Number!

            *****************************
        """)
    while True:
        input('Pick a number from 1 to 100'
              '\n'
              '\n   ')

start_game()

"""Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """