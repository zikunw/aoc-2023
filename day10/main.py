from functools import * 
import time

# (up, down, left, right)
connectivity = {
    "|": (True, True, False, False),
    "-": (False, False, True, True),
    "L": (True, False, False, True),
    "J": (True, False, True, False),
    "7": (False, True, True, False),
    "F": (False, True, False, True),
    ".": (False, False, False, False),
    "S": (False, False, False, False),
}

def main():
    input_str = open("day10/input.txt", "r").readlines()
    input_str = [list(line.strip()) for line in input_str]
    
    print(input_str)
    
    traversalMap = [[None for i in range(len(input_str[0]))] for j in range(len(input_str))]
    
    sx = 0
    sy = 0
    for i in range(len(input_str)):
        for j in range(len(input_str[0])):
            if input_str[i][j] == "S":
                sx = i
                sy = j
                break
    
    print(sx, sy)
    
    # check surrounding of s for connectivity
    # check up
    stack = []
    print(connectivity[input_str[sx-1][sy]])
    if sx-1 >= 0 and connectivity[input_str[sx-1][sy]][1]:
        traversalMap[sx-1][sy] = 1
        stack += [(sx-1, sy, sx, sy)]
    # check down
    if sx+1 < len(input_str) and connectivity[input_str[sx+1][sy]][0]:
        traversalMap[sx+1][sy] = 1
        stack += [(sx+1, sy, sx, sy)]
    # check left
    if sy-1 >= 0 and connectivity[input_str[sx][sy-1]][3]:
        traversalMap[sx][sy-1] = 1
        stack += [(sx, sy-1, sx, sy)]
    # check right
    if sy+1 < len(input_str[0]) and connectivity[input_str[sx][sy+1]][2]:
        traversalMap[sx][sy+1] = 1
        stack += [(sx, sy+1, sx, sy)]
        
    #print(traversalMap)
    
    while len(stack) > 0:
        cur = stack.pop(0)
        traverse(cur[0], cur[1], cur[2], cur[3], traversalMap[cur[0]][cur[1]], input_str, traversalMap, stack)
    
    for row in traversalMap: 
        print(row)
    
    # find the largest value
    traversalMap = map(lambda x: map(lambda y: 0 if y == None else y, x), traversalMap)
    maxVal = reduce(lambda x, y: max(x, y), [reduce(lambda x, y: max(x, y), row) for row in traversalMap])

    print(maxVal)
    
def traverse(toX, toY, fromX, fromY, val, map, traversalMap, stack):
    if (traversalMap[toX][toY] == None and traversalMap[toX][toY] < val) or map[toX][toY] == ".":
        return
    else:
        traversalMap[toX][toY] = val
    symbol = map[toX][toY]
    dirs = connectivity[symbol]
    if dirs[0] and toX-1 >= 0 and (toX-1 != fromX or toY != fromY):
        traversalMap[toX-1][toY] = val+1 if traversalMap[toX-1][toY] == None else min(val+1, traversalMap[toX-1][toY])
        stack += [(toX-1, toY, toX, toY)]
    if dirs[1] and toX+1 < len(map) and (toX+1 != fromX or toY != fromY):
        traversalMap[toX+1][toY] = val+1 if traversalMap[toX+1][toY] == None else min(val+1, traversalMap[toX+1][toY])
        stack += [(toX+1, toY, toX, toY)]
    if dirs[2] and toY-1 >= 0 and (toX != fromX or toY-1 != fromY):
        traversalMap[toX][toY-1] = val+1 if traversalMap[toX][toY-1] == None else min(val+1, traversalMap[toX][toY-1])
        stack += [(toX, toY-1, toX, toY)]
    if dirs[3] and toY+1 < len(map[0]) and (toX != fromX or toY+1 != fromY):
        traversalMap[toX][toY+1] = val+1 if traversalMap[toX][toY+1] == None else min(val+1, traversalMap[toX][toY+1])
        stack += [(toX, toY+1, toX, toY)]
    
if __name__ == "__main__":
    main()