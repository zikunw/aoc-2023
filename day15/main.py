def main():
    input_str = open("day15/input.txt", "r").readlines()
    g = input_str[0].strip().split(",")
        
    print(g)
    s = 0
    for i in range(len(g)):
        s += myHash(g[i])
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