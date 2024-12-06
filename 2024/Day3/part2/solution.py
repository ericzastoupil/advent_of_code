import re

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.read()

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    locations = [(match.start(0), match.end(0)) for match in re.finditer(pattern, lines)]

    sum = 0
    for l in locations:
        do = lines.rfind('do()', 0, l[0])
        dont = lines.rfind("don't()", 0, l[0])
        if do >= dont:
            sum += int(lines[l[0] + 4 : l[1] - 1].split(',')[0]) * int(lines[l[0] + 4 : l[1] - 1].split(',')[1])
    
    print("Solution: " + str(sum))