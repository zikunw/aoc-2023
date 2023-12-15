def main():
    input_str = open("day14/input.txt", "r").readlines()
    g = [list(line.strip()) for line in input_str]
        
    for row in g:
        for col in row:
            print(col, end="")
        print()
    print()
        
    roll_north(g)
    
    for row in g:
        for col in row:
            print(col, end="")
        print()
        
    print(count_weight(g))
        
    
def roll_north(g):
    rolled_count = 10
    while rolled_count > 0:
        rolled_count = 0
        for row in range(1, len(g)):
            for col in range(len(g[0])):
                if g[row][col] == "O" and g[row-1][col] == ".":
                    g[row][col] = "."
                    g[row-1][col] = "O"
                    rolled_count += 1
                    
def count_weight(g):
    weight = 0
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == "O":
                weight += len(g) - row
    return weight
    
    
if __name__ == "__main__":
    main()