def look(char, i, j):
    if char == lines[i][j]:
        return True
    return False

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()

    MAX_I = len(lines)
    total = 0

    for i in range(1,len(lines) - 1):
        MAX_J = len(lines[i])
        for j in range(1, len(lines[i]) - 1):
            if lines[i][j] == 'A':
                #M's on top
                if look('M', i - 1, j - 1) and look('M', i - 1, j + 1) and look('S', i + 1, j - 1) and look('S', i + 1, j + 1):
                    total += 1
                #M's on right
                elif look('M', i - 1, j + 1) and look('M', i + 1, j + 1) and look('S', i - 1, j - 1) and look('S', i + 1, j - 1):
                    total += 1
                #M's on bottom
                elif look('M', i + 1, j - 1) and look('M', i + 1, j + 1) and look('S', i - 1, j - 1) and look('S', i - 1, j + 1):
                    total += 1
                #M's on left
                elif look('M', i - 1, j - 1) and look('M', i + 1, j - 1) and look('S', i - 1, j + 1) and look('S', i + 1, j + 1):
                    total += 1

    print ("Solution: ", total)