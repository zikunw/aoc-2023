def main():
    part1()
    part2()
    
def part1():
    with open("day2/input.txt", "r") as f:
        s = 0
        for line in f:
            line = line.strip()
            id = line.split(":")[0].split(" ")[1]
            line = line.split(":")
            games = line[1].split(";")
            valid = True
            for game in games:
                game = game.strip().split(",")
                #print(game)
                for show in game:
                    show = show.strip()
                    # if blue
                    if show.split(" ")[1][0] == "b":
                        if int(show.split(" ")[0]) > 14:
                            valid = False
                            break
                    if show.split(" ")[1][0] == "r":
                        if int(show.split(" ")[0]) > 12:
                            valid = False
                            break
                    if show.split(" ")[1][0] == "g":
                        if int(show.split(" ")[0]) > 13:
                            valid = False
                            break
            if valid:
                print("id", id)
                s += int(id)
        print(s)
        
def part2():
    with open("day2/input.txt", "r") as f:
        s = 0
        for line in f:
            line = line.strip()
            line = line.split(":")
            games = line[1].split(";")
            
            min_red = 0
            min_green = 0
            min_blue = 0
            
            for game in games:
                game = game.strip().split(",")
                #print(game)
                for show in game:
                    show = show.strip()
                    # if blue
                    if show.split(" ")[1][0] == "b":
                        min_blue = max(min_blue, int(show.split(" ")[0]))
                    if show.split(" ")[1][0] == "r":
                        min_red = max(min_red, int(show.split(" ")[0]))
                    if show.split(" ")[1][0] == "g":
                        min_green = max(min_green, int(show.split(" ")[0]))
            p = min_red * min_green * min_blue
            s += p
        print(s)
                    
main()