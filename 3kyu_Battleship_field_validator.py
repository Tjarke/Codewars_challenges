"""
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly to the following rules:

    There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
    Each ship must be a straight line, except for submarines, which are just single cell.
    The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game, visit this link.
"""

import numpy as np


def validate_battlefield(field):
    bfield = np.array(field)
    
    shiplen = 0
    allowed_ships = [4,3,3,2,2,2,1,1,1,1]
    
    y_max = len(bfield[0,:])-1
    x_max = len(bfield[:,0])-1
    
    horizontal = 0
    
    for y in range(y_max+1):
        for x in range(x_max+1):
            shiplen = 0
            if bfield[x,y] == 1:
                shiplen += 1
                
                if (x == x_max and y == y_max):
                    # (x == x_max and bfield[x,y+1] == 0)) or 
                    # (bfield[x+1,y] == 0 and y == y_max) or
                    # (bfield[x+1,y] == 0 and bfield[x,y+1] == 0)):
                    
                    ship = [x,y,shiplen,horizontal]                   
                    if not test_neighbours(ship,bfield):
                        return False   
                    Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                    if not Condition:
                        return Condition
                
                elif x == x_max:
                    if bfield[x,y+1] == 0:
                        ship = [x,y,shiplen,horizontal]                   
                        if not test_neighbours(ship,bfield):
                            return False   
                        Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                        if not Condition:
                            return Condition
                    if bfield[x,y+1] == 1:
                        horizontal = 0
                        ship = find_ship(x,y,shiplen,bfield,horizontal)  
                        if not test_neighbours(ship,bfield):
                             return False   
                        Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                        if not Condition:
                             return Condition
                         
                elif y == y_max:
                    if bfield[x+1,y] == 0:
                        ship = [x,y,shiplen,horizontal]                   
                        if not test_neighbours(ship,bfield):
                            return False   
                        Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                        if not Condition:
                            return Condition
                    elif bfield[x+1,y] == 1:
                        horizontal = 1
                        ship = find_ship(x,y,shiplen,bfield,horizontal)
                        if not test_neighbours(ship,bfield):
                             return False   
                        Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                        if not Condition:
                             return Condition
                    
                elif bfield[x+1,y] == 0 and bfield[x,y+1] == 1:
                     horizontal = 0
                     ship = find_ship(x,y,shiplen,bfield,horizontal)  
                     if not test_neighbours(ship,bfield):
                         return False   
                     Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                     if not Condition:
                         return Condition
                     
                elif (bfield[x+1,y] == 1 and bfield[x,y+1] == 0):
                     horizontal = 1
                     ship = find_ship(x,y,shiplen,bfield,horizontal)
                     if not test_neighbours(ship,bfield):
                         return False   
                     Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                     if not Condition:
                         return Condition
                     
                elif (bfield[x+1,y] == 0 and bfield[x,y+1] == 0):
                    ship = [x,y,shiplen,horizontal]                   
                    if not test_neighbours(ship,bfield):
                        return False   
                    Condition, shiplen, bfield, allowed_ships = validate_and_replace(ship, bfield, allowed_ships)
                    if not Condition:
                        return Condition
                     
    return len(allowed_ships) == 0


def test_neighbours(ship,bfield):
    # ship = [x,y,shiplen,horizontal]
    x = ship[0]
    y = ship[1]
    shiplen = ship[2]
    horizontal = ship[3]
    
    y_max = len(bfield[0,:])-1
    x_max = len(bfield[:,0])-1
        
    if horizontal:
        lb_x = min(i for i in [x-1,x] if i>=0)
        ub_x = max(i for i in [x+shiplen+1,x+shiplen,x] if i<=x_max)
        if y == 0:
            cols = y+1
        elif y == y_max:
            cols = y-1
        else:
            cols = [y-1,y+1]
        if bfield[lb_x:ub_x,cols].any() != 0:
            return False
    else:
        lb = min(i for i in [y-1,y] if i>=0)
        ub = max(i for i in [y+shiplen+1,y+shiplen,y] if i<=y_max)
        if x == 0:
            rows = x+1
        elif x == x_max:
            rows = x-1
        else:
            rows = [x-1,x+1]               
        if bfield[rows,lb:ub].any() != 0:
            return False
    return True

def validate_and_replace(ship,bfield,allowed_ships):
    x = ship[0]
    y = ship[1]
    shiplen = ship[2]
    horizontal = ship[3]
    
    try:
        allowed_ships.pop(allowed_ships.index(shiplen))
        if horizontal:
            bfield[x:x+shiplen,y] = 0 
        else:
            bfield[x,y:y+shiplen] = 0
        shiplen = 0     
        return True, shiplen, bfield, allowed_ships                 
    except:
        return False, shiplen, bfield, allowed_ships   


def find_ship(x,y,shiplen,bfield,horizontal):
    
    y_max = len(bfield[0,:])-1
    x_max = len(bfield[:,0])-1

    
    if horizontal:
        x_w = x+1
        while x_w <= x_max:
            if bfield[x_w,y] == 1:
                shiplen += 1
            else:
                break
            x_w += 1
        ship = [x,y,shiplen,horizontal]
    else:
        y_w = y+1
        while y_w <= y_max:
            if bfield[x,y_w] == 1:
                shiplen += 1
            else:
                break
            y_w += 1
        ship = [x,y,shiplen,horizontal]
    return ship
