import random
import statistics


def start_game():
    ## Pre reqs ##
    answer = random.randint(1, 100)
    total = []
    count = 0

    ### Game Starts ###
    print(
        """
            ***********************************

               Welcome to Guess That Number!

            ***********************************
        """)
    game = True
    while game:
        guess = input("Enter a number between 1 and 100"
                      "\n")
        ### Error try block ###
        try:
            guess = int(guess)
            if guess not in range(1,100):
                raise ValueError
        except ValueError as err:
            err = print("\nPlease enter a number that is between 1 and 100, try again")
            start_game()

        ### Guess conditions ###
        if guess > answer:
            print(f"{guess} is higher than the answer, try again...")
            count += 1
        elif guess < answer:
            print(f"{guess} is lower than the answer, try again...")
            count += 1
        elif guess == answer:
            count += 1
            print(f"Well done you made {count} attempt(s) this time!\n")


            confirm = input("Would you like to play again? Anything you say that is not 'Yes' will end the game.\n")
            if confirm == "yes":
                start_game()
            else:
                total.append(count)
                print("Here is your overall stats after this game!"
                      f"\nTotal Attempts: {total[0:]} \nAverage Score: \n"
                      "\nThank you for playing! Goodbye!")

            break





start_game()
