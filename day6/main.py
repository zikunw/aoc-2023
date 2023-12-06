import concurrent.futures

def main():
    #part1()
    part2()
    
def part1():
    with open("day6/input.txt", "r") as file:
        lines = file.readlines()
        times = [int(n) for n in lines[0][6:].strip().split(" ") if n != ""]
        distances = [int(n) for n in lines[1][9:].strip().split(" ") if n != ""]
        print(times)
        print(distances)
    
    result = 1
    for i in range(len(times)):
        print(times[i], distances[i])
        counter = 0
        for time_press in range(times[i] + 1):
            print(time_press * (times[i]-time_press), distances[i])
            if time_press * (times[i]-time_press) > distances[i]:
                counter += 1
                
        print(counter)
    
        result *= counter
        
    print(result)

def part2():
    with open("day6/input.txt", "r") as file:
        lines = file.readlines()
        times = int("".join([n for n in lines[0][6:].strip().split(" ") if n != ""]))
        distances = int("".join([n for n in lines[1][9:].strip().split(" ") if n != ""]))
        print(times)
        print(distances)
    
    counter = 0
    for time_press in range(times + 1):
        if time_press * (times-time_press) > distances:
            counter += 1
            
    print(counter)


main()