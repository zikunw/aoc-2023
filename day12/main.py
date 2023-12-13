from itertools import combinations_with_replacement

import itertools

def main():
    input_str = open("day12/example.txt", "r").readlines()
    lines = [list(line.strip().split(" ")) for line in input_str]
    
    #lines = [[list(map(int, line[1].split(","))), line[0]] for line in lines]
    lines = [[list(map(int, line[1].split(",")))*5, ((line[0]+"?")*5)[:-1]] for line in lines]
    
    for line in lines:
        print(line)
        
    s = 0
    k = 0
    for line in lines:
        k += 1
        cur_sum = 0
        num_question_marks = line[1].count("?")
        for comb in itertools.product([".", "#"], repeat=num_question_marks):
            i = 0
            nline = list(line[1])
            for j in range(len(nline)):
                if nline[j] == "?":
                    nline[j] = comb[i]
                    i += 1

            nline = "".join(nline).split(".")
            nline = [n for n in nline if n != ""]
            nline = [len(n) for n in nline]
            if nline == line[0]:
                s += 1
                cur_sum += 1
        print(k, cur_sum)
            
    print("sum", s)
    
    
    
if __name__ == "__main__":
    main()