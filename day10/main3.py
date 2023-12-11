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
    input_str = open("day10/example2.txt", "r").readlines()
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
        
    #print(traversalMap)
    flags = {}
    val = 0
    for sx in range(len(input_str)):
        for sy in range(len(input_str[0])):
            if traversalMap[sx][sy] == None and input_str[sx][sy] != ".":
                findLoop(sx, sy, input_str, traversalMap, flags, val)
                val += 1
            
    print(flags)
    
     # go through outer layer and find all the gaps
    gaps = []
    for row in range(len(traversalMap)):
        if traversalMap[row][0] not in flags or flags[traversalMap[row][0]] == False:
            gaps += [(row, 0)]
            traversalMap[row][0] = 'X'
        if traversalMap[row][-1] not in flags or flags[traversalMap[row][-1]] == False:
            gaps += [(row, len(traversalMap[0])-1)]
            traversalMap[row][-1] = 'X'
    for col in range(len(traversalMap[0])):
        if traversalMap[0][col] not in flags or flags[traversalMap[0][col]] == False:
            gaps += [(0, col)]
            traversalMap[0][col] = 'X'
        if traversalMap[-1][col] not in flags or flags[traversalMap[-1][col]] == False:
            gaps += [(len(traversalMap)-1, col)]
            traversalMap[-1][col] = 'X'
            
    def fillGap(x, y, maze, gaps):
        if x-1 >= 0           and (maze[x-1][y] == None or maze[x-1][y] == 'X' or flags[maze[x-1][y]] == False):
            if maze[x-1][y] != 'X':
                maze[x-1][y] = 'X'
                gaps += [(x-1, y)]
        if x+1 < len(maze)    and (maze[x+1][y] == None or maze[x+1][y] == 'X' or flags[maze[x+1][y]] == False):
            if maze[x+1][y] != 'X':
                maze[x+1][y] = 'X'
                gaps += [(x+1, y)]
        if y-1 >= 0           and (maze[x][y-1] == None or maze[x][y-1] == 'X' or flags[maze[x][y-1]] == False):
            if maze[x][y-1] != 'X':
                maze[x][y-1] = 'X'
                gaps += [(x, y-1)]
        if y+1 < len(maze[0]) and (maze[x][y+1] == None or maze[x][y+1] == 'X' or flags[maze[x][y+1]] == False):
            if maze[x][y+1] != 'X':
                maze[x][y+1] = 'X'
                gaps += [(x, y+1)]
    
    while len(gaps) > 0:
        cur = gaps.pop(0)
        fillGap(cur[0], cur[1], traversalMap, gaps)
    
    count = 0
    for row in traversalMap: 
        for c in row:
            print(c if c != None else "?", end="")
            if c == None:
                count += 1
        print()
    print(count)

def findLoop(sx, sy, map, traversalMap, flags, val):
    stack = []
    flags[val] = True
    print("finding loop at", sx, sy)
    for row in traversalMap: 
        for c in row:
            print(c if c != None else "?", end="")
        print()
    input()
    traversalMap[sx][sy] = val
    if sx-1 >= 0 and connectivity[map[sx-1][sy]][1]:
        traversalMap[sx-1][sy] = val
        stack += [(sx-1, sy, sx, sy)]
    # check down
    if sx+1 < len(map) and connectivity[map[sx+1][sy]][0]:
        traversalMap[sx+1][sy] = val
        stack += [(sx+1, sy, sx, sy)]
    # check left
    if sy-1 >= 0 and connectivity[map[sx][sy-1]][3]:
        traversalMap[sx][sy-1] = val
        stack += [(sx, sy-1, sx, sy)]
    # check right
    if sy+1 < len(map[0]) and connectivity[map[sx][sy+1]][2]:
        traversalMap[sx][sy+1] = val
        stack += [(sx, sy+1, sx, sy)]
    
    while len(stack) > 0:
        cur = stack.pop(0)
        traverse(cur[0], cur[1], cur[2], cur[3], traversalMap[cur[0]][cur[1]], map, traversalMap, stack, flags)

def traverse(toX, toY, fromX, fromY, val, map, traversalMap, stack, flags):
    if flags[val] == False:
        return
    if map[toX][toY] == ".":
        return
    else:
        traversalMap[toX][toY] = val
    symbol = map[toX][toY]
    dirs = connectivity[symbol]
    
    print("traversing", toX, toY, "from", fromX, fromY, "with val", val)
    print("stack:", stack)
    for row in traversalMap:
        for c in row:
            print(c if c != None else "?", end="")
        print()
    #input()
    
    if dirs[0] and toX-1 >= 0 and (toX-1 != fromX or toY != fromY):
        if traversalMap[toX-1][toY] == None and connectivity[map[toX-1][toY]][1]:
            print("appending", toX-1, toY)
            traversalMap[toX-1][toY] = val
            stack += [(toX-1, toY, toX, toY)]
        else:
            if traversalMap[toX-1][toY] != val:
                print("setting flag to false", val, "at", toX-1, toY)
                flags[val] = False
                return
            
    if dirs[1] and toX+1 < len(map) and (toX+1 != fromX or toY != fromY):
        if traversalMap[toX+1][toY] == None and connectivity[map[toX+1][toY]][0]:
            print("appending", toX+1, toY)
            traversalMap[toX+1][toY] = val
            stack += [(toX+1, toY, toX, toY)]
        else:
            if traversalMap[toX+1][toY] != val:
                print("setting flag to false", val, "at", toX+1, toY)
                flags[val] = False
                return
            
    if dirs[2] and toY-1 >= 0 and (toX != fromX or toY-1 != fromY):
        if traversalMap[toX][toY-1] == None and connectivity[map[toX][toY-1]][3]:
            print("appending", toX, toY-1)
            traversalMap[toX][toY-1] = val
            stack += [(toX, toY-1, toX, toY)]
        else:
            if traversalMap[toX][toY-1] != val:
                print("setting flag to false", val, "at", toX, toY-1)   
                flags[val] = False
                return
            
    if dirs[3] and toY+1 < len(map[0]) and (toX != fromX or toY+1 != fromY):
        if traversalMap[toX][toY+1] == None and connectivity[map[toX][toY+1]][2]:
            print("appending", toX, toY+1)
            traversalMap[toX][toY+1] = val
            stack += [(toX, toY+1, toX, toY)]
        else:
            if traversalMap[toX][toY+1] != val:
                print("setting flag to false", val, "at", toX, toY+1)
                flags[val] = False
                return


if __name__ == "__main__":
    main()