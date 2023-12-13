import time

def main():
    input_str = open("day12/input.txt", "r").readlines()
    lines = [list(line.strip().split(" ")) for line in input_str]
    
    lines = [[list(map(int, line[1].split(",")))*5, ((line[0]+"?")*5)[:-1]] for line in lines]
    
    s = 0
    opt_s = 0
    
    start = time.time()
    for line in lines:
        s += dp(line)
    end = time.time() - start
    print("sum    ", s, "time:", end)
    
    # start = time.time()
    # for line in lines:
    #     opt_s += opt_dp(line)
    # end = time.time() - start
            
    # print("opt_sum", opt_s, "time:", end)
    
    
def dp(line):
    pattern = line[0]
    s = line[1]
    mem = {}
    
    def rec(i, cur, prev_hash_count):
        #print("REC", s[i:], cur, prev_hash_count)
        
        if cur == []: 
            if prev_hash_count != 0: return 0
            if i == len(s): return 1
            if s[i] == "#": return 0
            return rec(i+1, cur, 0)

        if i >= len(s):  return 0
            
        se = serialize(i, cur, prev_hash_count)        
        if se in mem: return mem[se]
        
        if s[i] == ".": 
            if prev_hash_count != 0:
                if cur[0] != 1:
                    mem[se] = 0
                    return 0
                else:
                    mem[se] = rec(i+1, cur[1:], 0)
                    return mem[se]
            mem[se] = rec(i+1, cur, 0)
            return mem[se]
        
        if s[i] == "#":
            hash_count = 1 + prev_hash_count
            if hash_count > cur[0]:
                mem[se] = 0
                return 0
            elif hash_count == cur[0]:
                if i+1 < len(s) and s[i+1] == "#":
                    mem[se] = 0
                    return 0
                elif i+1 < len(s) and s[i+1] == "?":
                    mem[se] = rec(i+2, cur[1:], 0)
                    return mem[se]
                mem[se] = rec(i+1, cur[1:], 0)
                return mem[se]
            mem[se] = rec(i+1, cur, hash_count)
            return mem[se]

        # if s[i] == "?"
        # when we place a #
        num_hash_we_want = cur[0]-1-prev_hash_count
        if num_hash_we_want < 0:
            n1 = 0
        else:
            j = i+1
            while num_hash_we_want > 0 and j < len(s) and s[j] in "#?":
                num_hash_we_want -= 1
                j += 1
            if num_hash_we_want > 0: # invalid
                n1 = 0
            else:
                if j < len(s) and s[j] == "#":
                    n1 = 0
                elif j < len(s) and s[j] == "?":
                    n1 = rec(j+1, cur[1:], 0)
                else:
                    n1 = rec(j, cur[1:], 0)
            
        # when we place a .
        if prev_hash_count != 0:
            n2 = 0
        else:
            n2 = rec(i+1, cur, 0)
        #print(s[i:].rjust(15, ' '), "  ", str(cur).ljust(20, ' '), "place:", n1, "not place:", n2,", j:", j, s[j:] )
        mem[se] = n1 + n2
        return mem[se]
    
    
    return rec(0, pattern, 0)
    #print("mem", mem)


def opt_dp(line):
    pattern = line[0]
    s = line[1]
    locations_of_question_mark = [i for i in range(len(s)) if s[i] == "?"]
    cur_offset = len(pattern) + 1
    max_hash_count = max(pattern)
    print("size of mem:", len(locations_of_question_mark)*cur_offset*max_hash_count,"lo_question:", len(locations_of_question_mark), "cur_offset:", cur_offset, "max_hash_count:", max_hash_count)
    # mem[i][cur_offset][prev_hash_count]
    mem = [[[-1 for _ in range(max_hash_count)] for _ in range(cur_offset)] for _ in range(len(locations_of_question_mark)+1)]
    
    def rec(i, cur_offset, prev_hash_count):
        
        # se = serialize(i, cur, prev_hash_count)        
        # if se in mem: return mem[se]
        if mem[i][cur_offset][prev_hash_count] != -1: 
            return mem[i][cur_offset][prev_hash_count]
        
        if cur_offset == len(pattern): 
            if prev_hash_count != 0: return 0
            if i == len(s): return 1
            if s[i] == "#": return 0
            mem[i][cur_offset][prev_hash_count] = rec(i+1, cur_offset, 0)
            return mem[i][cur_offset][prev_hash_count] 

        if i >= len(s):  return 0
            
        if s[i] == ".": 
            if prev_hash_count != 0:
                if pattern[cur_offset] != 1:
                    mem[i][cur_offset][prev_hash_count] = 0
                    return 0
                else:
                    mem[i][cur_offset][prev_hash_count] = rec(i+1, cur_offset+1, 0)
                    return mem[i][cur_offset][prev_hash_count]
            mem[i][cur_offset][prev_hash_count] = rec(i+1, cur_offset, 0)
            return mem[i][cur_offset][prev_hash_count]
        
        if s[i] == "#":
            hash_count = 1 + prev_hash_count
            if hash_count > pattern[cur_offset]:
                mem[i][cur_offset][prev_hash_count] = 0
                return 0
            elif hash_count == pattern[cur_offset]:
                if i+1 < len(s) and s[i+1] == "#":
                    mem[i][cur_offset][prev_hash_count] = 0
                    return 0
                elif i+1 < len(s) and s[i+1] == "?":
                    mem[i][cur_offset][prev_hash_count] = rec(i+2, cur_offset+1, 0)
                    return mem[i][cur_offset][prev_hash_count]
                mem[i][cur_offset][prev_hash_count] = rec(i+1, cur_offset+1, 0)
                return mem[i][cur_offset][prev_hash_count]
            mem[i][cur_offset][prev_hash_count] = rec(i+1, cur_offset, hash_count)
            return mem[i][cur_offset][prev_hash_count]

        # if s[i] == "?"
        # when we place a #
        num_hash_we_want = pattern[cur_offset]-1-prev_hash_count
        if num_hash_we_want < 0:
            n1 = 0
        else:
            j = i+1
            while num_hash_we_want > 0 and j < len(s) and s[j] in "#?":
                num_hash_we_want -= 1
                j += 1
            if num_hash_we_want > 0: # invalid
                n1 = 0
            else:
                if j < len(s) and s[j] == "#":
                    n1 = 0
                elif j < len(s) and s[j] == "?":
                    n1 = rec(j+1, cur_offset+1, 0)
                else:
                    n1 = rec(j, cur_offset+1, 0)
            
        # when we place a .
        if prev_hash_count != 0:
            n2 = 0
        else:
            n2 = rec(i+1, cur_offset, 0)
        
        #print(s[i:].rjust(15, ' '), "  ", str(cur).ljust(20, ' '), "place:", n1, "not place:", n2,", j:", j, s[j:] )
        mem[i][cur_offset][prev_hash_count] = n1 + n2
        return mem[i][cur_offset][prev_hash_count]
    
    #r = rec(0, 0, 0)
    #print("mem with value", sum([sum([sum([1 if mem[i][j][k] != -1 else 0 for k in range(max_hash_count)]) for j in range(cur_offset)]) for i in range(len(s)+1)]))
    
    return 0

# serialize
def serialize(i, cur, prev_hash_count):
    return str(i) + "," + str(cur) + "," + str(prev_hash_count)
        

if __name__ == "__main__":
    main()