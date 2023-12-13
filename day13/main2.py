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

    print(s)
    
def findMirror(block):
    # find row with mirror
    row = -1
    for i in range(len(block)-1):
        up = i
        down = i+1
        smack = 0
        while down < len(block) and up >= 0:
            for j in range(len(block[up])):
                if block[up][j] != block[down][j]:
                    smack += 1
                    if smack > 1:
                        break
            up -= 1
            down += 1
        if smack == 1:
            row = i
            break

    # find column with mirror
    col = -1
    for i in range(len(block[0])-1):
        left = i
        right = i+1
        smack = 0
        while right < len(block[0]) and left >= 0:
            for j in range(len(block)):
                if block[j][left] != block[j][right]:
                    smack += 1
                    if smack > 1:
                        break
            left -= 1
            right += 1
        if smack == 1:
            col = i
            break
    return row, col+1     
    
if __name__ == "__main__":
    main()