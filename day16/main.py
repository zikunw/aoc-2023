energy_type = [
    # "-", # horizontal
    # "|", # vertical
    "l-",
    "r-",
    "u|",
    "d|",
]

# energy_grid[x][y] = ["-", "|", "/"]

def main():
    with open("day16/input.txt", "rb") as f:
        data = f.readlines()
        data = [list(line.strip()) for line in data]
        data = [list(map(chr, line)) for line in data]
        
    for line in data:
        for c in line:
            print(c, end='')
        print()
        
    width = len(data[0])
    height = len(data) 
    print(width, height)
    
    energy_grid = [[[] for y in range(width)] for x in range(height)]
    #energy_grid[0][0] = ["-"]
    stack = [((0, 0), (0, -1), "l-")]
    while stack != []:
        cur_coord, prev_coord, energy = stack.pop()
        #print(cur_coord, prev_coord, energy)
        
        if energy not in energy_type:
            raise Exception("Invalid energy")
        
        if not checkXY(cur_coord[0], cur_coord[1], width, height): 
            print("Out of bounds")
            continue
        
        cur_energies = energy_grid[cur_coord[0]][cur_coord[1]] # energies: ["-", "|", "/", "\\"]
        cur_mirror = data[cur_coord[0]][cur_coord[1]]          # mirrors: [".", "/", "\\", "|", "-"]
        
        if energy in cur_energies: 
            print("Already visited")
            continue
        energy_grid[cur_coord[0]][cur_coord[1]].append(energy)
        
        orig_energy = energy
        energy = energy[-1]
        
        if cur_mirror == "." or energy == cur_mirror:
            x_diff = cur_coord[0] - prev_coord[0]
            y_diff = cur_coord[1] - prev_coord[1]
            stack.append(((cur_coord[0]+x_diff, cur_coord[1]+y_diff), cur_coord, orig_energy))
        elif cur_mirror == "/":
            if energy == "-":
                if prev_coord[1] < cur_coord[1]:
                    stack.append(((cur_coord[0]-1, cur_coord[1]), cur_coord, "d|"))
                else:
                    stack.append(((cur_coord[0]+1, cur_coord[1]), cur_coord, "u|"))
            elif energy == "|":
                if prev_coord[0] < cur_coord[0]:
                    stack.append(((cur_coord[0], cur_coord[1]-1), cur_coord, "r-"))
                else:
                    stack.append(((cur_coord[0], cur_coord[1]+1), cur_coord, "l-"))
            else: 
                raise Exception("Invalid energy")
        elif cur_mirror == "\\":
            if energy == "-":
                if prev_coord[1] < cur_coord[1]:
                    stack.append(((cur_coord[0]+1, cur_coord[1]), cur_coord, "u|"))
                else:
                    stack.append(((cur_coord[0]-1, cur_coord[1]), cur_coord, "d|"))
            elif energy == "|":
                if prev_coord[0] < cur_coord[0]:
                    stack.append(((cur_coord[0], cur_coord[1]+1), cur_coord, "l-"))
                else:
                    stack.append(((cur_coord[0], cur_coord[1]-1), cur_coord, "r-"))
            else:
                raise Exception("Invalid energy")
        elif cur_mirror == "|":
            if energy == "-":
                stack.append(((cur_coord[0]-1, cur_coord[1]), cur_coord, "d|"))
                stack.append(((cur_coord[0]+1, cur_coord[1]), cur_coord, "u|"))
            elif energy == "|":
                stack.append(((cur_coord[0]-prev_coord[0], cur_coord[1]-prev_coord[1]), cur_coord, orig_energy))
            else:
                raise Exception("Invalid energy")
        elif cur_mirror == "-":
            if energy == "|":
                stack.append(((cur_coord[0], cur_coord[1]+1), cur_coord, "l-"))
                stack.append(((cur_coord[0], cur_coord[1]-1), cur_coord, "r-"))
            elif energy == "-":
                stack.append(((cur_coord[0]-prev_coord[0], cur_coord[1]-prev_coord[1]), cur_coord, orig_energy))
            else:
                raise Exception("Invalid energy")
        else:
            raise Exception("Invalid mirror")
        
        # for line in energy_grid:
        #     for c in line:
        #         if c == []:
        #             print(".", end='')
        #         else:
        #             print("#", end='')
        #     print()
        print(len(stack))
        
        #input()
        
    count = 0
    for line in energy_grid:
        for c in line:
            if c != []:
                count += 1
    print(count)
        
      

def checkXY(x, y, width, height):
    return 0 <= x < width and 0 <= y < height
    
if __name__ == '__main__':
    main()
    
# #elif energy == "\\":
#                 stack.append(((cur_coord[0]+1, cur_coord[1]-1), cur_coord, "/"))
#                 stack.append(((cur_coord[0]-1, cur_coord[1]+1), cur_coord, "/"))