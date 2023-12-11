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
}

def main():
    input_str = open("day10/input.txt", "r").readlines()
    maze = [list(line.strip()) for line in input_str]
    
    m = len(maze)
    n = len(maze[0])

    # adding gaps with 'X'
    temp = [['X' for i in range(len(maze[0])*2-1)] for j in range(len(maze)*2-1)]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            temp[i*2][j*2] = maze[i][j] if maze[i][j] != '.' else 'X'
    
    maze = temp
    
    # connect gaps
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] not in connectivity:
                continue
            if row-1 >= 0 and connectivity[maze[row][col]][0]:
                if row-2 >= 0 and maze[row-2][col] in connectivity and connectivity[maze[row-2][col]][1]:
                    maze[row-1][col] = '|'
            if row+1 < len(maze) and connectivity[maze[row][col]][1]:
                if row+2 < len(maze) and maze[row+2][col] in connectivity and connectivity[maze[row+2][col]][0]:
                    maze[row+1][col] = '|'
            if col-1 >= 0 and connectivity[maze[row][col]][2]:
                if col-2 >= 0 and maze[row][col-2] in connectivity and connectivity[maze[row][col-2]][3]:
                    maze[row][col-1] = '-'
            if col+1 < len(maze[0]) and connectivity[maze[row][col]][3]:
                if col+2 < len(maze[0]) and maze[row][col+2] in connectivity and  connectivity[maze[row][col+2]][2]:
                    maze[row][col+1] = '-'
    
    traverseMap = [[0 for i in range(len(maze[0]))] for j in range(len(maze))]
    val = 1
    flags = {}
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if traverseMap[row][col] == 0 and maze[row][col] != 'X':
                result = findLoop(row, col, maze, traverseMap, val)
                flags[val] = result
                val += 1
    print(flags)
    
    # remove all the non-looping paths
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if traverseMap[row][col] not in flags or flags[traverseMap[row][col]] == False:
                maze[row][col] = 'X'

        
    # go through outer layer and find all the gaps
    gaps = []
    for row in range(len(maze)):
        if maze[row][0] == 'X':
            gaps += [(row, 0)]
            maze[row][0] = 'O'
        if maze[row][-1] == 'X':
            gaps += [(row, len(maze[0])-1)]
            maze[row][-1] = 'O'
    for col in range(len(maze[0])):
        if maze[0][col] == 'X':
            gaps += [(0, col)]
            maze[0][col] = 'O'
        if maze[-1][col] == 'X':
            gaps += [(len(maze)-1, col)]
            maze[-1][col] = 'O'
            
    while len(gaps) > 0:
        cur = gaps.pop(0)
        fillGap(cur[0], cur[1], maze, gaps)
                
    for row in maze:
        for c in row:
            print(c, end='')
        print()
        
    # turn maze back
    original = [['.' for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            original[i][j] = maze[i*2][j*2]
    
    for row in original:
        for c in row:
            print(c, end='')
        print()
    maze = original
    # count '.'s
    count = 0
    for row in maze:
        for col in row:
            if col == 'X':
                count += 1
    print(count)
    # generate an image using PIL
    from PIL import Image
    img = Image.new('RGB', (n, m), color = 'white')
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if maze[j][i] == 'X':
                pixels[i, j] = (0, 0, 0)
            elif maze[j][i] == 'O':
                pixels[i, j] = (255, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)
    img.save('day10/output.png')
        
def fillGap(x, y, maze, gaps):
    if x-1 >= 0 and maze[x-1][y] == 'X':
        maze[x-1][y] = 'O'
        gaps += [(x-1, y)]
    if x+1 < len(maze) and maze[x+1][y] == 'X':
        maze[x+1][y] = 'O'
        gaps += [(x+1, y)]
    if y-1 >= 0 and maze[x][y-1] == 'X':
        maze[x][y-1] = 'O'
        gaps += [(x, y-1)]
    if y+1 < len(maze[0]) and maze[x][y+1] == 'X':
        maze[x][y+1] = 'O'
        gaps += [(x, y+1)]

def findLoop(x, y, maze, traverseMap, val):
        originx = x
        originy = y
        fromX = -1
        fromY = -1
        while True:
            if x == originx and y == originy and fromX != -1 and fromY != -1:
                return True
            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
                return False
            if traverseMap[x][y] == val:
                return True
            if traverseMap[x][y] != 0:
                return False
            if maze[x][y] == "X":
                return False
            
            traverseMap[x][y] = val
            if maze[x][y] == "|":
                if fromX == x-1:
                    fromX, fromY = x, y
                    x += 1
                else:
                    fromX, fromY = x, y
                    x -= 1
                continue    
            if maze[x][y] == "-":
                if fromY == y-1:
                    fromX, fromY = x, y
                    y += 1
                else:
                    fromX, fromY = x, y
                    y -= 1
                continue
            if maze[x][y] == "L":
                if fromX == x-1:
                    fromX, fromY = x, y
                    y += 1
                else:
                    fromX, fromY = x, y
                    x -= 1
                continue
            if maze[x][y] == "J":
                if fromX == x-1:
                    fromX, fromY = x, y
                    y -= 1
                else:
                    fromX, fromY = x, y
                    x -=1
                continue
            if maze[x][y] == "7":
                if fromX == x+1:
                    fromX, fromY = x, y
                    y-=1
                else:
                    fromX, fromY = x, y
                    x+=1
                continue
            if maze[x][y] == "F":
                if fromX == x+1:
                    fromX, fromY = x, y
                    y += 1
                else:
                    fromX, fromY = x, y
                    x += 1
                continue
                
        return False
    
if __name__ == "__main__":
    main()