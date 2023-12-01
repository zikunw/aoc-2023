def main():
    
    # Part 1
    
    s = 0
    # read input
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            # find first digit
            for c in line:
                if c.isdigit():
                    first_digit = c
                    break
            
            # find last digit
            for c in reversed(line):
                if c.isdigit():
                    second_digit = c
                    break
            
            num = int(first_digit+second_digit)
            s += num
    print("part 1", s)
    
    # Part 2
    
    d = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    def process(line):
        new_line = ""
        for i in range(len(line)):
            if i+4 <= len(line) and line[i:i+4] in d:
                new_line += d[line[i:i+4]]
            elif i+3 <= len(line) and line[i:i+3] in d:
                new_line += d[line[i:i+3]]
            elif i+5 <= len(line) and line[i:i+5] in d:
                new_line += d[line[i:i+5]]
            elif line[i].isdigit():
                new_line += line[i]
        return new_line
    
    s = 0
    # read input
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = process(line)
            
            # find first digit
            for c in line:
                if c.isdigit():
                    first_digit = c
                    break
            
            # find last digit
            for c in reversed(line):
                if c.isdigit():
                    second_digit = c
                    break
            num = int(first_digit+second_digit)
            s += num
    print("part 2", s)
main()