import math
import time

def main():
    # print(overlap_ranges((74, 14), (64, 13)))
    # print(overlap_ranges((0, 10), (2, 5)))
    # print(overlap_ranges((0, 1), (2, 5)))
    # print(overlap_ranges((0, 5), (2, 5)))
    #print(overlap_ranges((79, 14), (50, 48)))
    #print(overlap_ranges((77, 11), (64, 13)))
    better_part2()

def part1():
    # Read input
    with open("day5/input.txt", "r") as file:
        lines = file.readlines()
        seeds = [int(n) for n in lines[0][6:].strip().split(" ")]
        print(seeds)
        
        ms = [[] for _ in range(7)]
        cur_m = -1
        for line in lines[1:]:
            if line == "\n":
                continue
            if "map" in line:
                cur_m += 1
                continue
            ms[cur_m].append([int(n) for n in line.strip().split(" ")])
            
        min_soil = math.inf
        for seed in seeds:
            #print("Seed: ", seed)
            cur_value = seed
            for m_index in range(7):
                # try to find the value
                for entry in ms[m_index]:
                    if cur_value >= entry[1] and cur_value <= entry[1] + entry[2]:
                        #print("Found: ", entry)
                        cur_value = entry[0] + (cur_value - entry[1])
                        break
                # if not we just use the last value
                #print(cur_value)
            #print(cur_value)
            min_soil = min(min_soil, cur_value)
        print(min_soil)
        
def part2():
    # Read input
    with open("day5/input.txt", "r") as file:
        lines = file.readlines()
        seeds = [int(n) for n in lines[0][6:].strip().split(" ")]
        
        ms = [[] for _ in range(7)]
        cur_m = -1
        for line in lines[1:]:
            if line == "\n":
                continue
            if "map" in line:
                cur_m += 1
                continue
            ms[cur_m].append([int(n) for n in line.strip().split(" ")])
            
        min_soil = math.inf
        for i in range(len(seeds)):
            if i % 2 == 1: continue
            print(i, seeds[i], seeds[i+1])
            for j in range(seeds[i], seeds[i] + seeds[i+1]):
                seed = j
                if seed % 1000 == 0:
                    print("Seed: ", seed, j-seeds[i], "/", seeds[i+1])
                cur_value = seed
                for m_index in range(7):
                    # try to find the value
                    for entry in ms[m_index]:
                        if cur_value >= entry[1] and cur_value <= entry[1] + entry[2]:
                            #print("Found: ", entry)
                            cur_value = entry[0] + (cur_value - entry[1])
                            break
                    # if not we just use the last value
                    #print(cur_value)
                #print(cur_value, end=" ")
                min_soil = min(min_soil, cur_value)
        print(min_soil)

def better_part2():
    # Read input
    with open("day5/input.txt", "r") as file:
        lines = file.readlines()
        seeds = [int(n) for n in lines[0][6:].strip().split(" ")]
        
        ms = [[] for _ in range(7)]
        cur_m = -1
        for line in lines[1:]:
            if line == "\n":
                continue
            if "map" in line:
                cur_m += 1
                continue
            ms[cur_m].append([int(n) for n in line.strip().split(" ")])
        
        # sort every m in ms by the first value
        for m in ms:
            m.sort(key=lambda x: x[1])
            
        min_soil = math.inf
        for i in range(len(seeds)):
            if i % 2 == 1: continue
            print(i, seeds[i], seeds[i+1])
            
            # (base, range)
            cur_num_seg = [(seeds[i], seeds[i+1])]
            for m in ms:
                new_num_seg = []
                while cur_num_seg != []:
                    seg = cur_num_seg.pop()
                    has_split = False
                    for entry in m:
                        overlap, remains = overlap_ranges(seg, (entry[1], entry[2]))
                        if overlap != (0, 0):
                            new_num_seg.append((overlap[0]+entry[0]-entry[1], overlap[1]))
                            has_split = True
                            if len(remains) > 0:
                                cur_num_seg += remains
                            break
                            
                    if not has_split:
                        new_num_seg.append(seg)
                    
                cur_num_seg = new_num_seg
                
            for seg in cur_num_seg:
                min_soil = min(min_soil, seg[0])
                
        print(min_soil)

# given two (base, range) tuples, return [(base, range with overlap), [(base, range without overlap)]]
def overlap_ranges(tuple1, tuple2):
    print("overlap_ranges:", tuple1, tuple2)
    base1, range1 = tuple1
    base2, range2 = tuple2

    end1 = base1 + range1
    end2 = base2 + range2

    # Check for overlap
    if base1 <= end2 and base2 <= end1:
        # Find the start of the overlap
        start = max(base1, base2)

        # Find the end of the overlap
        end = min(end1, end2)

        # Find the length of the overlap
        length = end - start 
        
        if length == 0:
            print("return 1")
            return [(0, 0), [(base1, range1)]]

        # complete overlap
        if start == tuple1[0] and length == tuple1[1]:
            print("return 2")
            return [(start, length), []]
        
        if base1 <= base2 <= end1 <= end2:
            print("return 3")
            return [(start, length), [(base1, start-base1)]]
        
        if base2 <= base1 <= end2 <= end1:
            print("return 4")
            return [(start, length), [(end2, end1-end2)]]
        
        if base1 <= base2 <= end2 <= end1:
            print("return 5")
            return [(start, length), [(base1, base2-base1), (end2, end1-end2)]]
        
        raise("Unhandled cases.")
    else:
        # If there is no overlap, return the input tuples as is
        return [(0, 0), [tuple1]]


main()