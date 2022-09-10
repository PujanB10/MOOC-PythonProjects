def block_correct(board,row,column):
    numbers=[]
    for i in range(row,row+3):
        for j in range(column,column+3):
            if board[i][j]>0 and board[i][j] in numbers:
                return False
            numbers.append(board[i][j])
    return True    

    
if __name__ == "__main__": 
    sudoku = [
             [9, 0, 0, 0, 8, 0, 3, 0, 0],
             [2, 0, 0, 2, 5, 0, 7, 0, 0],
             [0, 2, 0, 3, 0, 0, 0, 0, 4],
             [2, 9, 4, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 7, 3, 0, 5, 6, 0],
             [7, 0, 5, 0, 6, 0, 4, 0, 0],
             [0, 0, 7, 8, 0, 3, 9, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 3],
             [3, 0, 0, 0, 0, 0, 0, 0, 2]
            ]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))