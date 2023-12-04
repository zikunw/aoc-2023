def main():
    #part1()
    part2()
    
def part1():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        # construct the grid
        grid = []
        for line in lines:
            grid.append((line.strip()))
            
    s = 0
    
    for line in grid:
        line = line[9:]
        line = line.split("|")
        winning_num = [e for e in line[0].strip().split(" ") if e != ""]
        my_num = [e for e in line[1].strip().split(" ") if e != ""]
        cur_score = 0
        for num in my_num:
            if num in winning_num:
                if cur_score == 0:
                    cur_score = 1
                else:
                    cur_score *= 2
        s += cur_score
    print(s)

def part2():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        # construct the grid
        grid = []
        for line in lines:
            grid.append((line.strip()))
            
    s = 0
    scores = [1] * len(grid)
    
    for line, index in zip(grid, range(len(grid))):
        line = line[9:]
        line = line.split("|")
        winning_num = [e for e in line[0].strip().split(" ") if e != ""]
        my_num = [e for e in line[1].strip().split(" ") if e != ""]
        cur_score = 0
        for num in my_num:
            if num in winning_num:
                cur_score += 1
        next_index = (index + 1)
        while next_index < len(grid) and next_index < (index + cur_score + 1):
            scores[next_index] += scores[index]
            next_index += 1
        
        s += cur_score * scores[index]
    print(sum(scores))

main()