from random import randint

print("Rock".lower())
print("paper".lower())
print("Scissors".lower())
print("wellcome To this Game")
print("---------------------")

pcMove = randint(0, 2)
if pcMove == 0:
    player_2 = "rock"
elif pcMove == 1:
    player_2 = "paper"
elif pcMove == 2:
    player_2 = "scissors"

player_1_win = 0
player_2_win = 0
rounds = float(input("How Many round do you want to play ???"))

while player_1_win < rounds and player_2_win < rounds:

    player_1 = input("what is your choise PLAYER 1 ? ").lower()
    print(f"PLAYER 2 : {player_2} ")
    print("")

    if player_1 == player_2:
        print(" you have same idea! Do this round again ...")

    elif player_1 == "rock":
        if player_2 == "paper":
            print("P 2 have PAPER so win this round")
            player_2_win += 1
        elif player_2 == "scissors":
            print("P 2 have SCIEEORS so YOU win this round !")
            player_1_win += 1
    elif player_1 == "paper":
        if player_2 == "rock":
            print("P 2 have ROCK so  YOU win this round !")
            player_1_win += 1
        elif player_2 == "scissors":
            print("P 2 have SCIEEORS so win this round")
            player_2_win += 1
    elif player_1 == "scissors":
        if player_2 == "paper":
            print("P 2 have PAPER so  YOU win this round !")
            player_1_win += 1
        elif player_2 == "rock":
            print("P 2 have ROCK so win this round")
            player_2_win += 1

    else:
        print(" SOME THING IS WRONG BRO !!!")

    if player_1 == "exit" or player_1 == "q":
        break
        print("this is END / Bye ...")

if player_1_win > player_2_win:
    winner = "you"
elif player_1_win < player_2_win:
    winner = "PC"
print("--------------------------------------------------------------------------------")
print(f"at the end you have {player_1_win} and pc have {player_2_win} . so {winner} WIN !")
