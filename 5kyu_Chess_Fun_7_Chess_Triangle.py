"""
Task

Consider a bishop, a knight and a rook on an n × m chessboard. They are said to form a triangle if each piece attacks exactly one other piece and is attacked by exactly one piece.

Calculate the number of ways to choose positions of the pieces to form a triangle.

Note that the bishop attacks pieces sharing the common diagonal with it; the rook attacks in horizontal and vertical directions; and, finally, the knight attacks squares which are two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from its position.

Example

For n = 2 and m = 3, the output should be 8.

Input/Output

    [input] integer n

    Constraints: 1 ≤ n ≤ 40.

    [input] integer m

    Constraints: 1 ≤ m ≤ 40, 3 ≤ n x m.

    [output] an integer


"""


def chess_triangle(n, m):
    total_pos = 0
    for x in range(n):
        for y in range(m):
            pos_hors = (x,y)
            scnd_piece = [(x+2,y+1), (x+1,y+2),
                          (x-1,y+2), (x-2,y+1),
                          (x-2,y-1), (x-1,y-2),
                          (x+1,y-2), (x+2,y-1)]
            allowed = [pos for pos in scnd_piece if pos[0] < n and pos[0] >= 0 
                       and pos[1] < m and pos[1] >= 0]
            for pos_rook in allowed:
                for b_x in range(n):
                    b_y = pos_rook[1]
                    pos_bish = (b_x,b_y)
                    if abs(pos_bish[0]-pos_hors[0]) == abs(pos_bish[1]-pos_hors[1]):
                        total_pos += 1
                for b_y in range(m):
                    b_x = pos_rook[0]
                    pos_bish = (b_x,b_y)
                    if abs(pos_bish[0]-pos_hors[0]) == abs(pos_bish[1]-pos_hors[1]):
                        total_pos += 1
                        
            for pos_bish in allowed:
                b_x = pos_bish[0]
                b_y = pos_bish[1]
                thrd_piece = [(b_x+1,b_y+1), (b_x+2,b_y+2),
                              (b_x-1,b_y+1), (b_x-2,b_y+2),
                              (b_x-1,b_y-1), (b_x-2,b_y-2),
                              (b_x+1,b_y-1), (b_x+2,b_y-2)]
                allowed =  [pos for pos in thrd_piece if pos[0] < n and pos[0] >= 0 
                       and pos[1] < m and pos[1] >= 0]  
                for pos_rook in allowed:
                    if pos_rook[0] == pos_hors[0] or pos_rook[1] == pos_hors[1]:
                        total_pos += 1
    return total_pos


