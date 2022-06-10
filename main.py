import random

print("Welcome to the Rock Paper Scissors game. You will be playing against the CPU(Computer). Take note of the following rules below;")
print('''
Rock smashes Scissors
Paper covers Rock
Scissors cut Paper
1. It is a Tie when you and Computer picks the same option
2. You win if you smash/cover/cut Computer's option; Computer loses
3. Computer wins if it smashes/covers/cut your option; You lose.

The GAME BEGINS NOW! ''')

player_option = ["R", "P", "S"]
cpu_option = ["R", "P", "S"]


def player_choice():
    player_action = input('''Pick from the following Option;
 "R" for "Rock",
 "P" for "Paper",
 "S" for "Scissors" \n''')
    player_action = player_action.upper()

    if player_action in player_option:
        # print("You chose: ", player_action)
        return player_action
    else:
        print("Invalid input!")
    return player_choice()


def cpu_choice():
    cpu_action = random.choice(cpu_option)
    cpu_action = cpu_action.upper()
    # print("Cpu chose: %s" % cpu_action)
    return cpu_action


def option_selection():
    player_wins = 0
    cpu_wins = 0
    tie_score = 0

    while True:
        player_action = player_choice()
        cpu_action = cpu_choice()

        print("Player (", player_action, ") : CPU (", cpu_action, ")")

        if player_action == cpu_action:
            print("\nIts a tie!")
            tie_score += 1
            return option_selection()

        elif player_action == "R":
            if cpu_action == "S":
                # print("\n")
                print(player_action.upper(), "(Rock) smashes ",
                      cpu_action.upper(), "(Scissors), You win!")
                player_wins += 1
            else:
                print("\n")
                print(cpu_action.upper(), "(Paper) covers",
                      player_action.upper(), "(Rock), You lose!")
                cpu_wins += 1
        elif player_action == "P":
            if cpu_action == "R":
                print("\n")
                print(player_action.upper(), "(Paper) covers",
                      cpu_action.upper(), "(Rock), You win!")
                player_wins += 1
            else:
                print("\n")
                print(cpu_action.upper(), "(Scissors) cuts",
                      player_action.upper(), "(Paper), You lose!")
                cpu_wins += 1
        elif player_action == "S":
            if cpu_action == "P":
                print("\n")
                print(player_action.upper(), "(Scissors) cuts",
                      cpu_action.upper(), "(Paper), You win!")
                player_wins += 1
            else:
                print("\n")
                print(cpu_action.upper(), "(Rock) smashes",
                      player_action.upper(), "(Scissors), You lose!")
                cpu_wins += 1
            print("Game Over!")
        else:
            print("Invalid selection")

        print("")
        print("Tie score: %s" % tie_score)
        print("Player's score: %s" % player_wins)
        print("Computer's score: %s" % cpu_wins)

        break

        # print("\n")
        # print("Would you want to play again?")

        # replay = input("Choose 'Y' for 'Yes' and 'N' for 'No' \n").lower()

        # if replay == "y":
        #     print("Okay Cool!\n")

        # elif replay == "n":
        #     print("Bye! See You later")
        #     break
        # else:
        #     print("Invalid Option, \n")
        #     return option_selection()


option_selection()
