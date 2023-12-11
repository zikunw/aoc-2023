times = 1000000

def main():
    input_str = open("day11/input.txt", "r").readlines()
    input_str = [list(line.strip()) for line in input_str]
    
    #print(input_str)
    
    galaxy = input_str
    
    double_row = []
    double_col = []
    for i in range(len(galaxy)):
        empty_row = True
        empty_col = True 
        for j in range(len(galaxy[i])):
            if galaxy[i][j] != ".":
                empty_row = False
            if galaxy[j][i] != ".":
                empty_col = False
                
        if empty_row:
            double_row.append(i)
        if empty_col:
            double_col.append(i)
    
    # mark the double rows and columns with X
    for i in double_row:
        for j in range(len(galaxy[i])):
            galaxy[i][j] = "X"
    for i in double_col:
        for j in range(len(galaxy)):
            galaxy[j][i] = "X"
        
    for row in galaxy:
        for col in row:
            print(col, end=" ")
        print()
        
    list_of_planets = []
    for i in range(len(galaxy)):
        for j in range(len(galaxy[i])):
            if galaxy[i][j] == "#":
                list_of_planets.append((i,j))
                
    print(list_of_planets)
    
    s = 0
    for i in range(len(list_of_planets)):
        for j in range(i+1, len(list_of_planets)):
            s += abs(list_of_planets[i][0] - list_of_planets[j][0]) + abs(list_of_planets[i][1] - list_of_planets[j][1])
            for k in range(len(double_row)):
                if max(list_of_planets[i][0], list_of_planets[j][0]) >= double_row[k] and min(list_of_planets[i][0], list_of_planets[j][0]) <= double_row[k]:
                    s += times-1
            for k in range(len(double_col)):
                if max(list_of_planets[i][1], list_of_planets[j][1]) >= double_col[k] and min(list_of_planets[i][1], list_of_planets[j][1]) <= double_col[k]:
                    s += times-1
            print(s, list_of_planets[i], list_of_planets[j])
            
    print(s)
main()