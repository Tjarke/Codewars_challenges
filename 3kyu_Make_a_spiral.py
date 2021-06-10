"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000

and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000

Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


"""
import numpy as np
 
def spiralize(size):
    spiral = np.zeros((size,size))
    spiral[0,:] = 1
    n = size - 1
    
    lb_y = 1
    ub_y = size
    y = n
    lb_x = 0
    ub_x = size-1
    x = n
    
    flip = 1   
    for i in range(int(n)):
        if i%2 == 0:
            spiral[lb_y:ub_y,x] = 1
            y = ub_y-1 if flip==1 else lb_y
            lb_y += 1
            ub_y -= 1
        else:
            spiral[y,lb_x:ub_x] = 1
            x = lb_x if flip==1 else ub_x-1
            lb_x += 1
            ub_x -= 1
            flip *= -1

    return spiral.astype('int').tolist()


