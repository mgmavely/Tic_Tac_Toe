import random

def board_print(posn):
    print("")
    print(str(posn[0]) + "|" + str(posn[1]) + "|" + str(posn[2]))
    print("-----")
    print(str(posn[3]) + "|" + str(posn[4]) + "|" + str(posn[5]))
    print("-----")
    print(str(posn[6]) + "|" + str(posn[7]) + "|" + str(posn[8]))
    print("")

def check_win(posn):
    if str(posn[0]) == str(posn[1]) and str(posn[1]) == str(posn[2]):
        return posn[0]
    elif str(posn[3]) == str(posn[4]) and str(posn[4]) == str(posn[5]):
        return posn[3]
    elif str(posn[6]) == str(posn[7]) and str(posn[7]) == str(posn[8]):
        return posn[6]
    elif str(posn[0]) == str(posn[3]) and str(posn[3]) == str(posn[6]):
        return posn[0]
    elif str(posn[1]) == str(posn[4]) and str(posn[4]) == str(posn[7]):
        return posn[1]
    elif str(posn[2]) == str(posn[5]) and str(posn[5]) == str(posn[8]):
        return posn[2]
    elif str(posn[0]) == str(posn[4]) and str(posn[4]) == str(posn[8]):
        return posn[0]
    elif str(posn[2]) == str(posn[4]) and str(posn[4]) == str(posn[6]):
        return posn[2]
    else:
        return "VOID"
    
print("Tic Tac Toe : Github @mgmavely")
print("Select Gamemode: Player vs Player [1] or Player vs Computer [2]")
gamemode = input()
turn = 1
count = 0
posns = [1,2,3,4,5,6,7,8,9]
aiposns = [1,2,3,4,5,6,7,8,9]

if gamemode == "1":
    print("Player vs Player selected")
    while True:
        if count == 9:
            print("It's a tie")
            break
        print("")
        print("Player " + str(turn) + "'s turn")
        board_print(posns)
        inp = input()
        for i in range(len(posns)):
            cond = 0
            if str(inp) == str(posns[i]):
                if turn == 1:
                    cond = 1
                    posns[i] = "X"
                    turn = 2
                    break
                elif turn == 2:
                    cond = 1
                    posns[i] = "O"
                    turn = 1
                    break
        if cond == 0:
            print("Illegal Move, Try again!")

        w = check_win(posns)
        if w == "O":
            board_print(posns)
            print("Player 2 Wins!")
            break
        elif w == "X":
            board_print(posns)
            print("Player 1 Wins!")
            break
        count += 1
elif gamemode == "2":
    print("Player vs Computer selected")
    while True:
        if count == 9:
            print("It's a tie")
            break
        print("")
        if turn == 1:
            print("Player 1's turn")
            board_print(posns)
            inp = input()
            for i in range(len(posns)):
                cond = 0
                if str(inp) == str(posns[i]):
                    cond = 1
                    aiposns.remove(posns[i])
                    posns[i] = "X"
                    turn = 2
                    break
        if cond == 0:
            print("Illegal Move, Try again!")

        w = check_win(posns)
        if w == "O":
            board_print(posns)
            print("Player 2 Wins!")
            break
        elif w == "X":
            board_print(posns)
            print("Player 1 Wins!")
            break
        count += 1
        
        if turn == 2:
            rnd = random.choice(aiposns)
            posns[int(rnd) - 1] = "O"
            aiposns.remove(rnd)
            turn = 1
        
else:
    print("Invalid gamemode selection, Goodbye!")



    
                
