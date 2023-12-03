with open("input.txt", "r") as f:
    lines = f.readlines()
    # construct the grid
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
        
s = 0

# create a new grid that contains gear number
# we will give each gear a unique number
gear_grid = [] # 2d array with [num, gear_id[]]
gear_id = 0
for row in range(len(grid)):
    gear_grid.append([[num, []] for num in grid[row]])
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "*":
            gear_id += 1
            # mark surrounding cell with uuid
            if row > 0 and col > 0:
                gear_grid[row-1][col-1][1].append(gear_id)
            if row > 0:
                gear_grid[row-1][col][1].append(gear_id)
            if row > 0 and col < len(grid[0])-1:
                gear_grid[row-1][col+1][1].append(gear_id)
            if col > 0:
                gear_grid[row][col-1][1].append(gear_id)
            if row < len(grid)-1 and col > 0:
                gear_grid[row+1][col-1][1].append(gear_id)
            if row < len(grid)-1:
                gear_grid[row+1][col][1].append(gear_id)
            if row < len(grid)-1 and col < len(grid[0])-1:
                gear_grid[row+1][col+1][1].append(gear_id)
            if col < len(grid[0])-1:
                gear_grid[row][col+1][1].append(gear_id)
                
def get_num(num_row, num_col):
    if gear_grid[num_row][num_col][0] not in "0123456789":
        return -1, None, None
    num_col_end = num_col
    while num_col_end < len(gear_grid[0])-1 and gear_grid[num_row][num_col_end+1][0] in "0123456789":
        num_col_end += 1
    num = int("".join([num[0] for num in gear_grid[num_row][num_col:num_col_end+1]]))
    gears = set()
    for num_col in range(num_col, num_col_end+1):
        gears.update(gear_grid[num_row][num_col][1])
    return num_col_end, num, gears

gear_list = {}

row = 0
col = 0
while row < len(grid):
    while col < len(grid[0]):
        num_col_end, num, gears = get_num(row, col)
        if num_col_end == -1:
            col += 1
            continue
        for gear in gears:
            if gear not in gear_list:
                gear_list[gear] = []
            gear_list[gear].append(num)
        
        col = num_col_end + 1
    row += 1
    col = 0

for gear in gear_list:
    if len(gear_list[gear]) == 2:
        s += gear_list[gear][0] * gear_list[gear][1]

print(s)