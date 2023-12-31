from enum import Enum
import math

class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    
    def left(self):
        return Direction((self.value - 1) % 4)
    def right(self):
        return Direction((self.value + 1) % 4)
    def offset(self):
        if self == Direction.UP:
            return (0, -1)
        elif self == Direction.DOWN:
            return (0, 1)
        elif self == Direction.LEFT:
            return (-1, 0)
        elif self == Direction.RIGHT:
            return (1, 0)
        else:
            raise ValueError("Invalid direction")
    def __str__(self) -> str:
        if self == Direction.UP:
            return "^"
        elif self == Direction.DOWN:
            return "v"
        elif self == Direction.LEFT:
            return "<"
        elif self == Direction.RIGHT:
            return ">"
        else:
            raise ValueError("Invalid direction")

def main():
    with open("day18/example.txt", "rb") as f:
        data = f.readlines()
        data = [line.strip().split() for line in data]
        data = [[str(line[0])[2], int(str(line[1])[2]), str(line[2])] for line in data]

    #print(data)
    
    
    #process data
    # new_data = []
    # for line in data:
    #     hexVal = str(line[2])[4:-2]
    #     distance = int(hexVal[:-1], 16)
    #     if hexVal[-1] == "0":
    #         direction = "R"
    #     elif hexVal[-1] == "1":
    #         direction = "D"
    #     elif hexVal[-1] == "2":
    #         direction = "L"
    #     elif hexVal[-1] == "3":
    #         direction = "U"
    #     else:
    #         raise ValueError("Invalid direction")
    #     new_data.append((direction, distance))
    # data = new_data
    
    # start in the middle
    #start_position = (width // 1, height // 2)
    start_position = [0, 0]
    max_x = float("-inf")
    max_y = float("-inf")
    min_x = float("inf")
    min_y = float("inf")
    up_lines = []
    down_lines = []
    points = [(0, 0)]
    totalDistance = 0
    for line in data:
        if line[0] == "U":
            up_lines.append((start_position[0], start_position[1]-line[1], start_position[1]))
            start_position[1] -= line[1]
        elif line[0] == "D":
            start_position[1] += line[1]
            down_lines.append((start_position[0], start_position[1], line[1]+1))
        elif line[0] == "L":
            start_position[0] -= line[1]
        elif line[0] == "R":
            start_position[0] += line[1]
        else:
            raise ValueError("Invalid direction")
        totalDistance += line[1]
        points.append((start_position[0], start_position[1]))
        max_x = max(max_x, start_position[0])
        max_y = max(max_y, start_position[1])
        min_x = min(min_x, start_position[0])
        min_y = min(min_y, start_position[1])
        
    # print(max_x, max_y, min_x, min_y)
    print(up_lines)
    print(down_lines)
    
    # draw lines
    temp = [[0] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for line in up_lines:
        for i in range(line[2]):
            temp[line[1]+i][line[0]] = 1
    for line in down_lines:
        for i in range(line[2]):
            temp[line[1]-i][line[0]] = 1
    printMap(temp)

    # innerArea = shoelaceArea(points)
    # print(innerArea)
    # interior = innerArea - math.floor(totalDistance/2) + 1
    # print(interior)
    # print(totalDistance + interior)
    
    # my method
    print(len(up_lines), len(down_lines))
    s = 0
    for i in range(min_y, max_y+1):
        print(i)
        up_lines = [line for line in up_lines if line[1] <= i <= line[2]]
        up_lines.sort(key=lambda x: x[0])
        print(up_lines)
        down_lines = [line for line in down_lines if line[1] >= i >= line[2]]
        down_lines.sort(key=lambda x: x[0])
        print(down_lines)
        input()
    
    
    return 0

    
    for line in data:
        direction = chr(ord(line[0]))
        steps = int(line[1])
        print(line)
        if direction == "U":
            #print("U")
            # expand map if needed
            if start_position[1] - steps < 0:
                new_map = [[0] * width for _ in range(height+steps+1)]
                for i in range(height):
                    new_map[i+steps] = map[i]
                map = new_map
                height += steps + 1
                start_position = (start_position[0], start_position[1]+steps)
            for i in range(int(line[1])):
                map[start_position[1] - i][start_position[0]] = 1
            start_position = (start_position[0], start_position[1] - int(line[1]))
            
        elif direction == "D":
            #print("D")
            # expand map if needed
            if start_position[1] + steps >= height:
                new_map = [[0] * width for _ in range(height+steps+1)]
                for i in range(height):
                    new_map[i] = map[i]
                map = new_map
                height += steps + 1
                start_position = (start_position[0], start_position[1])
            #printMap(map)
            #print(start_position)
            for i in range(int(line[1])):
                map[start_position[1] + i][start_position[0]] = 1
            start_position = (start_position[0], start_position[1] + int(line[1]))
            
        elif direction == "L":
            #print("L")
            if start_position[0] - steps < 0:
                diff = steps - start_position[0]
                #print(diff)
                new_map = [[0] * (width+diff+1) for _ in range(height)]
                for i in range(height):
                    for j in range(width):
                        new_map[i][j+diff] = map[i][j]
                map = new_map
                width += diff
                start_position = (start_position[0]+diff, start_position[1])
                #print(new_map, start_position)
            for i in range(int(line[1])):
                map[start_position[1]][start_position[0] - i] = 1
            start_position = (start_position[0] - steps, start_position[1])
            
        elif direction == 'R':
            #print("R", start_position[0], steps, width)
            if start_position[0] + steps >= width:
                diff = start_position[0] + steps - width + 1    
                new_map = [[0] * (width+diff) for _ in range(height)]
                for i in range(height):
                    for j in range(width):
                        new_map[i][j] = map[i][j]
                map = new_map
                width += diff
                start_position = (start_position[0], start_position[1])
            #printMap(map)
            for i in range(int(line[1])):
                map[start_position[1]][start_position[0] + i] = 1
            start_position = (start_position[0]+steps, start_position[1])
            
        else:
            print(direction)
            raise ValueError("Invalid direction")
        
        
    #printMap(map)
    #input()
        
    # flood fill from edges
    stack = []
    for i in range(width):
        if map[0][i] == 0:
            stack.append((i, 0))
        if map[height-1][i] == 0:
            stack.append((i, height-1))
    for i in range(height):
        if map[i][0] == 0:
            stack.append((0, i))
        if map[i][width-1] == 0:
            stack.append((width-1, i))
            
    while stack != []:
        x, y = stack.pop()
        if map[y][x] == 0:
            map[y][x] = 2
            if x > 0:
                stack.append((x-1, y))
            if x < width-1:
                stack.append((x+1, y))
            if y > 0:
                stack.append((x, y-1))
            if y < height-1:
                stack.append((x, y+1))
                
    #printMap(map)
    
    # sum 1 and 0
    s = 0
    for i in range(height):
        for j in range(width):
            if map[i][j] == 1 or map[i][j] == 0:
                s += 1
                
    print(s)
        
def printMap(map):
    for line in map:
        for c in line:
            if c == 0:
                print(".", end="")
            else:
                print("#", end="")
        print()
    print()
    
def shoelaceArea(points):
    # https://en.wikipedia.org/wiki/Shoelace_formula
    # points is a list of (x, y) tuples
    # points = [(x1, y1), (x2, y2), ...]
    # points = [(x1, y1), (x2, y2), ..., (x1, y1)]
    #print(points)
    n = len(points)
    area = 0
    for i in range(n-1):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    area += points[n-1][0] * points[0][1] - points[0][0] * points[n-1][1]
    return abs(area) / 2

if __name__ == '__main__':
    main()