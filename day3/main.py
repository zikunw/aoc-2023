with open("input.txt", "r") as f:
    lines = f.readlines()
    # construct the grid
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
        
s = 0

def check_num_relevant(num_row, num_col_start, num_col_end):
    print("check", grid[num_row][num_col_start:num_col_end+1])
    # check if the surrounding cells include symbols that is not . or a digit
    # check row above
    if num_row > 0:
        for num_col in range(num_col_start, num_col_end+1):
            if grid[num_row-1][num_col] not in ".0123456789":
                return True
        if num_col_start > 0:
            if grid[num_row-1][num_col_start-1] not in ".0123456789":
                return True
        if num_col_end < len(grid[0])-1:
            if grid[num_row-1][num_col_end+1] not in ".0123456789":
                return True
    # check row below
    if num_row < len(grid)-1:
        for num_col in range(num_col_start, num_col_end+1):
            if grid[num_row+1][num_col] not in ".0123456789":
                return True
        if num_col > 0:
            if grid[num_row+1][num_col_start-1] not in ".0123456789":
                return True
        if num_col_end < len(grid[0])-1:
            if grid[num_row+1][num_col_end+1] not in ".0123456789":
                return True
    # check left
    if num_col_start > 0:
        if grid[num_row][num_col_start-1] not in ".0123456789":
            return True
    # check right
    if num_col_end < len(grid[0])-1:
        if grid[num_row][num_col_end+1] not in ".0123456789":
            return True
    return False

def get_num(num_row, num_col):
    if grid[num_row][num_col] not in "0123456789":
        return -1
    num_col_end = num_col
    while num_col_end < len(grid[0])-1 and grid[num_row][num_col_end+1] in "0123456789":
        num_col_end += 1
        
    return num_col_end

row = 0
col = 0
while row < len(grid):
    while col < len(grid[0]):
        num_col_end = get_num(row, col)
        if num_col_end == -1:
            col += 1
            continue
        
        print(row, col, num_col_end)
        if check_num_relevant(row, col, num_col_end):
            print("relevant\n")
            s += int("".join(grid[row][col:num_col_end+1]))
        col = num_col_end + 1
    row += 1
    col = 0
        

print(s)