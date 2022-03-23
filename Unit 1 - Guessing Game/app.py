import random
import statistics as st


def start_game():
    ## Pre reqs ##
    answer = random.randint(1, 100)
    total = []
    count = 0
    highscore = [15]
    ### Game Starts ###
    print(
        f"""
            ***********************************
               Welcome to Guess That Number!
            ***********************************
            
\nThe highscore to beat is {highscore[0]}.""")
    game = True
    while game:
        guess = input("Enter a number between 1 and 100"
                      "\n")
        ### Error try block ###
        try:
            guess = int(guess)
            if guess not in range(1, 101):
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
            if count < highscore[0]:
                highscore.pop(0)
                highscore.append(count)
                print(highscore)
                print(f"Well done! Your new highscore is {highscore[0]}")
            elif count >= highscore[0]:
                print(f"The highscore to beat is {highscore[0]}")




            confirm = input("Would you like to play again? Anything said other than 'yes' will end the game.\n")
            if confirm == "yes":
                total.append(count)
                if count < highscore[0]:
                    highscore.pop(0)
                    highscore.append(count)
                    print(highscore)
                count = 0
                next_answer = random.randint(1, 100)
                answer = next_answer
                continue
            else:
                total.append(count)
                print(
                    f"""
                    \nThanks for playing! Here is some stats for you.
Current Highscore: {highscore[0]}                    
Total Attempts: {sum(total)}
Average Attempts: {st.mean(total)}
Median: {st.median(total)}
Mode: {st.mode(total)}
                    """)
                game = False





start_game()