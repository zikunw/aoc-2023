from functools import * 
import time

def main():
    input_str = open("day9/input.txt", "r").readlines()
    input_str = [line.strip().split() for line in input_str]
    
    lines = []
    for line in input_str:
        lines += [[int(n) for n in line]]
    print(lines)
    
    histories = [process(line) for line in lines]
    print(histories)
    
    results = [getResult(history) for history in histories]
    print(sum(results))
    results = [getResult2(history) for history in histories]
    print(sum(results))
    
def process(line):
    history = [line]
    while True:
        if len(set(history[-1])) == 1 and history[-1][0] == 0:
            break
        diff = []
        for i in range(len(history[-1])-1):
            diff += [(history[-1][i+1]-history[-1][i])]
        history += [diff]
    return history

def getResult(history):
    cur = history[-1][-1]
    for i in range(len(history)-2, -1, -1):
        cur = history[i][-1] + cur
    return cur
    
def getResult2(history):
    cur = history[-1][0]
    for i in range(len(history)-2, -1, -1):
        cur = history[i][0] - cur
    return cur

if __name__ == "__main__":
    main()