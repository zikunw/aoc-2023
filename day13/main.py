def main():
    input_str = open("day13/input.txt", "r").readlines()
    lines = [list(line.strip().split(" ")) for line in input_str]
    
    blocks = []
    cur_block = []
    for line in lines:
        print(line)
        if line == ['']:
            blocks.append(cur_block)
            cur_block = []
        else:
            cur_block.append(line[0])
    blocks.append(cur_block)
    
    #print(blocks[0])
    s = 0
    for b in blocks:
        row, col = findMirror(b)
        if not(row == -1 or row == len(b)-1):
            s += (row+1) * 100
        else:
            s += col
        for r in b:
            print(r)
        print(row, col, s, "\n")
            
    print(s)
    
def findMirror(block):
    # find row with mirror
    row = -1
    for i in range(len(block)-1):
        up = i
        down = i+1
        not_mirror = False
        while down < len(block) and up >= 0:
            print(up, down, block[up], block[down])
            if block[up] != block[down]:
                not_mirror = True
                break
            up -= 1
            down += 1
        if not not_mirror:
            print("haha")
            row = i
            break
    print(row)

    # find column with mirror
    col = -1
    print("col")
    for i in range(len(block[0])-1):
        left = i
        right = i+1
        not_mirror = False
        while right < len(block[0]) and left >= 0:
            #print(left, right, block[0][left], block[0][right])
            # check entire column
            for j in range(len(block)):
                if block[j][left] != block[j][right]:
                    not_mirror = True
                    break
            left -= 1
            right += 1
        if not not_mirror:
            col = i
            break
    print(col)
    return row, col+1     
    
if __name__ == "__main__":
    main()