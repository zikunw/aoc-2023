from enum import Enum
import queue

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
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

class traversed:
    def __init__(self, x, y, cost, direction, direction_times, history = []):
        self.x = x
        self.y = y
        self.cost = cost
        self.direction = direction              # 0 = up, 1 = down, 2 = left, 3 = right
        self.direction_times = direction_times  # how many times we have gone in this direction, no more than 3
        self.history = history
        
    def next_directions(self):
        r = []
        if self.direction_times < 10:
            r.append(self.direction)
        if self.direction_times > 3:
            r.append(self.direction.left())
            r.append(self.direction.right())
        return r
    
    def toVisited(self):
        return f"{self.x},{self.y},{self.direction},{self.direction_times}"
    
    def __repr__(self) -> str:
        return f"(x{self.x}, y{self.y}, c{self.cost}, d{self.direction}, dt{self.direction_times})"

    def __str__(self) -> str:
        return f"(x{self.x}, y{self.y}, c{self.cost}, d{self.direction}, dt{self.direction_times})"
    
    def __eq__(self, __value: object) -> bool:
        if self.cost != __value.cost:
            return False
    
    def __lt__(self, __value: object) -> bool:
        if self.cost < __value.cost:
            return True
        elif self.cost > __value.cost:
            return False
        
        return False
        

def main():
    with open("day17/input.txt", "rb") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        m = [[int(chr(c)) for c in line] for line in data]
        print(m)
        
    rows = len(m)
    cols = len(m[0])
    
    print(rows, cols)
    
    q = queue.PriorityQueue()
    s1 = traversed(x=0, y=0, cost=0, direction=Direction.RIGHT, direction_times=0)
    s2 = traversed(x=0, y=0, cost=0, direction=Direction.DOWN, direction_times=0)
    q.put(s1)
    q.put(s2)
    visted = set()
    
    while not q.empty():
        task = q.get()
        print(task.cost, task)
        if task.toVisited() in visted:
            continue
        visted.add(task.toVisited())
        nextDirections = task.next_directions()
        for direction in nextDirections:
            offset = direction.offset()
            x = task.x + offset[0]
            y = task.y + offset[1]
            if x < 0 or y < 0 or x >= len(m[0]) or y >= len(m):
                continue
            cost = task.cost + m[y][x]
            if x == len(m[0]) - 1 and y == len(m) - 1:
                print("Found the exit!")
                print(cost)
                # print(task.history)
                # graphHistory(m, task.history)
                return cost
            new_direction_times = 1 if direction != task.direction else task.direction_times + 1
            q.put(traversed(x=x, y=y, cost=cost, direction=direction, direction_times=new_direction_times, history=task.history + [f"x{x},y{y},c{cost},d{direction},dt{new_direction_times}"]))
        
        #print(q.queue)
        #input()

def graphHistory(m, history):
    for h in history:
        print(h)
        x = h.split(",")[0].split("x")[1]
        y = h.split(",")[1].split("y")[1]
        dir = h.split(",")[3].split("d")[1]
        m[int(y)][int(x)] = dir
        
        for line in m:
            for c in line:
                if str(c) in "<>^v":
                    print(bcolors.WARNING+str(c)+bcolors.ENDC, end="")
                else:
                    print(c, end="")
            print()
            
        input()

if __name__ == "__main__":
    main()
    
    # print(Direction.LEFT.left())
    # print(Direction.LEFT.right())