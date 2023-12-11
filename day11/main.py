times = 10

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
    
    for i in range(len(double_row)):
        double_row[i] += i
    for i in range(len(double_col)):
        double_col[i] += i
    print(double_row)
    print(double_col)
    new_galaxy = [[0]*(len(galaxy[0])+len(double_col)) for i in range(len(galaxy)+len(double_row))]
    i = 0
    j = 0
    for row in range(len(new_galaxy)):
        for col in range(len(new_galaxy[row])):
            if row in double_row or col in double_col:
                new_galaxy[row][col] = "."
            else:
                new_galaxy[row][col] = galaxy[i][j]
                j += 1
            # for a in new_galaxy:
            #     for b in a:
            #         print(b, end=" ")
            #     print()
            # input()
        if row not in double_row:
            i += 1
        j = 0
        
    for row in new_galaxy:
        for col in row:
            print(col, end=" ")
        print()
        
    list_of_planets = []
    for i in range(len(new_galaxy)):
        for j in range(len(new_galaxy[i])):
            if new_galaxy[i][j] != ".":
                list_of_planets.append((i,j))
                
    print(list_of_planets)
    
    s = 0
    for i in range(len(list_of_planets)):
        for j in range(i+1, len(list_of_planets)):
            s += abs(list_of_planets[i][0] - list_of_planets[j][0]) + abs(list_of_planets[i][1] - list_of_planets[j][1])
            print(s, list_of_planets[i], list_of_planets[j])
            
    print(s)
main()