"""
Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.
"""


from copy import deepcopy


def sudoku(puzzle):
    grid = puzzle
    solve(grid)
    return ans
    
def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if check(y,x,n,grid):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return
    global ans
    ans = deepcopy(grid)

    
def check(y,x,n,grid):
    #check rows:
    for i in range(0,9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False 
    #check squares              
    x0 = (x//3)*3   #get starting location of each square
    y0 = (y//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    
    return True




### nice explanation video https://www.youtube.com/watch?v=G_UYXzGuqvM


