def get_input(file_name):
    file_list = []
    with(open(file_name, 'r')) as file:
        for line in file:
            file_list.append(line.strip())

    return file_list

def is_valid_pos(row, col, row_len, col_len):
    if row < 0 or col < 0 or row >= row_len or col >= col_len:
        return False
    return True

def count_adjacent_rolls(row, col, file_list):
    row_len = len(file_list)
    col_len = len(file_list[row])

    adjacent_rolls = 0

    if is_valid_pos(row - 1, col - 1, row_len, col_len):
        if file_list[row - 1][col - 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row - 1, col, row_len, col_len):
        if file_list[row - 1][col] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row - 1, col + 1, row_len, col_len):
        if file_list[row - 1][col + 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row, col - 1, row_len, col_len):
        if file_list[row][col - 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row, col + 1, row_len, col_len):
        if file_list[row][col + 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row + 1, col - 1, row_len, col_len):
        if file_list[row + 1][col - 1] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row + 1, col, row_len, col_len):
        if file_list[row + 1][col] == '@':
            adjacent_rolls += 1
    if is_valid_pos(row + 1, col + 1, row_len, col_len):
        if file_list[row + 1][col + 1] == '@':
            adjacent_rolls += 1

    return adjacent_rolls

def evaluate_roll(row, col, file_list):
    adjacent_rolls = 0
    
    if file_list[row][col] == '.':
        return 0
    
    #if its in a corner, it has fewer than 4 adjacent rolls
    #if (row == 0 and col == 0) or (row == 0 and col == len(file_list[row])-1) or (row == len(file_list)-1 and col == 0) or (row == len(file_list)-1 and col == len(file_list[row])-1):
    #    return 1
    
    adjacent_rolls = count_adjacent_rolls(row, col, file_list)

    if adjacent_rolls < 4:
        return 1
    return 0

def evaluate_list(file_list):

    valid_rolls = 0

    for i in range(0, len(file_list)):
        for j in range(0, len(file_list[i])):
            valid_rolls += evaluate_roll(i, j, file_list)

    return valid_rolls

def play_game(file_list):

    total_valid_rolls= evaluate_list(file_list)
    
    return total_valid_rolls    

if __name__ == "__main__":
    print("Solution: ", play_game(get_input("input.txt")))