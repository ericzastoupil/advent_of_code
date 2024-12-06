import re

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.read()

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    matches = re.findall(pattern, lines)

    sum = 0
    for match in matches:
        nums = match[match.index('(') + 1:match.index(')')]
        sum += int(nums.split(',')[0]) * int(nums.split(',')[1])

    print("Solution: " + str(sum))