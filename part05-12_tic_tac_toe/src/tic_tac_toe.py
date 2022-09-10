def play_turn(board,row,column,symbol):
    boundary=[0,1,2]
    if row not in boundary or column not in boundary:
        return False
    if board[column][row]=="":
        board[column][row]=symbol
        return True
    return False
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 11, 2, "0"))
    print(game_board)