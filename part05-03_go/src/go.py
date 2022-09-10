def who_won(board):
    check1=0
    check2=0
    for row in board:
        for element in row:
            if element==1:
                check1+=1
            elif element==2:
                check2+=1
    if check1>check2:
        return 1
    elif check1==check2:
        return 0
    return 2

if __name__ == "__main__":
    game_board=[[0,1,2,0],
                [1,0,0,1],
                [0,2,1,2],
                [0,0,1,2]]
    print(who_won(game_board))