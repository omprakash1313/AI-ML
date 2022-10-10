# to solve sudoko
# step 1 - construct a 9*9 matrix
dimension = 9


def problem(a):
    for i in range(dimension):
        for j in (dimension):
            print(a[i][j] + " ")
            print()


# taking parameters that is grid, row, col, numberber that is inserted
def sudukosolve(sudukoGrid, row, column, number):
    for i in range(9):
        if(sudukoGrid[row][i] == number):
            return False
    for i in range(9):
        if(sudukoGrid[i][column] == number):
            return False

    begningRow = row-row % 3  # restrction to current the block  3*3
    begningCol = column-column % 3  # restrction to current the block  3*3

    for i in range(3):
        for j in range(3):
            # checking not to have a numberber same in the block and row or column
            if sudukoGrid[i+begningRow][j+begningCol] == number:
                return False
        return True


def logicSolve(sudukoGrid, row, column):
    if (row==dimension-1 and column==dimension):
        return True

    if column == dimension:
        row = row+1
        col = 0

    if (sudukoGrid[row][column] > 0):
        return logicSolve(sudukoGrid, row, column+1)

    for number in range(1, dimension+1, 1):
        if sudukosolve(sudukoGrid, row, column, number):
            sudukoGrid[row][column] = number

            if logicSolve(sudukoGrid, row, column):
                sudukoGrid[row][column] = number
                if logicSolve(sudukoGrid, row, column+1):
                    return True
            sudukoGrid[row][column] = 0

            if logicSolve(sudukoGrid, row, col + 1):
                return True
            sudukoGrid[row][column] = 0
    return False

sudukoGrid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
              [0, 1, 0, 0, 0, 4, 0, 0, 0],
              [4, 0, 7, 0, 0, 0, 2, 0, 8],
              [0, 0, 5, 2, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 9, 8, 1, 0, 0],
              [0, 4, 0, 0, 0, 3, 0, 0, 0],
              [0, 0, 0, 3, 6, 0, 0, 7, 2],
              [0, 7, 0, 0, 0, 0, 0, 0, 3],
              [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if(logicSolve(sudukoGrid,0,0)):
    problem(sudukoGrid)
else:
    print("Answer")
