def look_left(char, start_i, start_j):
    if start_j > -1 and char == lines[start_i][start_j]:
        if char == 'M':
            return look_left('A', start_i, start_j - 1)
        elif char == 'A':
            return look_left('S', start_i, start_j - 1)
        elif char == 'S':
            return 1
    return 0

def look_up_left(char, start_i, start_j):
    if start_i > -1 and start_j > -1 and char == lines[start_i][start_j]:
        if char == 'M':
            return look_up_left('A', start_i - 1, start_j - 1)
        elif char == 'A':
            return look_up_left('S', start_i - 1, start_j - 1)
        elif char == 'S':
            return 1
    return 0

def look_up(char, start_i, start_j):
    if start_i > -1 and char == lines[start_i][start_j]:
        if char == 'M':
            return look_up('A', start_i - 1, start_j)
        elif char == 'A':
            return look_up('S', start_i - 1, start_j)
        elif char == 'S':
            return 1
    return 0

def look_up_right(char, start_i, start_j):
    if start_i > -1 and start_j < MAX_J and char == lines[start_i][start_j]:
        if char == 'M':
            return look_up_right('A', start_i - 1, start_j + 1)
        elif char == 'A':
            return look_up_right('S', start_i - 1, start_j + 1)
        elif char == 'S':
            return 1
    return 0

def look_right(char, start_i, start_j):
    if start_j < MAX_J and char == lines[start_i][start_j]:
        if char == 'M':
            return look_right('A', start_i, start_j + 1)
        elif char == 'A':
            return look_right('S', start_i, start_j + 1)
        elif char == 'S':
            return 1
    return 0

def look_down_right(char, start_i, start_j):
    if start_i < MAX_I and start_j < MAX_J and char == lines[start_i][start_j]:
        if char == 'M':
            return look_down_right('A', start_i + 1, start_j + 1)
        elif char == 'A':
            return look_down_right('S', start_i + 1, start_j + 1)
        elif char == 'S':
            return 1
    return 0

def look_down(char, start_i, start_j):
    if start_i < MAX_I and char == lines[start_i][start_j]:
        if char == 'M':
            return look_down('A', start_i + 1, start_j)
        elif char == 'A':
            return look_down('S', start_i + 1, start_j)
        elif char == 'S':
            return 1
    return 0

def look_down_left(char, start_i, start_j):
    if start_i < MAX_I and start_j > -1 and char == lines[start_i][start_j]:
        if char == 'M':
            return look_down_left('A', start_i + 1, start_j - 1)
        elif char == 'A':
            return look_down_left('S', start_i + 1, start_j - 1)
        elif char == 'S':
            return 1
    return 0

if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()

    MAX_I = len(lines)
    total = 0
    Xs = 0

    for i in range(len(lines)):
        MAX_J = len(lines[i])
        for j in range(len(lines[i])):
            if lines[i][j] == 'X':  
                Xs += 1
                total += look_left('M', i, j - 1)
                total += look_up_left('M', i - 1, j - 1)
                total += look_up('M', i - 1, j)
                total += look_up_right('M', i - 1, j + 1)
                total += look_right('M', i, j + 1)
                total += look_down_right('M', i + 1, j + 1)
                total += look_down('M', i + 1, j)
                total += look_down_left('M', i + 1, j - 1)

    print ("Solution: ", total)