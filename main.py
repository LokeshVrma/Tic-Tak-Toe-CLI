from sympy import true


print("             Tic Tak Toe             ")

locations = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]


def screen():
    print(f"{locations[0]} | {locations[1]} | {locations[2]} \n"
          f"--------- \n"
          f"{locations[3]} | {locations[4]} | {locations[5]} \n"
          f"--------- \n"
          f"{locations[6]} | {locations[7]} | {locations[8]} \n")

game_end = False


def check_winner():
    if locations[0] == locations[1] == locations[2]:
        return True
    elif locations[3] == locations[4] == locations[5]:
        return True
    elif locations[6] == locations[7] == locations[8]:
        return True
    elif locations[0] == locations[3] == locations[6]:
        return True
    elif locations[1] == locations[4] == locations[7]:
        return True
    elif locations[2] == locations[5] == locations[8]:
        return True
    elif locations[0] == locations[4] == locations[8]:
        return True
    elif locations[2] == locations[4] == locations[6]:
        return True


screen()

while not game_end:
    choices = ["x", "o"]

    player_1 = int(input("Player 1 Turn: "))
    player_1_index = locations.index(player_1)

    if player_1 in locations:
        if choices[0] != locations[player_1_index]:
            locations[player_1_index] = "x"

    screen()
    if check_winner():
        if locations.count("x") > locations.count("o"):
            print("Player 1 Won")
            game_end = True

        else:
            print("Player 2 Won")
            game_end = True

    else:
        player_2 = int(input("Player 2 Turn: "))
        player_2_index = locations.index(player_2)
        
        if player_2 in locations:
            if choices[1] != locations[player_2_index]:
                locations[player_2_index] = "o"
        
        screen()
