def print_sudoku(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                board[i][j]="_"
            m=f"{board[i][j]} "
            if (j+1)%3==0:
                m+=" "
            print(m,end="")
        print("")
        if (i+1)%3==0:
            print("")

def add_number(board,row,column,digit):
    board[row][column]=digit


if __name__ == "__main__":
    sudoku  = [
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]
              ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)