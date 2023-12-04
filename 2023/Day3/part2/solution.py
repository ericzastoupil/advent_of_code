
def isValidPos(i, j, n, m):
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

def check_surroundings(i, j):
    if (isValidPos(i - 1, j - 1, n, m)):
        if text_grid[i - 1][j - 1] == '*':
            return True, [i - 1, j - 1]
    if (isValidPos(i - 1, j, n, m)):
        if text_grid[i - 1][j]  == '*':
            return True, [i - 1, j]
    if (isValidPos(i - 1, j + 1, n, m)):
        if text_grid[i - 1][j + 1]  == '*':
            return True, [i - 1, j + 1]
    if (isValidPos(i, j - 1, n, m)):
        if text_grid[i][j - 1]  == '*':
            return True, [i, j - 1]
    if (isValidPos(i, j + 1, n, m)):
        if text_grid[i][j + 1]  == '*':
            return True, [i, j + 1]
    if (isValidPos(i + 1, j - 1, n, m)):
        if text_grid[i + 1][j - 1]  == '*':
            return True, [i + 1, j - 1]
    if (isValidPos(i + 1, j, n, m)):
        if text_grid[i + 1][j]  == '*':
            return True, [i + 1, j]
    if (isValidPos(i + 1, j + 1, n, m)):
        if text_grid[i + 1][j + 1]  == '*':
            return True, [i + 1, j + 1]
 
    return False, [0,0]

def create_grid(lines):
    result = []
    zeroes = []
    for line in lines:
        chars = []
        zero_line = []
        for char in line:
            chars.append(char)
            zero_line.append([1,0])
        result.append(chars)
        zeroes.append(zero_line)

    return result, zeroes

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    text_grid, zeroes = create_grid(lines)
    n = len(text_grid)
    m = len(text_grid[0])

    part_numbers = []
    number = ''
    adjacent_to_star = False
    star_location = []
    gear_dict = {}

    for i, row in enumerate(text_grid):
        for j, char in enumerate(row):
            if char.isdigit():
                number += char
                if not adjacent_to_star:
                    adjacent_to_star, star_location = check_surroundings(i, j)
            elif number:
                if adjacent_to_star:
                    gear_dict[number] = star_location
                    zeroes[star_location[0]][star_location[1]][0] *= int(number)
                    zeroes[star_location[0]][star_location[1]][1] += 1
                number = ''
                adjacent_to_star = False

    final = 0
    for row in zeroes:
        for element in row:
            if element[1] == 2:
                final += element[0]
    print(final)