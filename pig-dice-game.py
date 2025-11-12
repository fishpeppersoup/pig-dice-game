



# make an interactive game played by a user and a computer
import random
roll_ouput = random.randint(1, 6)

# create variables to store the total score of each player
total_score1 = 0
total_score2 = 0

# create variable to store the sum of the output of the rolls
roll_sum = 0

# create a loop that let's the game run until the total score of any player is greater than or equal to 100
flag = True
while flag and total_score1 < 100 and total_score2 < 100:
# print initial score of both players

    print("Player One's score:", total_score1)
    print("Computer's score:", total_score2)

# assign flags for player 1 and indicate who's turn it is
    flag = True
    flag_player1 = True
    print("")
    print("It's Player One's turn")
    while (flag_player1):

# request input from user and determine what the input does
        user_input = input("Would you like to roll or hold. Enter 'r' or 'h': ")

# if user enters "r" roll die and print output
        if user_input == "r":
            roll_output = random.randint(1, 6)
            print("rolled a", roll_output)

# if the roll output is 1, the loop ends and turn score equals 0
# print out the turn score of player 1 and total score of each player
            if roll_output == 1:
                print("Pigged out!")
                roll_sum = roll_sum * 0
                print("Turn score = ", roll_sum)
                print("Total score =", total_score1)
                print("")
                print("Player One's score:", total_score1)
                print("Computer's score:", total_score2)
                flag_player1 = False

# else sum up the output of the rolls
            else:

                roll_sum = roll_sum + roll_output

# ensure the loop ends if total score is greater than or equal to 100
                if total_score1 + roll_sum >= 100:
                    total_score1 = total_score1 + roll_sum
                    print("Turn score = ", roll_sum)
                    print("Total score =", total_score1)
                    print("")
                    flag_player1 = False
                    flag = False

# end loop if the user enters 'h' to hold and print the turn score for the user
# print total score of each player
        elif user_input == "h":
            total_score1 = total_score1 + roll_sum
            print("Turn score = ", roll_sum)
            print("Total score =", total_score1)
            print("")
            roll_sum = 0
            print("Player One's score:", total_score1)
            print("Computer's score:", total_score2)
            flag_player1 = False

# ensure the loop ends if total score of any player is greater than or equal to 100
    if flag:
        if total_score1 >= 100:
            flag = False

        if total_score2 >= 100:
            flag = False

# assign flag to player 2 and indicate their turn
    if flag:
        flag_player2 = True
        print("")
        print("It's Computer's turn")

# roll die for player 2 and follow same conditions for the roll outputs
        while (flag_player2):
            roll_output = random.randint(1, 6)
            print("rolled a", roll_output)
            if roll_output == 1:
                print("Pigged out!")
                roll_sum = roll_sum * 0
                flag_player2 = False

            else:
                roll_sum = roll_sum + roll_output

# ensure the loop ends if sum of rolls is greater than or equal to 20
# ensure the loop ends if total score is greater than or equal to 100
            if roll_sum >= 20:
                flag_player2 = False

            if total_score2 + roll_sum >= 100:
                flag_player2 = False
                flag = False

# calculate the total score for player 2
# print the turn score and the total score
        total_score2 = total_score2 + roll_sum
        print("Turn score = ", roll_sum)
        print("Total score =", total_score2)
        print("")
        roll_sum = 0

# make loop end if the total score of any player is greater than or equal to 100
        if flag:
            if total_score1 >= 100:
                flag_player2 = False

            if total_score2 >= 100:
                flag_player2 = False


# print the final score of each player
# print the winner
print("Final Score", total_score1, "vs", total_score2)
print("")
if total_score1 > total_score2:
    print("Player One Wins!")
else:
    print("Computer Wins!")
