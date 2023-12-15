import time

def main():
    input_str = open("day14/input.txt", "r").readlines()
    g = [list(line.strip()) for line in input_str]
        
    for row in g:
        for col in row:
            print(col, end="")
        print()
    print()
    
    #roll(g, "west")
    for i in range(1_000_000_000):
        start = time.time()
        roll(g, "north")
        roll(g, "west")
        roll(g, "south")
        roll(g, "east")
        
        #time.sleep(0.1)
        print(i, count_weight(g))
        with open("day14/output.txt", "a") as f:
            f.write(str(count_weight(g)) + "\n")
            # Find the pattern in the output.txt file
    
    for row in g:
        for col in row:
            print(col, end="")
        print()
        
    print(count_weight(g))
        
    
def roll(g, direction):
    match direction:
        case "north":
            for i in range(len(g[0])-1, -1, -1):
                o_counter = 0
                h_prev = len(g) - 1
                for j in range(len(g)-1, -1, -1):
                    if g[j][i] == "O":
                        o_counter += 1
                    elif g[j][i] == "#":
                        for k in range(h_prev, j+o_counter, -1):
                            g[k][i] = "."
                        for k in range(j+o_counter, j, -1):
                            g[k][i] = "O"
                        h_prev = j - 1
                        o_counter = 0
                if o_counter > 0:
                    for k in range(h_prev, -1, -1):
                        g[k][i] = "."
                    for k in range(o_counter):
                        g[k][i] = "O"   
        case "south":
            for i in range(len(g[0])):
                o_counter = 0
                h_prev = 0
                for j in range(len(g)):
                    if g[j][i] == "O":
                        o_counter += 1
                    elif g[j][i] == "#":
                        for k in range(h_prev, j-o_counter):
                            g[k][i] = "."
                        for k in range(j-o_counter, j):
                            g[k][i] = "O"
                        h_prev = j + 1
                        o_counter = 0
                if o_counter > 0:
                    for k in range(h_prev, len(g)):
                        g[k][i] = "."
                    for k in range(len(g)-o_counter, len(g)):
                        g[k][i] = "O"
        case "east":
            for i in range(len(g)):
                o_counter = 0
                h_prev = 0
                for j in range(len(g[0])):
                    if g[i][j] == "O":
                        o_counter += 1
                    elif g[i][j] == "#":
                        for k in range(h_prev, j-o_counter):
                            g[i][k] = "."
                        for k in range(j-o_counter, j):
                            g[i][k] = "O"
                        h_prev = j + 1
                        o_counter = 0
                if o_counter > 0:
                    for k in range(h_prev, len(g[0])):
                        g[i][k] = "."
                    for k in range(len(g[0])-o_counter, len(g[0])):
                        g[i][k] = "O"
        case "west":
            for i in range(len(g)):
                o_counter = 0
                h_prev = len(g[0]) - 1
                for j in range(len(g[0])-1, -1, -1):
                    if g[i][j] == "O":
                        o_counter += 1
                    elif g[i][j] == "#":
                        for k in range(h_prev, j+o_counter, -1):
                            g[i][k] = "."
                        for k in range(j+o_counter, j, -1):
                            g[i][k] = "O"
                        h_prev = j - 1
                        o_counter = 0
                if o_counter > 0:
                    for k in range(h_prev, -1, -1):
                        g[i][k] = "."
                    for k in range(o_counter):
                        g[i][k] = "O"
                    
def count_weight(g):
    weight = 0
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == "O":
                weight += len(g) - row
    return weight
    
    
if __name__ == "__main__":
    main()