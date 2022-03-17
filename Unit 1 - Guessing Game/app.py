import random
import statistics as st

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
            if guess not in range(1,101):
                count += 0
                raise ValueError
        except ValueError as err:
            err = print("Please enter a number that is between 1 and 100, try again\n"
                        "\nThis does not count towards your attempts, mistakes happen :)")
            continue

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



            confirm = input("Would you like to play again? Anything said other than 'Yes' will end the game.\n")
            if confirm == "yes":
                total.append(count)
                next_answer = random.randint(1, 100)
                answer = next_answer
                continue
            else:
                total.append(count)
                print(
                    f"""
                    \nThanks for playing! Here is some stats for you.
                    
                    \nTotal Attempts: {sum(total)} \nAverage Attempts: {st.mean(total)}
                    """)
                break


start_game()
