import random

space = " "
line = "|"
playerone = 1
playertwo = 2
playerones = []
playertwos = []
comps = []
wina = [1,4,7]
winb = [2,5,8]
winc = [3,6,9]
wind = [1,2,3]
wine = [4,5,6]
winf = [7,8,9]
wing = [1,5,9]
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("NEW GAME")
print('\n')
print(str(board[0]) + line + str(board[1]) + line + str(board[2]))
print("-"*5)
print(str(board[3]) + line + str(board[4]) + line + str(board[5]))
print("-"*5)
print(str(board[6]) + line + str(board[7]) + line + str(board[8]))
print('\n')

def play_one():
    print("playerone's turn")
    playerone = int(input())
    if playerone > 10 or playerone < 1:
        print("False move")
        print("-"*10)
        play_one()

    print('\n')
    for num in comps:
        if num == playerone:
            print("False move")
            print("-"*10)
            play_one()
    for num in playerones:
        if num == playerone:
            print("False move")
            print("-"*10)
            play_one()
    for num in board:
        if num == playerone:
            board[playerone-1] = "O"
            playerones.append(playerone)
    print('\n')
    print(str(board[0]) + line + str(board[1]) + line + str(board[2]))
    print("-"*5)
    print(str(board[3]) + line + str(board[4]) + line + str(board[5]))
    print("-"*5)
    print(str(board[6]) + line + str(board[7]) + line + str(board[8]))
    print('\n')

    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        print("Playerone wins")
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        print("Playerone wins")
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        print("Playerone wins")
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        print("Playerone wins")
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        print("Playerone wins")
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        print("Playerone wins")
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        print("Playerone wins")
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        print("Playerone wins")
    else:
        comp()

# def play_two():
#     print("playertwo's turn")
#     playertwo = int(input())
#     if playertwo > 10 or playertwo < 1:
#         print("False move")
#         print("-"*10)
#         play_two()
#     for num in playerones:
#         if num == playertwo:
#             print("False move")
#             print("-"*10)
#             play_two()
#     for num in playertwos:
#         if num == playertwo:
#             print("False move")
#             print("-"*10)
#             play_two()
#
#     for num in board:
#         if num == playertwo:
#             board[playertwo-1] = "X"
#             playertwos.append(playertwo)
#     print('\n')
#     print(str(board[0]) + line + str(board[1]) + line + str(board[2]))
#     print("-"*5)
#     print(str(board[3]) + line + str(board[4]) + line + str(board[5]))
#     print("-"*5)
#     print(str(board[6]) + line + str(board[7]) + line + str(board[8]))
#     print('\n')
#     if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
#         print("Playertwo wins")
#     elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
#         print("Playertwo wins")
#     elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
#         print("Playertwo wins")
#     elif board[0] == 'X' and board[3] == 'X' and board[7] == 'X':
#         print("Playertwo wins")
#     elif board[1] == 'X' and board[4] == 'X' and board[6] == 'X':
#         print("Playertwo wins")
#     elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
#         print("Playertwo wins")
#     elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
#         print("Playertwo wins")
#     elif board[2] == 'X' and board[4] == 'X' and board[7] == 'X':
#         print("Playertwo wins")
#     else:
#         play_one()

def comp():
    moves = [1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9]
    # or board[2] == 'O' and board[1] == 'O' or board[0] == 'O' and board[2]

        # for num in board:
            # if num == 1:
    if board[0] == 'O' and board[1] == 'O':
        board[2] = "X"
    elif board[2] == 'O' and board[1] == 'O':
        board[0] = "X"
    elif board[0] == 'O' and board[2] == 'O':
        board[1] = "X"
    elif board[3] == 'O' and board[4] == 'O':
        board[5] = "X"
    elif board[4] == 'O' and board[5] == 'O':
        board[3] = "X"
    elif board[3] == 'O' and board[5] == 'O':
        board[4] = "X"
    elif board[6] == 'O' and board[7] == 'O':
        board[8] = "X"
    elif board[7] == 'O' and board[8] == 'O':
        board[6] = "X"
    elif board[6] == 'O' and board[8] == 'O':
        board[7] = "X"
    elif board[0] == 'O' and board[3] == 'O':
        board[6] = "X"
    elif board[3] == 'O' and board[6] == 'O':
        board[0] = "X"
    elif board[0] == 'O' and board[6] == 'O':
        board[3] = "X"
    elif board[1] == 'O' and board[4] == 'O':
        board[7] = "X"
    elif board[4] == 'O' and board[7] == 'O':
        board[1] = "X"
    elif board[1] == 'O' and board[7] == 'O':
        board[4] = "X"
    elif board[2] == 'O' and board[5] == 'O':
        board[8] = "X"
    elif board[5] == 'O' and board[8] == 'O':
        board[2] = "X"
    elif board[2] == 'O' and board[8] == 'O':
        board[5] = "X"
    elif board[2] == 'O' and board[4] == 'O':
        board[6] = "X"
    elif board[4] == 'O' and board[6] == 'O':
        board[2] = "X"
    elif board[2] == 'O' and board[6] == 'O':
        board[4] = "X"
    elif board[0] == 'O' and board[4] == 'O':
        board[8] = "X"
    elif board[4] == 'O' and board[8] == 'O':
        board[0] = "X"
    elif board[0] == 'O' and board[8] == 'O':
        board[4] = "X"
    else:
        comp_move = random.choice(moves)

        for num in playerones:
            if num == comp_move:
                print("False move")
                print("-"*10)
                comp()

        for num in comps:
            if num == comp_move:
                print("False move")
                print("-"*10)
                comp()

        for num in board:
            if num == comp_move:
                board[comp_move-1] = "X"
                comps.append(comp_move)

    print('\n')
    print(str(board[0]) + line + str(board[1]) + line + str(board[2]))
    print("-"*5)
    print(str(board[3]) + line + str(board[4]) + line + str(board[5]))
    print("-"*5)
    print(str(board[6]) + line + str(board[7]) + line + str(board[8]))
    print('\n')
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        print("Computer wins")
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        print("Computer wins")
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        print("Computer wins")
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        print("Computer wins")
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print("Computer wins")
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        print("Computer wins")
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        print("Computer wins")
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        print("Computer wins")
    else:
        play_one()




play_one()
