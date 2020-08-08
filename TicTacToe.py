display_list = ['1','2','3','4','5','6','7','8','9']
player_1 = ''
player_2 = ''
choice_1 = 'Z'
choice_2 = ''
used_positions = []

# Display Board
def display_board():
    print(" ------- ------- -------")
    print("|       |       |       |")
    print(f"|   {display_list[6]}   |   {display_list[7]}   |   {display_list[8]}   |")
    print("|       |       |       |")
    print(" ------- ------- -------")
    print("|       |       |       |")
    print(f"|   {display_list[3]}   |   {display_list[4]}   |   {display_list[5]}   |")
    print("|       |       |       |")
    print(" ------- ------- -------")
    print("|       |       |       |")
    print(f"|   {display_list[0]}   |   {display_list[1]}   |   {display_list[2]}   |")
    print("|       |       |       |")
    print(" ------- ------- -------")

# Ask Player1's name and Player2's name and enter Player1's Choice & Player2's choice [X or O]
def get_names_and_chosen_symbols():
    global player_1 
    player_1 = input("Enter Player 1's name: ")
    global player_2 
    player_2 = input("Enter Player 2's name: ")
    global choice_1
    global choice_2
    while choice_1 not in ['X','O']:
        choice_1 = input("Enter player 1's choice: X or O ").upper()
        if choice_1 not in ['X','O']:
            print("Sorry! Only options are X or O ")
    
    if choice_1 == 'X':
        choice_2 = 'O'
    else:
        choice_2 = 'X'
    print(f"Since {player_1} chose {choice_1}, {player_2} gets {choice_2}")

# Keep getting player's and update display_list
def get_input_update_list(player):
    position = 'random'
    within_range = False
    while position.isdigit == False or within_range == False :
        position = input("Choose the position on the board [1-9]: ")
        if position.isdigit() == False:
            print("Sorry! Not a valid input. Enter a number as position between 1-9 ")
        else:
            if int(position) not in range(1,10):
                print("Sorry! The number you entered is out of range. Enter number between 1-9")
            elif int(position) in used_positions:
                print("Sorry! This position was already entered previously. Choose another number between 1-9")
            elif int(position) in range(1,10) and int(position) not in used_positions:
                within_range = True
                used_positions.append(int(position))
    position = int(position)
    if player == player_1:
        display_list[position-1] = choice_1
    else:
        display_list[position-1] = choice_2

def check_winning_condition():
    winning_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for pos1,pos2,pos3 in winning_combinations:
        if display_list[pos1-1] == choice_1 and display_list[pos2-1] == choice_1 and display_list[pos3-1]==choice_1:
            print(f"Yayyyyyyy! {player_1} WINS!!!! :D")
            print(f"Sorry {player_2} :( Better luck next time :)")
            return 1
        elif display_list[pos1-1] == choice_2 and display_list[pos2-1] == choice_2 and display_list[pos3-1]==choice_2:
            print(f"Yayyyyyyy! {player_2} WINS!!!! :D")
            print(f"Sorry {player_1} :( Better luck next time :)")
            return 1
    else:
        return 0

def start_game():
    print("\n\n\nHello! Welcome, Welcome, Welcome!!! To the grand Tic Tac Toe Challenge")
    print("\n\nThe rules are fairly simple and you probably know them already. But let me walk you through them anyway.")
    print("We have two players and each gets to choose among 'X' or 'O'. If any player manages to mark his/her symbol for three contiguious locations on this grid, he/she WINS")
    print("\nLet's start! Shall we?\n")
    get_names_and_chosen_symbols()
    print("This is the initial board")
    display_board()
    flag = 0
    for i in range(0,9):
        if flag == 0:
            if i % 2 == 0:
                print(f"{player_1}'s turn")
                get_input_update_list(player_1)
            else:
                print(f"{player_2}'s turn")
                get_input_update_list(player_2)
            display_board()
            flag = check_winning_condition()
        if flag == 0 and i == 8:
            print("No one wins :( Start over!")

start_game()

