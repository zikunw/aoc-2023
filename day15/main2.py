def main():
    input_str = open("day15/input.txt", "r").readlines()
    g = [e.split("=") for e in input_str[0].strip().split(",")]
        
    print(g)
    # s = 0
    # for i in range(len(g)):
    #     s += myHash(g[i])
    # print(s)
    
    # print(myHash("rn"))
    # print(myHash("qp"))
    boxes = [[] for i in range(256)]
    hboxes = {}
    
    for e in g:
        if len(e) == 2:
            if e[0] in hboxes:
                hboxes[e[0]] = e[1]
            else:
                boxes[myHash(e[0])].append(e[0])
                hboxes[e[0]] = e[1]
        else: # minus
            if e[0][:-1] in hboxes:
                boxes[myHash(e[0][:-1])].remove(e[0][:-1])
                del hboxes[e[0][:-1]]
            
    print(boxes)
    print(hboxes)
    
    s = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            s += (i+1) * (j+1) * int(hboxes[boxes[i][j]])
            
    print(s)
    
def myHash(s):
    curVal = 0
    for c in s:
        curVal += ord(c)
        curVal *= 17
        curVal = curVal % 256
        
    return curVal
    
if __name__ == "__main__":
    main()