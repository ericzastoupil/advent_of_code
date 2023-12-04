
def isValidPos(i, j, n, m):
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

def check_surroundings(i, j):
    non_symbols = ['.', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
 
    if (isValidPos(i - 1, j - 1, n, m)):
        if text_grid[i - 1][j - 1] not in non_symbols:
            return True
    if (isValidPos(i - 1, j, n, m)):
        if text_grid[i - 1][j] not in non_symbols:
            return True
    if (isValidPos(i - 1, j + 1, n, m)):
        if text_grid[i - 1][j + 1] not in non_symbols:
            return True
    if (isValidPos(i, j - 1, n, m)):
        if text_grid[i][j - 1] not in non_symbols:
            return True
    if (isValidPos(i, j + 1, n, m)):
        if text_grid[i][j + 1] not in non_symbols:
            return True
    if (isValidPos(i + 1, j - 1, n, m)):
        if text_grid[i + 1][j - 1] not in non_symbols:
            return True
    if (isValidPos(i + 1, j, n, m)):
        if text_grid[i + 1][j] not in non_symbols:
            return True
    if (isValidPos(i + 1, j + 1, n, m)):
        if text_grid[i + 1][j + 1] not in non_symbols:
            return True
 
    return False

def create_grid(lines):
    result = []
    for line in lines:
        chars = []
        for char in line:
            chars.append(char)
        result.append(chars)

    return result

if __name__ == '__main__':
    file = open('../input.txt', 'r')
    lines = file.readlines()

    text_grid = create_grid(lines)
    n = len(text_grid)
    m = len(text_grid[0])

    part_numbers = []
    number = ''
    adjacent_to_symbol = False

    for i, row in enumerate(text_grid):
        for j, char in enumerate(row):
            if char.isdigit():
                number += char
                if not adjacent_to_symbol:
                    adjacent_to_symbol = check_surroundings(i, j)
            elif number:
                if adjacent_to_symbol:
                    part_numbers.append(int(number))
                number = ''
                adjacent_to_symbol = False            
    
    print(sum(part_numbers))